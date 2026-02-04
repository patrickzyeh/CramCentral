from fastapi import APIRouter, UploadFile, File

from services.parsers.pdf_parser import PdfParser

# try implementing dependency inversion for the parsers
# store the accepted files somewhere perferably not in the code open closed
# split["."][-1] for extension
# check if extension and match appropriately

router = APIRouter()

@router.post("/", tags=["files"])
async def process_file(file: UploadFile = File(...)):
    parser = PdfParser(file)
    text = await parser.parse_text()
    return {"text": f"{text}"}