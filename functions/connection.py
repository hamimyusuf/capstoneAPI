import mysql.connector

def conn():
    mydb = mysql.connector.connect(
    host="localhost",
    port=3308,
    user="root",
    password="123",
    database="capstone_db"
    )
    cursor = mydb.cursor()
    return {
        "conn": mydb,
        "cursor": cursor
    }
