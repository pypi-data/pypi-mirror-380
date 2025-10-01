import sys
from src.modchem.commands import ExecuteEnvironment
def start_app(argv: str):
    execute = ExecuteEnvironment(args=argv)
    execute.initialize()

if __name__ == "__main__":
    start_app(sys.argv[1:])