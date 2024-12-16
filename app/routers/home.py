from fastapi import APIRouter, HTTPException, Response
from app.services.userservice import UserService
from app.services.regservice import RegistrationService
from app.services.authservice import AuthService
from app.schemas import UserBody, LoginBody
from typing import Annotated
from fastapi import Depends
from werkzeug.security import generate_password_hash, check_password_hash
from app import secutity, config

home_router = APIRouter()

@home_router.post("/registration")
def registration(userbody: UserBody):
    return RegistrationService().registration(userbody)

@home_router.post("/login")
def login(loginbody: LoginBody, response: Response):
    user = AuthService().authenticate_user(loginbody)
    token = AuthService().generate_token(user)
    response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
    return {"access_token": token}
    

# @home_router.post("/login")
# def login(loginbody: LoginBody, response: Response):
#     user = UserService().get_user_email(loginbody.email)
#     if user:
#         if check_password_hash(user.password_hash, loginbody.password):
#             token = secutity.create_access_token(uid=str(user.id))
#             response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
#             return {"access_token": token}
#         raise HTTPException(status_code=401)
    
@home_router.post("/logout")
def logout(response: Response):
    response.delete_cookie(config.JWT_ACCESS_COOKIE_NAME)
    return {"message": "Successfully logged out"}


