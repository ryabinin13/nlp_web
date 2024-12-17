from app.models import User
from app import SessionLocal

class UserRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create(self, data: dict):
        user = User(
            username=data['username'], 
            email=data['email'], 
            password_hash=data['password_hash'], 
            birthday=data['birthday']
        )

        self.db.add(user)
        self.db.commit()
        return user.id

    def get_id(self, id: int):
        return self.db.query(User).where(User.id == id).first()

    def get_email(self, email):
        return self.db.query(User).where(User.email == email).first()

    def getall(self):
        return self.db.query(User).all()

    def update(self, id: int, data: dict):
        user = self.db.query(User).where(User.id == id).first()

        user.username=data['username'], 
        user.email=data['email'], 
        user.password_hash=data['password_hash'], 
        user.birthday=data['birthday']

        self.db.commit()

    def delete(self, id: int):
        user = self.db.query(User).where(User.id == id).first()
        self.db.delete(user)
        self.db.commit()