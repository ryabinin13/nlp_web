from app.repositories.userrepository import UserRepository
from app.schemas import UserBody, LoginBody
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import HTTPException
from app import secutity, config

class UserService:

    def get_user_email(self, email: str):
        return UserRepository().get_email(email)
        