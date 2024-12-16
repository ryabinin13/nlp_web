from fastapi import APIRouter, Depends
from app.services.userservice import UserService
from app.schemas import UserBody
from app import secutity


user_router = APIRouter()

@user_router.get("/protected", dependencies=[Depends(secutity.access_token_required)])
def protected():
    return {"data": "secret"}