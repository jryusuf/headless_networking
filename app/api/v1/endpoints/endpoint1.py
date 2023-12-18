from fastapi import APIRouter

router = APIRouter()

@router.get("/endpoint1")
def read_endpoint1():
    return {"message": "data from endpoint1"}