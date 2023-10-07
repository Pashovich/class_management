from utils import get_connection, clear
from config import connection_url
from models import BaseManager
from commands import commands_map, promt

db = get_connection(connection_url)
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