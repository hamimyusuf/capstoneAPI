from starlette import status
from starlette.responses import JSONResponse

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ResponseNotModified(data, message):
    return{
        "data": [data],
        "code": 304,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}