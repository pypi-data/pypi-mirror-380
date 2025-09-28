from pathlib import Path as path
import pyfile
from pyfile.utils import *
from pyfile.enums import *
import os.path as syspath 

class Path:
    _literal: str
    _internal: path

    def __init__(self, literal: str):
        self._literal = self.format_literal_path(literal)
        self._internal = path(self._literal)

    def exists(self):
        return syspath.exists(self._literal)

    def get_parent_name(self):
        parent_names = self._literal.split("/")
        return parent_names[len(parent_names) -2]

    def get_name(self):
        last_index_of_dot = self._literal.rfind(".")
        return self._literal[self._literal.rfind("/")+1 : len(self._literal) if last_index_of_dot == -1 else last_index_of_dot]

    def get_literal(self):
        return self._literal
    
    def get_internal(self):
        return self._internal
    
    def get_systorage_paths(self, recursively: bool = False):
        return list(map(lambda path: self.format_literal_path(str(path)), (self._internal.rglob if recursively else self._internal.glob)("*")))

    def get_files_paths(self, recursively: bool = False, extensions: list[str] = []):
        extensions = convert_enum_values_to_str(extensions)
        return list(filter(lambda current_path: syspath.isfile(current_path) and (True if len(extensions) == 0 else (current_path[current_path.rfind("."):len(current_path)] in extensions)), self.get_systorage_paths(recursively)))

    def get_files(self, recursively: bool = False, extensions: list[Extensions | str] = []):
        extensions = convert_enum_values_to_str(extensions)
        builded_files = map(lambda path: pyfile.File(path), self.get_files_paths(recursively, extensions))
        return list(builded_files if len(extensions) == 0 else filter(lambda builded_file: builded_file.get_extension() in extensions, builded_files))
    
    def get_directories_paths(self, recursively: bool = False):
        return list(filter(lambda path: syspath.isdir(path), self.get_systorage_paths(recursively)))

    def get_directories(self, recursively: bool = False):
        return list(map(lambda path: pyfile.Directory(path, recursively), self.get_directories_paths()))

    ### Utils methods

    def format_literal_path(self, literal: str) -> str:
        # Replace "\" by "/" (universal path format)
        literal = literal.replace("\\", "/")
        # Remove all "//" occurrences in path to form it well
        while ("//" in literal): literal = literal.replace("//", "/")
        return literal if not literal.endswith("/") else literal[0:-1]