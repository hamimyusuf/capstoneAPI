from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controlers.information_controler import(
    showAllInfo,
    DataInfoByPlant
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

@router.post("/input",response_description="input data information")
async def input_data_information(RegUser: UserSchema = Body(...)):
    return ResponseModel(None, "API Not Found yet")

@router.get("/data",response_description="show all data information")
async def get_all_data_information():
    dataUser = await showAllInfo()
    return ResponseModel(dataUser, "Show All data")

@router.get("/data/{nama_tanaman}",response_description="show data information by plant name")
async def get_data_information(tanaman):
    dataInfo = await DataInfoByPlant(tanaman)
    if dataInfo:
        return ResponseModel(dataInfo, "Data User Show Successful")
    return ResponseModel(dataInfo, "Data Not found")

@router.put("/data/{id}",response_description="update data information")
async def update_data_information(UpdateUser: UserSchema = Body(...)):
    return ResponseModel(None, "API Not Found yet")

@router.delete("/data/{id}",response_description="delete data information")
async def delete_data_information(username):
    return ResponseModel(None, "API Not Found yet")