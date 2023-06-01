from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from models.response import(
    ErrorResponseModel,
    ResponseModel
)

from controlers.history_controler import(
    showDataHistory
)

router = APIRouter()

@router.get("/",response_description="post image file")
async def getDataHistory(username):
    dataHistory = await showDataHistory(username)
    if dataHistory:
        return ResponseModel(dataHistory, "Data History Show Successfull")
    return ResponseModel(dataHistory, "Data Not Found")