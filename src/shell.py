from pathlib import Path

from .commands.cat import CatCommand
from .commands.cd import ChangeDirectoryCommand
from .commands.exit import ExitCommand
from .commands.grep import GrepCommand
from .commands.help import HelpCommand
from .commands.history import HistoryCommand
from .commands.ls import ListCommand
from .commands.mv import MoveCommand
from .commands.pwd import PrintWorkingDirectoryCommand
from .commands.rm import RemoveCommand
from .commands.tar import TarCommand
from .commands.undo import UndoCommand
from .commands.untar import UntarCommand
from .commands.unzip import UnzipCommand
from .commands.zip import ZipCommand



class MiniShell:
    """База"""
    
    def __init__(self):
        self.current_dir = Path.cwd()
        self.running = False
        
        # Компоненты
        self.logger = ShellLogger()
        self.history = CommandHistory()
        self.file_manager = FileManager()
        self.archive_manager = ArchiveManager()
        self.search = FileSearch()
        
        # Команды
        self._setup_commands()
    
    def _setup_commands(self):
        """Доступные команды"""
        self.commands = {
            'ls': ListCommand(self),
            'cd': ChangeDirectoryCommand(self),
            'cat': CatCommand(self),
            'cp': CopyCommand(self),
            'mv': MoveCommand(self),
            'rm': RemoveCommand(self),
            'pwd': PrintWorkingDirectoryCommand(self),
            'zip': ZipCommand(self),
            'unzip': UnzipCommand(self),
            'tar': TarCommand(self),
            'untar': UntarCommand(self),
            'grep': GrepCommand(self),
            'history': HistoryCommand(self),
            'undo': UndoCommand(self),
            'exit': ExitCommand(self),
            'help': HelpCommand(self),
        }
    
    def run(self):
        """Start the shell main loop."""
        self.running = True
        print("Shell запущен введите exit чтобы выйти.")
        
        while self.running:
            try:
                pass
                
                if user_input:
                    self._perform_command(user_input)
                    
            except KeyboardInterrupt:
                print("\nИспользуйте 'exit' чтобы выйти")
            except EOFError:
                self._perform_command("exit")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
                self.logger.log_error(f"Неожиданная ошибка: {e}")
    
    def _perform_command(self, command_line):
        """Выполнение команды"""
        # история
        self.history.add_command(command_line)
        
        # парсинг команд
        parts = command_line.split()
        command_name = parts[0].lower()
        args = parts[1:]
        
        # выполнение команд
        pass