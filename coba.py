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


# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

key = "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"

openai.api_key = key

def chat_with_gpt(prompt):
    response = openai.Completion.create()

    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text']
    else:
        return None

prompt = 'Halo, apa kabar?'
response = chat_with_gpt(prompt)
if response:
    print(response)


