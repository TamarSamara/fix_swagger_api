import logging
import pytest
from api.book_store_api import BookstoreApi
import requests
import json
from data import BOOK_TITLE_LIST, ISBN, POST_BOOK
from models.book_store import BookStore
from testAccount import start as startAccount

login = {"userName": "foo",
         "password": "tamdsar&ssD*DF123£"}
account_userID = "3d8e4618-50c4-492d-a26b-bdc2c6ba44c7"

data1 = {
    "userId": "9d99ecdd-458d-4431-a228-3f86a2946800",
    "collectionOfIsbns": [
        {
            "isbn": "9781449365035",
            "title": "Speaking JavaScript",
            "subTitle": "An In-Depth Guide for Programmers",
            "author": "Axel Rauschmayer",
            "publish_date": "2014-02-01T00:00:00.000Z",
            "publisher": "O'Reilly Media",
            "pages": 460,
            "description": "Like it or not, JavaScript is everywhere these days-from browser to server to mobile-and now you, too, need to learn the language or dive deeper than you have. This concise book guides you into and through JavaScript, written by a veteran programmer who o",
            "website": "http://speakingjs.com/"
        }
    ]
}


@pytest.fixture(scope="session")
def start(pytestconfig):
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    # return pytestconfig.getoption("url")
    url = pytestconfig.getoption("url")
    res = requests.post(f'{url}Account/v1/GenerateToken', data=login)
    my_token = res.json()["token"]
    header = {'Authorization': f'Bearer {my_token}'}
    # return header
    # acc_api = AccountApi(url, header)
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


# def test_put_bookstore_to_user(start, startAccount):
#     # LOGGER.info("test put book for user executing")
#
#
#     res = start.put_book_by_isbn(ISBN["isbn"], ISBN)
#     # LOGGER.info(res)
#     # assert code == 200
#     res = startAccount.get_user_by_id(ISBN['userId'])
#     # LOGGER.info(code, res)
#     # assert ISBN["isbn"] in [book.isbn for book in res.books]
#     for book in res.books

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

#
# def test_add_list_books(start, startAccount):
#     # LOGGER.info("test_add_books_list executing")
#     res = start.post_bookstore(POST_BOOK)
#     # assert res.status_code == 204
#     print(f'res statusss = {res.status_code}')
#     # LOGGER.info(f" res = {res.text}")
#     res = startAccount.get_user(account_userID)
#     # LOGGER.info(f" res = {res},")
#     # assert code == 200
#     # assert BOOK_LIST_TO_ADD['collectionOfIsbns']['isbn'] in res.books
#     print(f' resss = {res.status_code}')
#     # print(f'lisssttt {}')
#



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
#
# #
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
