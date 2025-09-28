from pyfile.systorage import Systorage
import os

class File(Systorage):
    """
    Class representing a file in the storage system.

    This class extends `Systorage` and provides methods
    to manipulate files in the filesystem: creation, reading, 
    writing, deletion, etc.
    """

    _extension: str

    def __init__(self, path: str):
        """
        Initialize a File object with the given path.

        Args:
            path (str): Absolute or relative path to the file.

        Raises:
            Exception: If the path exists but is not a file.
        """
        super().__init__(path)
        if self.exists() and not os.path.isfile(path):
            raise Exception(f"\"{path}\" is not a file.")

    def get_extension(self) -> str:
        """
        Return the file extension (e.g. ".txt").

        Returns:
            str: File extension including the dot.
        """
        path = self.get_path()
        return path[path.rfind("."):len(path)]
    
    def get_name(self, with_extension: bool = False) -> str:
        """
        Return the file name, with or without extension.

        Args:
            with_extension (bool, optional): Include the extension if True.
                                             Defaults to False.

        Returns:
            str: File name.
        """
        return super().get_name() + (self.get_extension() if with_extension else "")
    
    def create(self) -> bool:
        """
        Create the file if it does not already exist.

        Returns:
            bool: True if the file exists after creation, False otherwise.
        """
        self.get_path_object().touch(exist_ok=True)
        return self.exists()

    def append(self, text_to_append: str) -> None:
        """
        Append text at the end of the file.

        Args:
            text_to_append (str): Content to append.
        """
        with open(self.get_path(), "a") as fs:
            fs.write(text_to_append)

    def write(self, text_to_write: str) -> None:
        """
        Write text into the file, overwriting its content if it exist.

        Args:
            text_to_write (str): New file content.
        """       
        with open(self.get_path(), "w") as fs:
            fs.write(text_to_write)

    def read_to_end(self, unexisting_raise: bool = True) -> str:
        """
        Read and return the entire file content.

        Args:
            unexisting_raise (bool, optional): 
                If True (default), raises an exception if the file does not exist.
                If False, returns an empty string in that case.

        Returns:
            str: File content.

        Raises:
            Exception: If the file does not exist and `unexisting_raise` is True.
        """
        file_text_content = ""
        if not self.exists():
            if unexisting_raise:
                raise Exception(f"\"{self.get_path()}\" file do not exist.")
        else:
            with open(self.get_path(), "r") as fs:
                fs.seek(0)
                file_text_content = fs.read()
        return file_text_content

    def delete_content(self) -> bool:
        """
        Delete the content of the file (clear it without removing the file).

        Returns:
            bool: True if the content was cleared, False if the file does not exist.
        """
        if self.exists() == False:
            return False
        self.write("")
        return True

    def delete(self, delete_content: bool = False) -> bool:
        """
        Delete the file from the filesystem.

        Args:
            delete_content (bool, optional): 
                If True, clears the file before deleting it. 
                Defaults to False.

        Returns:
            bool: True if the file was deleted, False otherwise.
        """
        if not self.exists(): return False
        if delete_content: self.delete_content()
        os.remove(self.get_path())
        return self.exists() == False