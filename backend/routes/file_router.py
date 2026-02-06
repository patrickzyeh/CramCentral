from fastapi import APIRouter, UploadFile, HTTPException, File, Depends
from typing import Annotated

from services.parsers.parser_factory import get_parser
from services.parsers.file_parser import FileParser
from services.card_generator_service import generate_flash_cards


router = APIRouter()

@router.post("/", tags=["files"])
async def process_file(parser: Annotated[FileParser, Depends(get_parser)], file: UploadFile = File(...)):
    if not parser:
        raise HTTPException(status_code=415, detail="Unsupported file type. Only PDF and PPTX are allowed.")

    text = await parser.parse_text()
    card_json = await generate_flash_cards(text)
    return card_json