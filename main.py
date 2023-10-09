from utils import get_connection, clear
from models import BaseManager
from commands import commands_map, promt

try:
    from config import connection_url
except ImportError:
    print("config.py does not exists. Created config.py. Please provide url. connection_url = 'url'. ")
    with open('config.py', 'w') as file:
        file.write("connection_url = ''")
    exit()

db = get_connection(connection_url)
if not db:
    print('Invalid Connection.')
    exit()
BaseManager.db_manager = db

while True:
    print()
    command_name = input(promt)
    if command_name == 'stop':
        break
    func = commands_map.get(command_name, None)
    clear()
    if func is None:
        print("Select from the command list")
        continue
    func()