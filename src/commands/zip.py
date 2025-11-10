class ZipCommand(Command):
    """Команда zip"""
    
    def execute(self, args):
        if len(args) < 2:
            raise ValueError("Usage: zip <folder> <archive_name>")
        
        folder = self.get_absolute_path(args[0])
        archive_path = self.shell.archive_manager.create_zip(folder, args[1])
        print(f"Создан архив: {archive_path}")
