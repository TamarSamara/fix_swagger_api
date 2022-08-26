from models.baseObj import BaseObj



class Account(BaseObj):
    def __init__(self, userId: str, username: str, books: [str]):
        self._userId = userId
        self._username = username
        self._books = books

    @property
    def userId(self) -> str:
        return self._userId

    @property
    def username(self) -> str:
        return self._username

    @property
    def books(self) -> [str]:
        return self._books
