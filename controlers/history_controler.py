from bson.objectid import ObjectId
from functions.connection import conn
from functions.generate_id import makeId
import mysql.connector

connection = conn()

def FormHelper(HistoryData) -> dict:
    return{
        "ID": str(HistoryData[0]),
        "date": str(HistoryData[1]),
        "image": str(HistoryData[2]),
        "tanaman": str(HistoryData[3]),
        "penyakit": str(HistoryData[4]),
        "deskripsi": str(HistoryData[5]),
        "solusi": str(HistoryData[6])
    }

async def showDataHistory(username: str) -> dict:
    sql = "SELECT HISTORY.ID_HISTORY,FILENAME,HISTORY.DATE,TANAMAN,PENYAKIT,DESKRIPSI,SOLUSI FROM HISTORY JOIN INPUT ON HISTORY.ID_INPUT = INPUT.ID_INPUT JOIN RESULT ON HISTORY.ID_RESULT = RESULT.ID_RESULT JOIN INFORMATION ON RESULT.ID_INFO = INFORMATION.ID_INFO WHERE HISTORY.USERNAME = %s;"
    connection["cursor"].execute(sql, (username,))
    check = connection["cursor"].fetchall()
    if check:
        data = []
        for temp in check:
            data.append(FormHelper(temp))
        return data
    return None