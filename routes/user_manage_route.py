from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controlers.register_controler import(
    addUser
)
from controlers.user_manage_controler import(
    showAllUsers,
    DataUserByUsername,
    UpdateUserData,
    DeleteUserData
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

@router.post("/user",response_description="register user in database")
async def register_data_user(RegUser: UserSchema = Body(...)):
    RegUser = jsonable_encoder(RegUser)
    NewUser = await addUser(RegUser)
    if NewUser == "Username Has Already Use":
        return  ResponseNotModified(NewUser, "Try Another Username")
    return ResponseModel(NewUser, "User Successfuly Added")

@router.get("/user",response_description="show all data user")
async def get_all_data_user():
    dataUser = await showAllUsers()
    return ResponseModel(dataUser, "Show All data")

@router.get("/user/{username}",response_description="show data user by username")
async def get_data_user(username):
    dataUser = await DataUserByUsername(username)
    if dataUser:
        return ResponseModel(dataUser, "Data User Show Successful")
    return ResponseModel(dataUser, "Data Not found")

@router.put("/user/{username}",response_description="update data user")
async def update_data_user(UpdateUser: UserSchema = Body(...)):
    UpdateUser = jsonable_encoder(UpdateUser)
    Updated = await UpdateUserData(UpdateUser)
    if Updated:
        return ResponseModel(Updated, "Data Update Successfully")
    return ResponseModel(Updated, "Data Not Found")

@router.delete("/user/{username}",response_description="delete data user")
async def delete_data_user(username):
    deleteUser = await DeleteUserData(username)
    if deleteUser:
        return ResponseModel(deleteUser, "Data User Successfully Deleted")
    return ResponseModel(None, "Data Not Found")