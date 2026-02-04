from abc import ABC, abstractmethod
from fastapi import UploadFile
class FileParser(ABC):
    def __init__(self, file: UploadFile):
        self.file = file
    @abstractmethod
    async def parse_text(self):
        pass
