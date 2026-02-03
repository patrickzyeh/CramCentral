from abc import ABC, abstractmethod
from fastapi import UploadFile

class FileParser(ABC):
    @abstractmethod
    def parseText(self, file: UploadFile):
        pass
