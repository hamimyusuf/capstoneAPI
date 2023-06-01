from bson.objectid import ObjectId
from functions.connection import conn
import mysql.connector
from passlib.hash import sha256_crypt


connection = conn()


def FormHelper(UserData) -> dict:
    return{
        "username": str(UserData[0]),
        "name": str(UserData[1])
    }

# add new user to database
async def addUser(DataUser: dict) -> dict:
    sql = "SELECT * FROM USER WHERE username = %s"
    username = str(DataUser["username"])
    connection["cursor"].execute(sql, (username,))
    check = connection["cursor"].fetchone()
    if check is not None:
        return "Username Has Already Use"
    
    password = sha256_crypt.encrypt(DataUser["password"])

    sql = "INSERT INTO USER (username, name, password) VALUES (%s, %s, %s)"
    val = (DataUser["username"],DataUser["name"],password)
    connection["cursor"].execute(sql, val)
    connection["conn"].commit()
    sql = "SELECT * FROM USER WHERE username = %s"
    username = str(DataUser["username"])
    connection["cursor"].execute(sql, (username,))
    newUser = connection["cursor"].fetchone()

    if newUser is not None:
        return FormHelper(newUser)
    else:
        return None