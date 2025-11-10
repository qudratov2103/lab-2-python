class UndoCommand(Command):
    """Команда undo"""
    
    def execute(self, args):
        recent = self.shell.history.get_recent(1)
        if recent:
            print(f"Last command was: {recent[0]}")
