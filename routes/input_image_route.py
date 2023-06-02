from fastapi import APIRouter, Body, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import fileinput
from utils.gcs_storage import GCStorage

from models.response import(
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()

@router.post("/",response_description="post image file")
async def uploadImage(username: str = Form(...), image : UploadFile=File(...)):
    file_path = GCStorage().upload_file(image)
    return{
        "upload file":file_path
    }