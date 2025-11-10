class ExitCommand(Command):
    """Команда exit"""
    
    def execute(self, args):
        print("Пока!")
        self.shell.running = False