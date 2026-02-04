from fastapi import UploadFile, File
import os

from .file_parser import FileParser
from .pdf_parser import PdfParser
from .pptx_parser import PptxParser

ACCEPTED_FILES = {
    ".pdf": PdfParser,
    ".pptx": PptxParser
} 

def get_parser(file: UploadFile = File(...)) -> FileParser:
    _, ext = os.path.splitext(file.filename)
    ext = ext.lower()
    
    parser_class = ACCEPTED_FILES.get(ext)
    if not parser_class:
        return None
    return parser_class(file)