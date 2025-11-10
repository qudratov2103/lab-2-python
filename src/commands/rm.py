class RemoveCommand(Command):
    """Команда rm"""
    
    def execute(self, args):
        if not args:
            raise ValueError("Usage: rm <target> [-r]")
        
        recursive = '-r' in args
        target_args = [arg for arg in args if arg != '-r']
        
        if not target_args:
            raise ValueError("Usage: rm <target> [-r]")
        
        target = self.get_absolute_path(target_args[0])
        
        if self.shell.file_manager.delete_file(target, recursive):
            print(f"Удалён {target}")
