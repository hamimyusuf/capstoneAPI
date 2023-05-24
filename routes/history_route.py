from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from models.response import(
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()

@router.get("/",response_description="post image file")
async def getDataHistory():
    return None