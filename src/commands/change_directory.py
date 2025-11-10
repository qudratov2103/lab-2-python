class ChangeDirectoryCommand(Command):
    """Комманда cd"""
    
    def execute(self, args):
        path = args[0] if args else "~"
        new_dir = self.shell.file_manager.change_directory(path, self.shell.current_dir)
        self.shell.current_dir = new_dir