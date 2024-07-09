from fastapi import FastAPI
from app.api import api_v1_router


app = FastAPI()
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello World"}
