from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/", tags=["files"])
async def process_file(file: UploadFile = File(...)):
    return {"message": f"{file.filename}"}