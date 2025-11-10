class UnzipCommand(Command):
    """Команда unzip"""
    
    def execute(self, args):
        if not args:
            raise ValueError("Usage: unzip <archive>")
        
        archive = self.get_absolute_path(args[0])
        self.shell.archive_manager.extract_zip(archive)
        print(f"Извлечен: {archive}")
