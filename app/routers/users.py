from fastapi import APIRouter, Depends, Response
from app.services.userservice import UserService
from app import secutity, config

user_router = APIRouter()

@user_router.post("/logout", dependencies=[Depends(secutity.access_token_required)])
def logout(response: Response):
    response.delete_cookie(config.JWT_ACCESS_COOKIE_NAME)
    return {"message": "Successfully logged out"}
