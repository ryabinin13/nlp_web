from app.repositories.userrepository import UserRepository
from app.schemas import UserBody, LoginBody
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import HTTPException
from app import secutity, config

class RegistrationService:

    def registration(self, data: UserBody):
        if not data.password1 == data.password2:
            raise HTTPException(status_code=400)

        password_hash = generate_password_hash(data.password1)
        data_dict = data.model_dump(exclude={"password1", "password2"})
        data_dict["password_hash"] = password_hash

        return UserRepository().create(data_dict)