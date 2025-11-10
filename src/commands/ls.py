class ListCommand(Command):
    """Команда ls"""
    
    def execute(self, args):
        path = self.shell.current_dir
        detailed = False
        
        # параметры команды ls
        for arg in args:
            if arg == '-l':
                detailed = True
            elif not arg.startswith('-'):
                path = self.get_absolute_path(arg)
        
        items = self.shell.file_manager.list_directory(path, detailed)
        
        if detailed:
            for item in items:
                print(f"{item['type']}{item['permissions']} "
                      f"{item['size']:8} "
                      f"{item['modified'].strftime('%Y-%m-%d %H:%M')} "
                      f"{item['name']}")
        else:
            for item in items:
                print(item['name'])