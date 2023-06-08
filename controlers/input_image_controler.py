from bson.objectid import ObjectId
from functions.connection import conn
import uuid
import mysql.connector
import requests


connection = conn()

def FormHelper(UserData,token) -> dict:
    return{
        "username": str(UserData[0]),
        "name": str(UserData[1]),
        "token":token,
    }


# Login User
async def diseasePredict(username, plant, img_url):
    ml_api_url = 'https://asia-southeast2-capstone-project-c23-pc640.cloudfunctions.net/function-1'
    payload = {
        'plant':plant,
        'image':img_url
        }
    result = requests.post(ml_api_url, json = payload)
    return result.text
    
       