from fastapi import FastAPI
from api.v1.endpoints import endpoint1

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World3"}

app.include_router(endpoint1.router, prefix="/api/v1")