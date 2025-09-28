from __future__ import annotations
import pyfile
import os
from .utils import *

class Directory(pyfile.Systorage):
    """
    Class representing a directory in the filesystem.

    This class extends `Systorage` and provides methods 
    to load, list, and explore the files and subdirectories 
    contained inside a directory.
    """

    _files: list[pyfile.File] = []
    _directories: list[Directory] = []

    def __init__(self, path: str, auto_load: bool = False):
        """
        Initialize a Directory object with the given path.

        Args:
            path (str): Absolute or relative path to the directory.
            auto_load (bool, optional): If True, automatically loads files 
                                        and subdirectories at initialization.
                                        Defaults to False.

        Raises:
            Exception: If the path exists but is not a directory.
        """
        super().__init__(path)
        if self.exists() and not os.path.isdir(path):
            raise Exception(f"\"{path}\" is not a folder.")
        if auto_load:
            self.load(True)

    def load(self, recursive_load: bool = False) -> None:        
        """
        Load files and subdirectories contained in this directory.

        Args:
            recursive_load (bool, optional): 
                If True, also loads all subdirectories recursively.
                Defaults to False.
        """
        self._files = pyfile.Path(self.get_path()).get_files()
        self._directories = pyfile.Path(self.get_path()).get_directories(recursive_load)

    def get_files_paths(
        self, 
        recursively: bool = False, 
        segmentation: bool = False
    ) -> list[dict[str, list[str]]] | list[str]:
        """
        Retrieve the paths of all files contained in this directory.

        Args:
            recursively (bool, optional): 
                If True, includes files from subdirectories recursively.
                Defaults to False.
            segmentation (bool, optional): 
                If True, groups results by directory in a dict form: 
                {directory_path: [file_paths]}.
                If False (default), returns a flat list of file paths.

        Returns:
            list[str] | list[dict[str, list[str]]]: 
                A flat list of file paths, or a segmented dictionary-based list.
        """
        self_files_paths = list(map(lambda x: x.get_path(), self._files))
        to_return = [{self.get_path(): self_files_paths} if segmentation else self_files_paths]
        if recursively:
            for dir in self._directories:
                to_return.append(dir.get_files_paths(recursively, segmentation))
        return flatten(to_return)
    
    def get_files(
        self, 
        recursively: bool = False, 
        segmentation: bool = False
    ) -> list[dict[pyfile.Directory, list[pyfile.File]]] | list[pyfile.File]:
        """
        Retrieve file objects contained in this directory.

        Args:
            recursively (bool, optional): 
                If True, includes files from subdirectories recursively.
                Defaults to False.
            segmentation (bool, optional): 
                If True, groups results by directory in a dict form:
                {Directory: [File]}.
                If False (default), returns a flat list of File objects.

        Returns:
            list[pyfile.File] | list[dict[pyfile.Directory, list[pyfile.File]]]: 
                A flat list of File objects, or a segmented dictionary-based list.
        """
        to_return = [{self: self._files} if segmentation else self._files]
        if recursively:
            for dir in self._directories:
                to_return.append(dir.get_files(recursively, segmentation))
        return flatten(to_return)

    def get_directories_paths(
        self, 
        recursively: bool = False, 
        segmentation: bool = False
    ) -> list[dict[str, list[str]]] | list[str]:
        """
        Retrieve the paths of all subdirectories contained in this directory.

        Args:
            recursively (bool, optional): 
                If True, includes subdirectories of all nested directories recursively.
                Defaults to False.
            segmentation (bool, optional): 
                If True, groups results by directory in a dict form:
                {directory_path: [subdirectory_paths]}.
                If False (default), returns a flat list of subdirectory paths.

        Returns:
            list[str] | list[dict[str, list[str]]]: 
                A flat list of subdirectory paths, or a segmented dictionary-based list.
        """
        self_directories_paths = list(map(lambda x: x.get_path(), self._directories))
        to_return = [{self.get_path(): self_directories_paths} if segmentation else self_directories_paths]
        if recursively:
            for dir in self._directories:
                to_return.append(dir.get_directories_paths(recursively, segmentation))
        return flatten(to_return)
    
    def get_directories(
        self, 
        recursively: bool = False, 
        segmentation: bool = False
    ) -> list[dict[pyfile.Directory, list[pyfile.Directory]]] | list[pyfile.Directory]:
        """
        Retrieve subdirectory objects contained in this directory.

        Args:
            recursively (bool, optional): 
                If True, includes subdirectories of all nested directories recursively.
                Defaults to False.
            segmentation (bool, optional): 
                If True, groups results by directory in a dict form:
                {Directory: [subdirectories]}.
                If False (default), returns a flat list of Directory objects.

        Returns:
            list[pyfile.Directory] | list[dict[pyfile.Directory, list[pyfile.Directory]]]: 
                A flat list of Directory objects, or a segmented dictionary-based list.
        """
        to_return = [{self: self._directories} if segmentation else self._directories]
        if recursively:
            for dir in self._directories:
                to_return.append(dir.get_directories(recursively, segmentation))
        return flatten(to_return)
