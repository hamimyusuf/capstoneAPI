import mysql.connector

def conn():
    mydb = mysql.connector.connect(
    host="mysqldb",
    port=3306,
    user="root",
    password="123",
    database="capstone_db"
    )
    cursor = mydb.cursor()
    return {
        "conn": mydb,
        "cursor": cursor
    }
