from bson.objectid import ObjectId
from functions.connection import conn
import mysql.connector
from passlib.hash import sha256_crypt


connection = conn()


# Login User
async def LoginUser(DataUser: dict) -> dict:
    sql = "SELECT * FROM USER WHERE username = %s"
    username = str(DataUser["username"])
    password = str(DataUser["password"])
    connection["cursor"].execute(sql, (username, ))
    check = connection["cursor"].fetchone()
    if check:
        print(check)
        verif = sha256_crypt.verify(password, check[2])
        if verif:
            return "Login Success" 
    return "Username or Password are invalid"
    
       