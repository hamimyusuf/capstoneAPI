from starlette import status
from starlette.responses import JSONResponse

def ResponseModel(data, message):
    return {
        "message": message,
        "code": 200,
        "data": [data],
    }

def ResponseLogin(data, message):
    return {
    "code":200,
    "message": message,
    "loginResult": data,
}

def ResponseNotModified(data, message):
    return{
        "data": [data],
        "code": 304,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}