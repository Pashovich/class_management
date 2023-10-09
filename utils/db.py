from pymongo import MongoClient


def get_connection(url):
    try:
        client = MongoClient(url, serverSelectionTimeoutMS = 2000)  
        client.server_info()
        db = client["class_management_system"]
        return db
    except Exception as e:
        print(e)
        return None