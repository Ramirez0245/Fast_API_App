from pymongo import MongoClient
import os

def Mongo_Collection(collection_name):
    CLIENT = MongoClient(os.getenv('CONNECTION_STRING'))
    DB = CLIENT['CLOUD_DATABASE']
    COLLECTION = DB['COLLECTION_USERS']    
    return COLLECTION


