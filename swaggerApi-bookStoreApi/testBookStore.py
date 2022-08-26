import logging
import pytest
from api.book_store_api import BookstoreApi
import requests
import json
from data import *
from models.book_store import BookStore
from testAccount import start as startAccount



@pytest.fixture(scope="session")
def start(pytestconfig):
    url = pytestconfig.getoption("url")
    res = requests.post(f'{url}Account/v1/GenerateToken', data=login)
    my_token = res.json()["token"]
    header = {'Authorization': f'Bearer {my_token}'}
    api = BookstoreApi(url, header)
    return api

@pytest.mark.passed
def test_get_bookstore(start):
    """
    Check if "get_bookstore" has returned all the books in the store
    passed 200
    """
    logging.info('Check if "get_books" has returned all the books in the store')
    res = start.get_bookstore()
    books = res.json()
    book_list = []
    for i in books['books']:
        b = BookStore(**i)
        book_list.append(b.to_json())
    for i in range(len(book_list)):
        # to check only title
        logging.info(f'Successfully get book')
        logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
        assert book_list[i].split(":")[2].split(",")[0][2:-1] == BOOK_TITLE_LIST[i]

    assert res.status_code == 200


@pytest.mark.failed
def test_put_bookstore_invalid_isbn(start):
    """
    Check "put_bookstore" with invalid ISBN
    failed 400
    """
    logging.info('Check "put_bookstore" with invalid ISBN')
    res = start.put_bookstore_by_isbn("97849325862", ISBN)
    logging.info(f'Successfully put book')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
    assert res.status_code == 200

@pytest.mark.failed
def test_put_bookstore_empty_isbn(start):
    """
    Check "put_bookstore" with invalid ISBN
    failed 400
    """
    logging.info('Check "put_bookstore" with invalid ISBN')
    res = start.put_bookstore_by_isbn("9781449325862", {})
    logging.info(f'Successfully put book')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}')
    assert res.status_code == 200


@pytest.mark.passed
def test_get_bookSore():
    """
    Check if you get books from the bookstore
    passed
    """
    logging.info("get book store")
    getBookStore = BookstoreApi().get_bookstore()
    print(f' staaaaaaaaattuuusss code {getBookStore.status_code}')
    logging.info("get bookstore")
    assert getBookStore.status_code == 200

@pytest.mark.passed
def test_post_bookstore():
    """
    Check to add an existing user
    passed
    """
    logging.info("add a new user to the store")

    postbook = BookApi().post_bookStore(data)
    logging.info("Successful Post Book")
    logging.warning(f'Error, status code is {postbook.status_code}')
    assert postbook.status_code == 200

#
