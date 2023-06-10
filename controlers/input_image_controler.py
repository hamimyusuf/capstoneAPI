from bson.objectid import ObjectId
from functions.connection import conn
from functions.generate_id import makeId
import mysql.connector
import requests


connection = conn()

def FormHelper(UserData,token) -> dict:
    return{
        "id_result": str(UserData[0]),
        "file": str(UserData[1]),
        "plant": str(UserData[1]),
        "result": str(UserData[1]),
        "deskripsi": str(UserData[1]),
        "penyebab": str(UserData[1]),
        "solusi": str(UserData[1]),
        "source": str(UserData[1]),
        "penulis": str(UserData[1])
    }


# Login User
async def diseasePredict(username, plant, img_url):
    ml_api_url = 'https://asia-southeast2-capstone-project-c23-pc640.cloudfunctions.net/function-1'
    payload = {
        'plant':plant,
        'image':img_url
        }
    result = requests.post(ml_api_url, json = payload)
    id_input = makeId()
    id_result = makeId()
    id_history = makeId()
    return result.text
    
       