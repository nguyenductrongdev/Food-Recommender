import pymongo
import logging
import mysql.connector
import configparser
import os

CONFIG_PATH = os.path.abspath(f"{__file__}/../../config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# MYSQL section config
db = mysql.connector.connect(
    host=config['MYSQL']['HOST'],
    user=config['MYSQL']['USER'],
    password=config['MYSQL']['PASSWORD'],
    database=config['MYSQL']['NAME']
)
cursor = db.cursor(dictionary=True)

# MONGODB section config
mongo_db_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_db_client[config["MONGODB"]["NAME"]]

if __name__ == "__main__":
    # mongo_db.insert_one({"Hello", "world"})
    pass
