import sys, os
from .command import ExecuteCommand
from pathlib import Path
class ExecuteEnvironment:
    """Класс инициализации виртуальной среды"""
    args = list
    commands = []
    def __init__(self, args):
        self.args = args
        self.commands.append(ExecuteCommand(
            name= "ExecuteExpetiment",
            description= "Запуск виртуальной среды эксперимента"
        ).dict_parser())
        
    def initialize(self):
        if "-h" in self.args:
            self.help_info()
        elif "ExecuteExperiment" in self.args:
            self.execute(self.args[1])

    def execute(self, dir: str):
        os.environ["MODCHEM_INIT"] = os.path.join(os.getcwd(), dir)
        try:
            os.mkdir(os.getenv("MODCHEM_INIT"))
            #file_path = Path(f'{os.getenv("MODCHEM_INIT")}/settings.py')
        except FileExistsError:
            sys.stderr.write(f"Путь {os.getenv("MODCHEM_INIT")} уже занят")

    def help_info(self):
        """Вывести информацию о текущих командах"""
        sys.stdout.write("Команды\n")
        for command in self.commands:
            self.info(command)
        
    def info(self, command):
        sys.stdout.write(f"\t{command["name"]} - {command["description"]}")

def execute_experiment_environment(argv: str):
    execute = ExecuteEnvironment(args=argv)
    execute.initialize()