from utils import get_connection
from config import connection_url
from models import Class
db = get_connection(connection_url)



Class.db = db

object_class = Class(
    'DataBase',
    'teacher 1',
    'Monday 10:30'
)
object_class.create_class()
