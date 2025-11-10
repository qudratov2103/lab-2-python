class CopyCommand(Command):
    """Команда cp"""
    
    def execute(self, args):
        if len(args) < 2:
            raise ValueError("Usage: cp <source> <destination> [-r]")
        
        recursive = '-r' in args
        source_args = [arg for arg in args if arg != '-r']
        
        if len(source_args) < 2:
            raise ValueError("Usage: cp <source> <destination> [-r]")
        
        source = self.get_absolute_path(source_args[0])
        destination = self.get_absolute_path(source_args[1])
        
        self.shell.file_manager.copy_file(source, destination, recursive)
        print(f"Скопировал {source} на {destination}")
