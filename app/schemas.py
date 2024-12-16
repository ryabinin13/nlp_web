from pydantic import BaseModel
from datetime import date

class UserBody(BaseModel):
    username: str
    email: str
    birthday: date
    password1: str
    password2: str

class LoginBody(BaseModel):
    email: str
    password: str