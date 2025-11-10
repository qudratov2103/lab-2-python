class GrepCommand(Command):
    """Команда grep"""
    
    def execute(self, args):
        if len(args) < 2:
            raise ValueError("Usage: grep <pattern> <path> [-r] [-i]")
        
        pattern = args[0]
        search_path = self.get_absolute_path(args[1])
        recursive = '-r' in args
        ignore_case = '-i' in args
        
        results = self.shell.search.grep(pattern, search_path, recursive, ignore_case)
        
        for result in results:
            print(f"{result['file']}:{result['line_number']}: {result['content']}")
            