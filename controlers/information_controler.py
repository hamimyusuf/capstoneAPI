from bson.objectid import ObjectId
from functions.connection import conmongo

data_info = conmongo()

def FormHelper(UserData) -> dict:
    return{
        "id": str(UserData['_id']),
        "tanaman": str(UserData['tanaman']),
        "penyakit":str(UserData['penyakit']),
        "deskripsi": str(UserData['deskripsi']),
        "penyebab": str(UserData['penyebab']),
        "solusi": str(UserData['solusi']),
        "source": str(UserData['source']),
        "penulis": str(UserData['penulis'])
    }


# show all info data
async def showAllInfo():
    allData = []
    async for info in data_info.find():
        allData.append(FormHelper(info))
    return allData

# show data info by plant
async def DataInfoByPlant(plant: str) -> dict:
    allData = []
    async for info in data_info.find({"tanaman": str(plant)}):
        allData.append(FormHelper(info))
    return allData

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
       