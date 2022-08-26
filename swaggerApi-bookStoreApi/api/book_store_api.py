import requests
from api.baseApi import BaseApi
from models.account import Account
from models.book_store import BookStore


class BookstoreApi(BaseApi):
    def __init__(self, url: str, header: dict):
        super().__init__(url, header)
        self._url = f"{self._base_url}BookStore/v1/"


    def get_bookstore(self) -> [list]:
        res = self.session.get(url=f"{self._url}Books")
        return res

    def post_bookstore(self, books: dict) -> requests.Response:
        res = self.session.post(url=f"{self._url}Books", data=books)
        return res

    def delete_bookstore(self, user_id: str) -> requests.Response:
        res = self.session.delete(url=f"{self._url}Books/?UserId={user_id}")
        return res

    def put_bookstore_by_isbn(self, isbn: str, data: dict):
        res = self.session.put(url=f"{self._url}Books/{isbn}", data=data)
        return res

    def delete_book(self, data: dict) -> requests.Response:
        res = self.session.delete(url=f"{self._url}Book", data=data)
        return res
