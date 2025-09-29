import os
from pathlib import Path
from typing import Union

__version__ = '1.0.2'
__all__ = ['PackageIsDebug', 'package_is_debug', 'get_directory', 'chdir', '__version__']


def get_filename(path: str, raise_error: bool = True) -> str:
    if '/' in path:
        output = path.split('/')[-1]
    elif '\\' in path:
        output = path.split('\\')[-1]
    else:
        output = path

    if not os.path.isfile(path) and raise_error:
        raise FileNotFoundError('No such file: ' + path)
    else:
        return output


def get_extension(path: str, raise_error: bool = True) -> str:
    filename = get_filename(path, raise_error)
    return filename.split('.')[-1] if '.' in filename else ''


class PackageIsDebug:
    def __init__(self, file: Union[Path, str], tree_level: int = 1):
        file = file if isinstance(file, Path) else Path(file)
        if not file.is_file() or not file.exists() or get_extension(str(file)) != 'py':
            raise FileNotFoundError
        self.file = file
        self.tree_level = tree_level

    def get_directory(self):
        file = self.file
        for level in range(self.tree_level + 2):
            file = file.parent
        if not file.is_dir():
            raise NotADirectoryError
        return file

    def is_debug(self):
        return self.get_directory().name != 'site-packages'

    def chdir(self):
        if not self.is_debug():
            os.chdir(self.get_directory())


def get_directory(file: Union[Path, str], tree_level: int = 1):
    return PackageIsDebug(file, tree_level).get_directory()


def package_is_debug(file: Union[Path, str], tree_level: int = 1):
    return PackageIsDebug(file, tree_level).is_debug()


def chdir(file: Union[Path, str], tree_level: int = 1):
    PackageIsDebug(file, tree_level).chdir()
