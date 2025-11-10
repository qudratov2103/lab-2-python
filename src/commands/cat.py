class CatCommand(Command):
    """Команда cat"""
    
    def execute(self, args):
        if not args:
            raise ValueError("Usage: cat <filename>")
        
        file_path = self.get_absolute_path(args[0])
        content = self.shell.file_manager.read_file(file_path)
        print(content)
        