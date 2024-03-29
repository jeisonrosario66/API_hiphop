import mysql.connector
from mysql.connector import Error
import os
from src.errors_handling.msg_exception import msg_exception

def create_db_connection():
    """
    Returns:
        MYSQL: Connection
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )
        return connection
    except Error as ex:
        print(msg_exception(create_db_connection,ex))
        
    
def close_db_connection(connection):
    if connection:
        connection.close()
