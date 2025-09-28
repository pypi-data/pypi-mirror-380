from pathlib import Path as plPath
import pyfile.path as PiFilePath

class Systorage:
    """
    Base class representing a storage element in the filesystem.

    This class serves as a foundation for filesystem-related objects 
    (such as files or directories). It wraps around a custom `Path` object 
    and provides access to metadata such as the element's name, parent name, 
    and path, along with utilities to check for its existence.
    """

    _path: PiFilePath.Path
    _parent_name: str
    _self_name: str

    def __init__(self, path: str):
        """
        Initialize a Systorage object with the given path.

        Args:
            path (str): Absolute or relative path to the storage element.
        """
        self._path = PiFilePath.Path(path)
        self._parent_name = self._path.get_parent_name()
        self._name = self._path.get_name()

    def exists(self) -> bool:
        """
        Check whether the storage element exists in the filesystem.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        return self.get_path_object().exists()

    # Getters
    def get_name(self) -> str:
        """
        Get the name of the storage element (without parent path).

        Returns:
            str: Name of the element (e.g. "file.txt").
        """
        return self._name
    
    def get_parent_name(self) -> str:
        """
        Get the name of the parent directory of the storage element.

        Returns:
            str: Name of the parent directory.
        """
        return self._parent_name
    
    def get_path(self) -> str:
        """
        Get the full literal path to the storage element.

        Returns:
            str: Path as a string.
        """
        return self._path.get_literal()
        
    def get_path_object(self) -> plPath:
        """
        Get the internal `pathlib.Path` object representing this element.

        Returns:
            pathlib.Path: Path object for advanced operations.
        """
        return self._path.get_internal()