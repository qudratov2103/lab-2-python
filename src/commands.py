"""Имплементации комманд shell"""

from pathlib import Path


class Command:
    """База"""
    
    def __init__(self, shell):
        self.shell = shell
    
    def get_absolute_path(self, path_str):
        path_obj = Path(path_str)
        if not path_obj.is_absolute():
            path_obj = self.shell.current_dir / path_obj
        return path_obj.resolve()
