from app.models import User, Message

class MassegeRepository:
    def __init__(self):
        super().__init__()

    def create(self, data: dict, user: User):
        message = Message(
            text = data['text'],
            user = user
        )
        self.db.add(message)
        self.db.commit()

        return message.id

    def get_id(self, id: int):
        return self.db.query(Message).where(Message.id == id).first()

    def getall(self):
        return self.db.query(Message).all()

    def update(self, id: int, data: dict):
        pass

    def delete(self, id: int):
        pass