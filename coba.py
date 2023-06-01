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

url = 'https://story-api.dicoding.dev/v1/register'
myobj = {'name':'hamim%20yusuf',
'email':'hamimyusuf@yahoo.com',
'password':'huhuhaha12345'}

x = requests.post(url, json = myobj)

print(x.text)

