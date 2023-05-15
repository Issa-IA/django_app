#Install Mysql on your computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector-python
#pip install mysql-connector

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='crmdjan',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

""" for create new database
import mysql.connector
connection = mysql.connector.connect(host='localhost',                                         
                                           user='root',
                                           password='')

cursor = connection.cursor()
cursor.execute("create database crmdjan")
print("All done")
"""