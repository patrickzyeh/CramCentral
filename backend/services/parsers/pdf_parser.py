from io import BytesIO
from pypdf import PdfReader

from .file_parser import FileParser

class PdfParser(FileParser):
    
    async def parse_text(self) -> str:
        content = await self.file.read()
        reader = PdfReader(BytesIO(content))
        
        slideText = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                slideText.append(text)

        return " ".join(slideText)