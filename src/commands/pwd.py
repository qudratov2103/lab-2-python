class PrintWorkingDirectoryCommand(Command):
    """Команда pwd"""
    
    def execute(self, args):
        print(self.shell.current_dir)