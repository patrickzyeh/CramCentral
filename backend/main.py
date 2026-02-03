from fastapi import FastAPI

from routes.file_router import router as file_router 

app = FastAPI()

app.include_router(file_router, prefix="/files")

@app.get("/")
def read_root():
    return {"Hello": "World"}


