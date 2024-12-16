from app.repositories.userrepository import UserRepository
from app.schemas import UserBody, LoginBody
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import HTTPException
from app import secutity, config
from app.models import User

class AuthService:

    def authenticate_user(self, loginbody: LoginBody):
        user = UserRepository().get_email(loginbody.email)
        if not user:
            raise HTTPException(status_code=404)
        if not check_password_hash(user.password_hash, loginbody.password):
            raise HTTPException(status_code=401)
        return user

    def generate_token(self, user: User):
        return secutity.create_access_token(uid=str(user.id))
