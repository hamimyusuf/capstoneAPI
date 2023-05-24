from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controlers.register_controler import(
    addUser
)

from models.response import (
    ResponseModel,
    ResponseNotModified,
    ErrorResponseModel
)

from models.register_model import (
    UserSchema
)

router = APIRouter()

@router.post("/",response_description="register user in database")
async def register_data_user(RegUser: UserSchema = Body(...)):
    RegUser = jsonable_encoder(RegUser)
    NewUser = await addUser(RegUser)
    if NewUser == "Username Has Already Use":
        return  ResponseNotModified(NewUser, "Try Another Username")
    return ResponseModel(NewUser, "User Successfuly Added")