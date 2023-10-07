from pymongo import MongoClient


def get_connection(url):
    client = MongoClient(url)  
    db = client["class_management_system"]
    return db