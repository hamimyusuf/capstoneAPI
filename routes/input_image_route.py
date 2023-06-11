from fastapi import APIRouter, Body, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
from functions.generate_id import makeId
import os
import fileinput
from utils.gcs_storage import GCStorage
from controlers.input_image_controler import diseasePredict 

from models.response import(
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()

@router.post("/",response_description="post image file")
async def uploadImage(username: str = Form(...), plant: str = Form(...), image : UploadFile=File(...)):
    unique_filename = makeId() + "-" + image.filename
    file_utils = f"utils/{unique_filename}"
    with open(file_utils, "wb") as file:
        contents = await image.read()
        file.write(contents)
    file_path = GCStorage().upload_file(file_utils)
    os.remove(file_utils)
    predict = await diseasePredict(username, plant, file_path)
    return ResponseModel(predict, "Menampilkan Hasil Analisis")