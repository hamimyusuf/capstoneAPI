from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controlers.login_controler import(
    LoginUser
)

from models.response import (
    ResponseModel,
    ResponseLogin,
    ErrorResponseModel
)

from models.login_model import (
    UserLoginSchema
)

router = APIRouter()

@router.post("/",response_description="user login")
async def login_data_user(logUser: UserLoginSchema = Body(...)):
    logUser = jsonable_encoder(logUser)
    StatUser = await LoginUser(logUser)
    if StatUser == "Username or Password are invalid":
        return ResponseModel(StatUser, "Login Fail")
    return ResponseLogin(StatUser, "Success")