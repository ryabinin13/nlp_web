from abc import ABC, abstractmethod
from app import SessionLocal

class BaseRepository(ABC):
    def __init__(self):
        self.db = SessionLocal()

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def get_id(self, id: int):
        pass

    @abstractmethod
    def get_email(self, email: str):
        pass

    @abstractmethod
    def getall(self):
        pass

    @abstractmethod
    def update(self, id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass