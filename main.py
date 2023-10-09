from utils import get_connection, clear
from models import BaseManager
from commands import commands_map, promt

import os 
from dotenv import load_dotenv

load_dotenv('.env')


def main():
    db = get_connection(os.getenv('CONNECTION_URL'))
    if db == None:
        print('Invalid Connection.')
        return
    BaseManager.db_manager = db

    while True:
        command_name = input(promt)
        if command_name == 'stop':
            return
        func = commands_map.get(command_name, None)
        clear()
        if func is None:
            print("Select from the command list")
            continue
        output = func()
        clear()
        if isinstance(output, str):
            print(output + '\n')

if __name__ == '__main__':
    main()