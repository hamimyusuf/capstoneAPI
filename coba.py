# import mysql.connector


# mydb = mysql.connector.connect(
# host="localhost",
# port=3308,
# user="root",
# password="123",
# database="capstone_db"
# )
# cursor = mydb.cursor()

# # sql = "INSERT INTO USER (username, name, password) VALUES (%s, %s, %s)"
# # val = ("hamim1","hamimyusuf","hamim123")
# # cursor.execute(sql, val)
# # mydb.commit()

# sql = "SELECT * FROM USER"
# # username = "ThoriqLigarHaidar"
# check = cursor.execute(sql)
# print(check)
# newUser = cursor.fetchall()
# print(newUser)
# data = []
# async for temp in newUser:
#     data.append(temp)
# print(data)

import requests
from functions.connection import mongoconn
# data_info = conmongo()
infodb = mongoconn()

# ml_api_url = 'https://asia-southeast2-capstone-project-c23-pc640.cloudfunctions.net/function-1'
# payload = {
#     'plant':'chili',
#     'image':'https://storage.googleapis.com/c23_pc640_bucket/c23/brownspot.jpg'
#     }
# result = requests.post(ml_api_url, json = payload)
# print(result.text)
cari = infodb.find_one({"penyakit":"leaf_curl","tanaman":"chili"})
print(cari)
# from functions.generate_id import makeId

# id_input = makeId()
# id_result = makeId()
# id_history = makeId()

# print(id_input,id_history,id_result)