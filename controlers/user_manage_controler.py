from bson.objectid import ObjectId
from functions.connection import conn
import mysql.connector


connection = conn()


def FormHelper(UserData) -> dict:
    return{
        "username": str(UserData[0]),
        "name": str(UserData[1]),
        "password": str(UserData[2])
    }

# show all user data
async def showAllUsers():
    sql = "SELECT * FROM USER"
    connection["cursor"].execute(sql)
    check = connection["cursor"].fetchall()
    if check is None:
        return "Data is Empty"
    data = []
    for temp in check:
        data.append(FormHelper(temp))
    return data 

# show user data by username
async def DataUserByUsername(username: str) -> dict:
    sql = "SELECT * FROM USER WHERE username = %s"
    connection["cursor"].execute(sql, (username,))
    dataUser = connection["cursor"].fetchone()
    if dataUser is None:
        return None
    return FormHelper(dataUser)

# Update data user
async def UpdateUserData(DataUser: dict) -> dict:
    sql = "SELECT * FROM USER WHERE username = %s"
    username = str(DataUser["username"])
    connection["cursor"].execute(sql, (username,))
    check = connection["cursor"].fetchone()
    if check is None:
        return None
    sql = "UPDATE USER SET username = %s, name = %s, password = %s WHERE username = %s"
    val = (DataUser["username"],DataUser["name"],DataUser["password"],DataUser["username"])
    connection["cursor"].execute(sql, val)
    connection["conn"].commit()
    sql = "SELECT * FROM USER WHERE username = %s"
    username = str(DataUser["username"])
    connection["cursor"].execute(sql, (username,))
    updateUser = connection["cursor"].fetchone()
    return FormHelper(updateUser)

# Delete Data User
async def DeleteUserData(username: str) -> dict:
    sql = "SELECT * FROM USER WHERE username = %s"
    connection["cursor"].execute(sql, (username,))
    dataUser = connection["cursor"].fetchone()
    if dataUser is None:
        return None
    sql = "DELETE FROM USER WHERE username = %s"
    connection["cursor"].execute(sql, (username,))
    connection["conn"].commit()
    return "Deleted"




