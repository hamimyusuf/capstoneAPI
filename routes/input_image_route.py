from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from models.response import(
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()

@router.post("/",response_description="post image file")
async def uploadImage():
    return None