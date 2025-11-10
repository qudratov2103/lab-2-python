class HistoryCommand(Command):
    """Команда history"""
    
    def execute(self, args):
        count = int(args[0]) if args and args[0].isdigit() else 10
        commands = self.shell.history.get_recent(count)
        
        for i, cmd in enumerate(commands, 1):
            print(f"{i:3}: {cmd}")
