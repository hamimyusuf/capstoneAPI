from bson.objectid import ObjectId
from functions.connection import conn
from functions.generate_id import makeId
from functions.connection import conmongo
import mysql.connector

connection = conn()
data_info = conmongo()

def FormHelper(HistoryData,info) -> dict:
    return{
        "ID": str(HistoryData[0]),
        "date": str(HistoryData[2]),
        "image":str(HistoryData[1]) ,
        "tanaman":str(info['tanaman']),
        "penyakit":str(info['penyakit']),
        "deskripsi": str(info['deskripsi']),
        "penyebab": str(info['penyebab']),
        "solusi": info['solusi'],
        "source": str(info['source']),
        "penulis": str(info['penulis'])
    }

async def showDataHistory(username: str) -> dict:
    sql = "SELECT HISTORY.ID_HISTORY,FILENAME,HISTORY.DATE, RESULT.ID_INFO FROM HISTORY JOIN INPUT ON HISTORY.ID_INPUT = INPUT.ID_INPUT JOIN RESULT ON HISTORY.ID_RESULT = RESULT.ID_RESULT WHERE HISTORY.USERNAME = %s;"
    connection["cursor"].execute(sql, (username,))
    check = connection["cursor"].fetchall()
    if check:
        data = []
        for temp in check:
            id_info = ObjectId(temp[3])
            print(id_info)
            dataInfo = await data_info.find_one({"_id":id_info})
            print(dataInfo)
            data.append(FormHelper(temp,dataInfo))
        # id_info = data[0][]
        print(data)
        return data
    return None