class HelpCommand(Command):
    """Команда help"""
    
    def execute(self, args):
        print("Доступные команды:")
        print("  Файловые операции:")
        print("    ls [path] [-l]      - Список содержимого текущей дериктории")
        print("    cd [path]           - Сменить дерикторию")
        print("    cat <file>          - Отобразить контент файла")
        print("    cp <src> <dest> [-r] - Копировать файлы/дериктории")
        print("    mv <src> <dest>     - Сдвигать/Переименовывать файл")
        print("    rm <target> [-r]    - Удалять файлы/дериктории")
        print("    pwd                 - Показать текущую дерикторию")
        print("")
        print("  Операции архивации:")
        print("    zip <folder> <archive>  - Создать ZIP архив")
        print("    unzip <archive>         - Извлечь ZIP")
        print("    tar <folder> <archive>  - Создать TAR архив")
        print("    untar <archive>         - Извлечь TAR")
        print("")
        print("  Поиск и история:")
        print("    grep <pattern> <path> [-r] [-i] - Поиск в файлах")
        print("    history [n]          - Показать историю команд")
        print("    undo                 - Базовый функционал команды undo")
        print("    help                 - Показать данную информацию")
        print("    exit                 - Выйти из shell")
    