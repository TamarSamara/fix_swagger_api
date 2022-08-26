import logging
import pytest
from api.book_store_api import BookstoreApi
import requests
from data import *
from models.book_store import BookStore


@pytest.fixture(scope="session")
def start(pytestconfig):
    url = pytestconfig.getoption("url")
    res = requests.post(f'{url}Account/v1/GenerateToken', data=login)
    my_token = res.json()["token"]
    header = {'Authorization': f'Bearer {my_token}'}
    api = BookstoreApi(url, header)
    return api


@pytest.mark.passed
def test_get_books(start):
    """
    Check if "get_bookstore" has returned all the books in the store
    passed 200
    """
    logging.info('Check if "get_books" has returned all the books in the store')
    res = start.get_bookstore()
    assert res.status_code == 200
    books = res.json()
    book_list = []
    for i in books['books']:
        b = BookStore(**i)
        book_list.append(b.to_json())
    for i in range(len(book_list)):
        # to check only title
        logging.info(f'Successfully get books, status code is: {res.status_code}')
        logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
        assert book_list[i].split(":")[2].split(",")[0][2:-1] == BOOK_TITLE_LIST[i]


@pytest.mark.passed
def test_get_book_by_userID(start):
    """
    Check if you get a book by user id
    passed 200
    """
    logging.info('Check if you get a book by user id')
    res = start.get_book_by_ID(ISBN)
    logging.info(f'Successfully get book by user id, status code is: {res.status_code}')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
    assert res.status_code == 200
    assert res.json()["isbn"] == ISBN


@pytest.mark.passed
def test_add_list_books(start):
    """
    Check if add list of books
    passed 200
    """
    logging.info('Check if add list of books')
    res = start.post_add_list_of_books(ListOfBooks)
    logging.info(f'Successfully add list of books, status code is: {res.status_code}')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
    assert res.status_code == 200
    assert res.reason == "OK"


@pytest.mark.passed
def test_delete_books_to_user(start):
    """
    Verify deleting books by user ID
    passed 200
    """
    logging.info('deleting books by user ID')
    res = start.delete_books(userID)
    logging.info(f'Books have been successfully deleted by user ID, status code is: {res.status_code}')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
    assert res.status_code == 200
    assert res.reason == "OK"
    assert userID not in res.text


@pytest.mark.passed
def test_delete_book_by_string_object(start):
    """
    Verify deleting book by string Object
    passed 200 -> 401 not Unauthorized :(
    """
    logging.info('deleting book by string Object ')
    res = start.delete_book(DELACCOUNT)
    logging.info(f'Books have been successfully deleted by string Object, status code is: {res.status_code}')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
    assert res.status_code == 200
    assert res.reason == "OK"


def test_put_book(start):
    """
    Check if the book is "put" by isbn
    """
    logging.info('Check if the book is "put" by isbn')
    res = start.put_bookstore_by_isbn(ISBN2, PUT_USER)
    logging.info(f'Books have been successfully putted by isbn, status code is: {res.status_code}')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
    assert res.status_code == 200
    assert res.reason == "OK"
