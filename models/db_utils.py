import logging
import mysql.connector
import configparser
import os

CONFIG_PATH = os.path.abspath(f"{__file__}/../../config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

db = mysql.connector.connect(
    host=config['DATABASE']['HOST'],
    user=config['DATABASE']['USER'],
    password=config['DATABASE']['PASSWORD'],
    database=config['DATABASE']['DATABASE']
)

cursor = db.cursor(dictionary=True)


# def query(query_string: str, param=None):
#     try:
#         logging.getLogger("__main__").debug(f"query_string: {query_string}")
#         cursor.execute(query_string, param)
#         if param:
#             db.commit()
#         return cursor.fetchall()
#     except Exception as e:
#         logging.getLogger("__main__").exception(e)
#         raise
