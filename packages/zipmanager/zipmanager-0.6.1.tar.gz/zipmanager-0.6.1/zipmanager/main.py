import binascii
import hashlib
import io
from os import path
import logging
import re
import zipfile
import base64
from json.decoder import JSONDecodeError
from contextlib import redirect_stdout

from .Exceptions import (FileNameConflict, ExternalClassOperation,
                         FileNotFound, BytesDecodeError, UnsupportedDataType,
                         Base64DecodingError, EmptyFileName, ZipDecodeError,
                         UnsupportedOption, FormatError, FileAlreadyExists,
                         FolderNameConflict, UnsupportedValueType)
from .File import File, MetaData


class ZipFolder:
    """
    The ZipFolder object holds all the files and data as a zip.
    """
    def __init__(self, data, experimental=False):
        """
        the data for the zip can be one of the following:

        - dictionary of file names and file data pairs (file data can be bytes, str for .txt or dict/list for .json)
        - set of file names (will create a base file based on file extension)
        - base64 str of a zip (from the get_b64 function)
        - path of the zip file (must have the .zip extension)
        - zip bytes (from the get_bytes function)

        :param data:                the data for the zip
        :type data:                 dict[str, dict] | dict[str, str] | dict[str, bytes] | dict[str, ZipFolder] |
                                    set[str] | str | bytes
        :param experimental:        used for testing experimental features, False by default.
        :type experimental:         bool
        """
        self.__metadata = {}
        self.experimental = experimental
        match data:
            case dict():
                self.__raw_zip = self.__create_zip(data)
            case set():
                self.__raw_zip = self.__create_zip(self.__create_base_dict(data))
            case str():
                self.__raw_zip = self.__b64_to_zip(data) if not File.is_path(data) \
                    else self.__bytes_to_zip(File.open_file(data))
                self.__add_metadata()
            case bytes():
                self.__raw_zip = self.__bytes_to_zip(data)
            case _:
                self.__raise(UnsupportedDataType, type(data))

    def __eq__(self, other):
        self.__check_class(other)
        return self.zip_hash() == other.zip_hash()

    def __add__(self, other):
        self.__check_class(other)
        temp = ZipFolder(self.raw_files())
        for f in other.file_list:
            if f not in temp.file_list:
                temp.add_file(f, other[f])
        return temp

    def __sub__(self, other):
        self.__check_class(other)
        temp = ZipFolder(self.raw_files())
        for f in self.file_list:
            if f in other.file_list and self[f] == other[f]:
                temp.delete_file(f)
        return temp

    def __and__(self, other):
        """
        Returns all files that are in both ZipFile objects.
        :type other: ZipFolder
        """
        self.__check_class(other)
        temp = ZipFolder({})
        for f in self.file_list:
            if f in other.file_list and self[f] == other[f]:
                temp.add_files({f: self[f]})
        return temp

    def __or__(self, other):
        """
        Returns all files that are in both ZipFile objects.
        :type other: ZipFolder
        """
        self.__check_class(other)
        temp = ZipFolder({})
        for f in self.file_list:
            if not (f in other.file_list and self[f] == other[f]) and f not in temp.file_list:
                temp.add_files({f: self[f]})
        for f in other.file_list:
            if not (f in self.file_list and self[f] == other[f]) and f not in temp.file_list:
                temp.add_files({f: other[f]})
        return temp

    def __lshift__(self, other):
        self.__check_class(other)
        for file in other.file_list:
            self.add_file(file, other[file])

    def __getitem__(self, file_name: str):
        if file_name in self.file_list:
            return File.unpack(file_name, self.__raw_zip.open(file_name).read())
        self.__raise(FileNotFound, file_name)
        return None

    def __setitem__(self, key, value):
        if key not in self.file_list:
            self.add_file(key, value)
        elif File.get_extension(key) != 'zip':
            self.update_file(key, value) if key in self.file_list else self.add_file(key, value)
        elif type(value) in [list, set, str, dict, bytes]:
            self.update_file(key, ZipFolder(value))

    def __str__(self):
        return (f'Zipfile Object {self:id} / '
                f'file number: {self:nfiles} / '
                f'size: {self:,size} bytes / '
                f'compressed size: {self:,csize} bytes')

    def __format__(self, format_spec: str):
        match re.sub(r'[ ,]', '', format_spec):
            case 'id':
                txt = str(hex(id(self)).upper())
                format_spec = format_spec.replace('id', '')
            case 'size':
                txt = self.get_size()
                format_spec = format_spec.replace('size', '')
            case 'csize' | 'c_size':
                txt = self.get_size(compressed=True)
                format_spec = re.sub(r'(csize|c_size)', '', format_spec)
            case 'nfiles' | 'n_files':
                txt = len(self.file_list)
                format_spec = re.sub(r'(nfiles|n_files)', '', format_spec)
            case 'files':
                txt = str(self.file_list)[1:-1]
                format_spec = format_spec.replace('files', '')
            case _:
                txt = str(self)
        try:
            return format(txt, format_spec)
        except (TypeError ,ValueError):
            self.__raise(FormatError, format_spec)
            return None

    def experimental_info(self):
        """
        prints out current experimental features.
        """
        print(
            f'Current list of experimental features:\n'
            f'\t• automatic deletion of redundant paths in the file_list and the raw zip object'
            f'\nexperimental features are currently {"enabled" if self.experimental else "disabled"}\n'
            f'please submit bugs at: https://github.com/SimplePythonCoder/zipmanager/issues/new?template=bug-report.yml'
              )

    def set_comment(self, comment, file_name=None):
        """
        sets comments to the  entire ZipFolder or specific files

        :param comment:         comment to set
        :type comment:          str
        :param file_name:       file to set a comment to. if None (is by default) will set for the entire ZipFolder
        :type file_name:        str
        """
        if file_name is None:
            self.__raw_zip.comment = comment.encode()
        elif file_name in self.file_list:
            self.__raw_zip.getinfo(file_name).comment = comment.encode()
        else:
            self.__raise(FileNotFound, file_name)

    def get_comment(self, file_name=None):
        """

        :param file_name:       file to get comment of. if None (is by default) will return the comment of the ZipFolder
        :type file_name:        str
        :return:                comment of the ZipFolder or the specified file
        :rtype:                 str | None
        """
        if not file_name:
            return self.__raw_zip.comment.decode() if self.__raw_zip.comment else None
        if file_name in self.file_list:
            return self.__raw_zip.getinfo(file_name).comment.decode() if self.__raw_zip.getinfo(file_name).comment else None
        else:
            self.__raise(FileNotFound, file_name)
            return None

    def print_zip(self):
        """
        prints the printdir of the ZipFolder
        """
        with io.StringIO() as string:
            with redirect_stdout(string):
                self.__raw_zip.printdir()
            string.seek(0)
            print('\n'.join(string.read().split('\n')[:-1]))

    def file_hash(self, file_name, hash_format='sha256', hex_val=True):
        """
        get hash of a file from the ZipFolder

        :param file_name:           file to get hash of
        :type file_name:            str
        :param hash_format:         hash library to use (sha256 by default).
                                    list here: https://docs.python.org/3/library/hashlib.html#hashlib.md5
        :type hash_format:          str
        :param hex_val:             if false will return the object instead of the hex value (True by default)
        :type hex_val:              bool
        :return:                    hash of the file
        :rtype:                     str | object
        """
        if file_name in self.file_list:
            match File.get_extension(file_name):
                case 'zip':
                    return self[file_name].zip_hash(hash_format, hex_val)
                case _:
                    return getattr(hashlib, hash_format)(self.__raw_zip.read(file_name)).hexdigest() if hex_val \
                    else getattr(hashlib, hash_format)(self.__raw_zip.read(file_name))
        self.__raise(FileNotFound, file_name)
        return None

    def zip_hash(self, hash_format='sha256', hex_val=True):
        """
        returns the hash of the zip data
        :param hash_format:         hash library to use (sha256 by default).
                                    list here: https://docs.python.org/3/library/hashlib.html#hashlib.md5
        :type hash_format:          str
        :param hex_val:             if false will return the object instead of the hex value (True by default)
        :type hex_val:              bool
        :return:                    hash value
        :rtype:                     str | object
        """
        hash_list = {file_name: self.file_hash(file_name, hash_format=hash_format) for file_name in self.file_list}
        return getattr(hashlib, hash_format)(str(hash_list).encode()).hexdigest() if hex_val \
            else getattr(hashlib, hash_format)(str(hash_list).encode())

    def get_creation_datetime(self, file_name):
        """
        returns the creation datetime of a file

        :param file_name:       name to get datetime object for
        :type file_name:        str
        :return:                datetime object representing the creation time of the file
        :rtype:                 datetime
        """
        return self.__metadata[file_name].creation_datetime if file_name in self.file_list \
            else self.__raise(FileNotFound, file_name)

    def get_size(self, file_name=None, compressed=False):
        """
        returns the size of a file or the entire zip.
        can return both compressed and normal size.

        :param file_name:           this will return the size of a specific file (disabled by default)
        :type file_name:            str
        :param compressed:          if true will return the compressed size (false by default)
        :type compressed:           bool
        :return:                    size in bytes of a file or the entire zip
        :rtype:                     int
        """
        size = 0
        match file_name:
            case str():
                if file_name in self.file_list:
                    return getattr(self.__metadata[file_name], 'compress_size' if compressed else 'size')
                self.__raise(FileNotFound, file_name)
            case _:
                for file in self.__raw_zip.filelist:
                    size += getattr(file, 'compress_size' if compressed else 'file_size')
        return size

    def get(self, file_name):
        """
        used to get the data of a specific file.
        if the file not in the ZipFolder, this will return None instead.

        :param file_name:       file name (if inside a folder add 'folder_name/' before the file name)
        :type file_name:        str
        :return:                file data
        :rtype:                 bytes | str | dict | ZipFolder
        """
        return self[file_name] if file_name in self.file_list else None

    def __get_minimal_paths_list(self):
        sorted_file_list = sorted(self.file_list)
        final_list = []
        for first_index in range(len(sorted_file_list)):
            flag = True
            if self.__metadata[sorted_file_list[first_index]].is_folder:
                for second_index in range(first_index+1, len(sorted_file_list)):
                    if sorted_file_list[second_index].startswith(sorted_file_list[first_index]):
                        flag = False
                        break
            if flag:
                final_list.append(sorted_file_list[first_index])

        return final_list

    def __refresh_file_list(self):
        """
        currently only used in experimental mode
        """
        new_file_list = self.__get_minimal_paths_list()
        for f in self.file_list:
            if f not in new_file_list:
                self.delete_file(f)

    def __add_metadata(self):
        for file_name in self.file_list:
            self.__metadata[file_name] = MetaData(self.__raw_zip.getinfo(file_name))

    def create_directory(self, directory):
        """
        creates a directory at the specified path

        :param directory:          name and where the directory should be located.
        :type directory:           str
        """
        if directory.endswith('/'):
            directory = directory[:-1]
        if f'{directory}/' in self.file_list:
            self.__raise(FolderNameConflict, directory)
            return
        self.__change_mode('w')
        self.__raw_zip.writestr(zipfile.ZipInfo(directory+'/'), '')
        self.__metadata[f'{directory}/'] = MetaData(self.__raw_zip.getinfo(f'{directory}/'))
        self.__change_mode('r')
        if self.experimental:
            self.__refresh_file_list()

    def add_file(self, file_name, file_data):
        if file_name in self.file_list:
            self.__raise(FileNameConflict, file_name)
        self.__change_mode('w')
        self.__raw_zip.writestr(file_name, File.pack(file_name, file_data))
        self.__metadata[file_name] = MetaData(self.__raw_zip.getinfo(file_name))
        self.__change_mode('r')
        if self.experimental:
            self.__refresh_file_list()

    def add_files(self, data):
        """
        add files to the zip file.
        you can add folders by adding the folder name before the filename separated by a '/'.

        :param data:            dict of filename as key and data as value
        :type data:             dict[str, dict] | dict[str, str] | dict[str, bytes]
                                | dict[str, ZipFolder] | set[str]
        """
        if temp := [file for file in data if file in self.file_list]:
            self.__raise(FileNameConflict, temp[0])
        match data:
            case dict():
                for file in data:
                    self.add_file(file, data[file])
            case set():
                for file in data:
                    self.add_file(file, File.create_base(File.get_extension(file)))
            case list():
                self.__raise(UnsupportedOption, 'add_files with list')

    def update_file(self, file_name, new_data):
        """
        updates file data, this can also be used to add files

        :param file_name:       name of file to update
        :type file_name:        str
        :param new_data:       new data for the updated files
        :type new_data:        str | bytes | dict | list | ZipFolder
        """
        if file_name in self.file_list:
            temp = self.__metadata[file_name].creation_datetime
            self.delete_file(file_name)
            self.add_file(file_name, new_data)
            self.__metadata[file_name].creation_datetime = temp
            del temp
        else:
            self.__raise(FileNotFound, file_name)

    def update_files(self, update_dict):
        """
        updates file data, this can also be used to add files.
        this is used for multiple file updates.

        :param update_dict:       name of file to update
        :type update_dict:        dict[str, dict] | dict[str, str] | dict[str, bytes] | dict[str, ZipFolder]
        """
        if temp:=[file for file in update_dict.keys() if file not in self.file_list]:
            self.__raise(FileNotFound, temp[0])
        for file, new_data in update_dict.items():
            self.update_file(file, new_data)

    def change_name(self, old_name, new_name):
        """
        change the name of the file.
        for non bytes files the extension should remain.

        :param old_name:        old file name
        :type old_name:         str
        :param new_name:        new file name
        :type new_name:         str
        """
        if old_name not in self.file_list:
            self.__raise(FileNotFound, old_name)
        if old_name != new_name:
            self.__raw_zip.getinfo(old_name).filename = new_name
            self.__metadata[new_name] = self.__metadata.pop(old_name)
            self.__metadata[new_name].name = new_name
            self.__raw_zip.NameToInfo[new_name] = self.__raw_zip.NameToInfo.pop(old_name)
        else:
            self.__log('How did we get here?')

    def delete_file(self, file_name):
        """
        deletes files from the zip file.

        :param file_name:            file name (if inside a folder add 'folder_name/' before the file name)
        :type file_name:             str
        :return:                     success status of the deletion (file not found will return False)
        :rtype:                      bool
        """
        if (file_name in self.file_list) and (temp:=[f for f in self.__raw_zip.filelist if f.filename == file_name]):
            self.__raw_zip.filelist.remove(temp[0])
            del self.__raw_zip.NameToInfo[file_name]
            del self.__metadata[file_name]
            return True
        return False

    def delete_files(self, file_names):
        """
        deletes files from the zip file.

        :param file_names:            set of file names (if inside a folder add 'folder_name/' before the file name)
        :type file_names:             set[str]
        :return:                      dict of file names and of success status of the deletion
                                      (file not found will return False)
        :rtype:                       dict[str, bool]
        """
        if type(file_names) is list:
            self.__log('Warning: usage of list type for delete_files'
                       ' is deprecated as of version 0.5.0')
        return {file: self.delete_file(file) for file in file_names}

    def raw_files(self):
        """
        used to get a dictionary of all files with file names as keys and data as value.
        :return:    A dict of all files as name, data pairs.
        :rtype:      dict
        """
        return {file: self[file] for file in self.file_list}

    @property
    def file_list(self):
        return [file.filename for file in self.__raw_zip.filelist]

    @property
    def metadata(self):
        return self.__metadata.copy()

    @metadata.setter
    def metadata(self, _value):
        self.__raise(UnsupportedOption, 'set metadata')

    def get_b64(self):
        """
        the string this function returns can be used in several ways:

        - saving multiple zip into a single file
        - sending text with an api instead of bytes
        - ZipFolder can read it and convert it to a zip

        :return:        a base64 string of the zip bytes
        :rtype:         str
        """
        return base64.b64encode(self.get_bytes()).decode()

    def get_bytes(self):
        """
        used to get the raw bytes of the zip.
        ZipFolder can use this response to create an identical zip - ZipFolder(some_zipfolder.get_bytes()).

        :return:        the bytes of the zip
        :rtype:         bytes
        """
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as file_zip:
            for file_name in self.file_list:
                file_zip.writestr(file_name, data=File.pack(file_name, self[file_name]))
        zip_buffer.seek(0)
        return zip_buffer.read()

    def __check_class(self, other):
        if type(self) is not type(other):
            self.__raise(ExternalClassOperation, type(other))

    def __change_mode(self, mode):
        self.__raw_zip.mode = mode

    def __create_zip(self, files):
        if '' in files:
            self.__raise(EmptyFileName)
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as file_zip:
            for file_name, data in files.items():
                try:
                    file_zip.writestr(file_name, data=File.pack(file_name, data))
                    self.__metadata[file_name] = MetaData(file_zip.getinfo(file_name))
                except (UnicodeDecodeError, JSONDecodeError):
                    self.__raise(BytesDecodeError, file_name)

        zip_buffer.seek(0)
        return zipfile.ZipFile(zip_buffer, 'r')

    @staticmethod
    def __create_base_dict(names):
        return {name: File.create_base(File.get_extension(name)) for name in names}

    def __bytes_to_zip(self, data):
        try:
            return zipfile.ZipFile(io.BytesIO(data), 'r')
        except zipfile.BadZipfile:
            self.__raise(ZipDecodeError)
            return None

    def __b64_to_zip(self, data):
        try:
            return zipfile.ZipFile(io.BytesIO(base64.b64decode(data)), 'r')
        except (binascii.Error, zipfile.BadZipfile):
            self.__raise(Base64DecodingError)
            return None

    @staticmethod
    def __log(msg, level='warning'):
        getattr(logging.getLogger('zipmanager'), level)(msg)

    @staticmethod
    def __raise(exc, *args, **kwargs):
        raise exc(*args, **kwargs) from None

    def __save(self, path_with_name, data):
        if type(path_with_name) is not str:
            self.__raise(UnsupportedValueType, path_with_name)
        with open(path_with_name, 'wb' if type(data) is bytes else 'w') as fh:
            fh.write(data)

    def save(self, path_with_name='./temp.zip'):
        """
        saves the zip folder to the given location.
        path must be with name (extension optional).
        :param path_with_name:      path for save location (empty will save it to current folder)
        :type path_with_name:       str
        """
        if type(path_with_name) is not str:
            self.__raise(UnsupportedValueType, path_with_name)
        self.__save(path_with_name if path_with_name.endswith('.zip') else path_with_name + '.zip', self.get_bytes())

    def safe_save(self, path_with_name='./temp.zip'):
        """
        saves the zip folder to the given location.
        will fail if file already exists.
        path must be with name (extension optional).
        :param path_with_name:      path for save location (empty will save it to current folder)
        :type path_with_name:       str
        """
        if path.exists(path_with_name):
            self.__raise(FileAlreadyExists, path_with_name)
        self.save(path_with_name)

    def save_file(self, file_name, path_with_name=None):
        """
        :param file_name:       file name to be saved
        :type file_name:        str
        :param path_with_name:            path to be saved to (./file_name by default)
        :type path_with_name:             str
        """
        self.__save(path_with_name if path_with_name else f'./{file_name}', self[file_name])

    def safe_save_file(self, file_name, path_with_name=None):
        """
        :param file_name:               file name to be saved
        :type file_name:                str
        :param path_with_name:          path to be saved to (./file_name by default)
        :type path_with_name:           str
        """
        if type(path_with_name) is str and path.exists(path_with_name):
            self.__raise(FileAlreadyExists, path_with_name)
        elif path.exists(f'./{file_name}'):
            self.__raise(FileAlreadyExists, f'./{file_name}')
        self.__save(path_with_name if path_with_name else f'./{file_name}', self[file_name])

