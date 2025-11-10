class MoveCommand(Command):
    """Команда mv"""
    
    def execute(self, args):
        if len(args) < 2:
            raise ValueError("Usage: mv <source> <destination>")
        
        source = self.get_absolute_path(args[0])
        destination = self.get_absolute_path(args[1])
        
        self.shell.file_manager.move_file(source, destination)
        print(f"Переместио {source} к {destination}")
