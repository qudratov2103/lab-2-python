class UntarCommand(Command):
    """Команда untar"""
    
    def execute(self, args):
        if not args:
            raise ValueError("Usage: untar <archive>")
        
        archive = self.get_absolute_path(args[0])
        self.shell.archive_manager.extract_tar(archive)
        print(f"Извлечен: {archive}")
