import mysql.connector
from mysql.connector import Error
from pymongo import MongoClient
import pymongo
import motor.motor_asyncio

def conn():
    try:
        mydb = mysql.connector.connect(
            host="mysqldb",
            port=3306,
            user="root",
            password="123",
            database="capstone_db",
            autocommit=True
        )
        cursor = mydb.cursor()
        return {
            "conn": mydb,
            "cursor": cursor
        }
    except Error as e:
        print(f"Kesalahan koneksi MySQL: {e}")
        print("Mencoba koneksi ulang...")
        # Menjalankan kembali fungsi conn() secara rekursif
        return conn()
        

def conmongo():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:123@mongodb:27017/')
    db = client.capstone_db
    dbinfo = db["information"]
    return dbinfo

def mongoconn():
    myclient = pymongo.MongoClient("mongodb://root:123@mongodb:27017/")
    mydb = myclient["capstone_db"]
    mycol = mydb["information"]
    return mycol




