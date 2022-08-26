import requests
from api.baseApi import BaseApi


class BookstoreApi(BaseApi):
    def __init__(self, url: str, header: dict):
        super().__init__(url, header)
        self._url = f"{self._base_url}BookStore/v1/"

    def get_bookstore(self) -> [list]:
        res = self.session.get(url=f"{self._url}Books")
        return res

    def post_add_list_of_books(self, books: dict) -> requests.Response:
        res = self.session.post(url=f"{self._url}s", data=books, headers=self._headers)
        return res

    def delete_books(self, user_id: str) -> requests.Response:
        res = self.session.delete(url=f"{self._url}", data=user_id, headers=self._headers)
        return res

    def delete_book(self, data: dict) -> requests.Response:
        res = self.session.delete(url=f"{self._url}Book", data=data)
        return res

    def put_bookstore_by_isbn(self, isbn: str, data: dict):
        res = self.session.put(url=f"{self._url}s/{isbn}", data=data, headers=self._headers)
        return res

    def get_book_by_ID(self, isbn: str):
        res = self.session.get(url=f"{self._url}Book?ISBN={isbn}")
        return res
