from functions.connection import conn
from functions.generate_id import makeId
from functions.connection import conmongo
import requests
import datetime

#Variabel Pengaturan Tanggal
now = datetime.datetime.now() # Data tanggal hari ini
tgldibuat = now.strftime("%Y/%m/%d")

data_info = conmongo()
connection = conn()

def FormHelper(UserData,plant,img_url,id_result,result) -> dict:
    return{
        "id_result": str(id_result),
        "file": str(img_url),
        "plant": str(plant),
        "result": str(result),
        "deskripsi": str(UserData['deskripsi']),
        "penyebab": str(UserData['penyebab']),
        "solusi": UserData['solusi'],
        "source": str(UserData['source']),
        "penulis": str(UserData['penulis'])
    }


# Login User
async def diseasePredict(username, plant, img_url):
    ml_api_url = 'https://asia-southeast2-capstone-project-c23-pc640.cloudfunctions.net/function-1'
    payload = {
        'plant':plant,
        'image':img_url
        }
    result = requests.post(ml_api_url, json = payload)
    dataInfo = await data_info.find_one({"penyakit":str(result.text),"tanaman":plant})
    if dataInfo:
        id_info = dataInfo['_id']
    id_input = makeId()
    id_result = makeId()
    id_history = makeId()
    sql = "INSERT INTO INPUT (ID_INPUT, ID_HISTORY, FILENAME) VALUES (%s, %s, %s)"
    val = (id_input,id_history,img_url)
    connection["cursor"].execute(sql, val)
    connection["conn"].commit()

    sql = "INSERT INTO RESULT (ID_RESULT, ID_HISTORY, ID_INFO) VALUES (%s, %s, %s)"
    val = (id_result,id_history,str(id_info))
    connection["cursor"].execute(sql, val)
    connection["conn"].commit()
    sql = "INSERT INTO HISTORY (ID_HISTORY, USERNAME, ID_INPUT, ID_RESULT, DATE) VALUES (%s, %s, %s, %s, %s)"
    val = (id_history,username,id_input, id_result, tgldibuat)
    connection["cursor"].execute(sql, val)
    connection["conn"].commit()

    return FormHelper(dataInfo, plant, img_url, id_result, result.text)
    
       