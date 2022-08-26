import logging
import pytest
from api.book_store_api import BookApi
from api.account_api import AccountApi
from models.account import Account
import requests

login = {"userName": "foo",
         "password": "tamdsar&ssD*DF123£"}
account_tam_auth = {
  "userName": "tamarauth",
  "password": "TamAr1ddd23$%^"
}
usedID_tamauth = "dfc0c7f2-7554-4c66-b300-f2d5e855586c"
accountAuth = {
    "userName": "tamar",
    "password": "SamA@213**&"
}
empty_account = {
    "userName": "",
    "password": ""
}
selaUserId = '6fc01df9-88a3-4153-9a7e-70d519afb6e0'
account_auth = {
    "userName": "tamaaaasrsam",
    "password": "SamA@213**&"
}
# {"userName": "tamar", "pass": "12345"}
wrong_password = ('{"code":"1300","message":"Passwords must have at least one non alphanumeric '
                  "character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase "
                  "('a'-'z'), one special character and Password must be eight characters or "
                  'longer."}')
account_not_auth = {
    "userName": "tamarsamara",
    "password": "SamA@213**&"
}
account_userID = "3d8e4618-50c4-492d-a26b-bdc2c6ba44c7"
new_account = {
    "userName": "tamar",
    "password": "12*aA$s@a345"
}
BOOK_LIST_TO_ADD = {
    "userId": selaUserId,
    "collectionOfIsbns": [
        {
            "isbn": "9781491904244"
        }
    ]
}
BOOKS_DELETE = {
    "isbn": "9781491904244",
    "userId": selaUserId
}


@pytest.fixture(scope="session")
def start(pytestconfig):
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    url = pytestconfig.getoption("url")
    res = requests.post(f'{url}Account/v1/GenerateToken', data=login)
    my_token = res.json()["token"]
    header = {'Authorization': f'Bearer {my_token}'}
    # return header
    acc_api = AccountApi(url, header)
    return acc_api


@pytest.mark.passed
def test_post_valid_account_authorized(start):
    """
    Verify a valid authorized account, if authorized
    passed
    """
    logging.info('Verify a valid authorized account, if authorized')
    res = start.post_login_authorized(login)
    logging.info('The account has been successfully authorized')
    logging.warning(f' Error, account {res.reason}, status code : {res.status_code}')
    assert res.reason == 'OK'
    assert res.status_code == 200



@pytest.mark.failed
def test_post_account_not_authorized(start):
    """
    Check invalid account, if authorized
    failed 404
    """
    logging.info('Check invalid account, if authorized')
    res = start.post_login_authorized(account_not_auth)
    logging.info('The account has been successfully authorized')
    logging.warning(f' Error, account {res.reason}, status code : {res.status_code}')

    assert res.reason == 'OK'
    assert res.status_code == 200



@pytest.mark.failed
def test_post_account_exists(start):
    """
    Check if an existing account is already posted
    failed 406
    """
    logging.info('Check if an existing account is already posted')
    res = start.post_account_user(account_auth)
    logging.info('Successfully posted an account')
    logging.warning(f'Error: Not Acceptable, {res.text[26:-2]}, status code : {res.status_code}')
    assert res.status_code == 201
    assert res.text.split(":")[-1][1:-2] != 'User exists!'



@pytest.mark.passed
def test_post_account_user_valid_account(start):
    """
    Check if posting a valid account
    passed 201
    """
    logging.info('posting an account with the wrong password (numbers only)')
    res = start.post_account_user(new_account)
    logging.info('Successfully posted an account')
    logging.warning(f'{res.reason}, status code: {res.status_code}, {res.text.split(":")[-1][1:-2]}')
    assert res.reason == 'Created'
    assert res.status_code == 201

@pytest.mark.failed
def post_account_wrong_password(start, account):
    """
    Check if posting an account with the wrong password (numbers only)
    failed 400
    """
    logging.info('posting an account with the wrong password (numbers only)')
    res = start.post_account_user(account)
    logging.info('Successfully posted an account')
    logging.warning(f'{res.reason}, status code: {res.status_code}, {res.text}')
    print(f'{res.reason},  status code: {res.status_code}, {res.text}')
    assert res.text == wrong_password

@pytest.mark.failed
def test_post_account_wrong_password_numbers(start):
    """
    Check if posting an account with the wrong password (numbers only)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "12345"})

@pytest.mark.failed
def test_post_account_wrong_password_uppercase(start):
    """
    Check if posting an account with the wrong password (uppercase only)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "TAMAR"})

@pytest.mark.failed
def test_post_account_wrong_password_lowercase(start):
    """
    Check if posting an account with the wrong password (lowercase only)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "tamar"})

@pytest.mark.failed
def test_post_account_wrong_password_special_character(start):
    """
    Check if posting an account with the wrong password (special character only)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "$$***"})

@pytest.mark.failed
def test_post_account_wrong_password_less_eight(start):
    """
    Check if posting an account with the wrong password (Password is less than eight)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "1tA$"})

@pytest.mark.failed
def test_post_account_wrong_password_numbers_uppercase(start):
    """
    Check if posting an account with the wrong password (numbers and uppercase only)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "123TAMAR456"})

@pytest.mark.failed
def test_post_account_wrong_password_numbers_lowercase(start):
    """
    Check if posting an account with the wrong password (numbers and lowercase only)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "123tamar456"})

@pytest.mark.failed
def test_post_account_wrong_password_numbers_special_character(start):
    """
    Check if posting an account with the wrong password (numbers and special_character only)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "123@#$*456"})

@pytest.mark.failed
def test_post_account_wrong_password_uppercase_lowercase(start):
    """
    Check if posting an account with the wrong password (Only uppercase and lowercase letters)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "tAmArsAmArA"})

@pytest.mark.failed
def test_post_account_wrong_password_uppercase_special_character(start):
    """
    Check if posting an account with the wrong password (Only uppercase and special_character)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "TAMAR$#*&@$"})

@pytest.mark.failed
def test_post_account_wrong_password_lowercase_special_character(start):
    """
    Check if posting an account with the wrong password (Only lowercase and special_character)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "tamar$#*&@$"})

@pytest.mark.failed
def test_post_account_wrong_password_lowercase_uppercase_numbers(start):
    """
    Check if posting an account with the wrong password (Only uppercase and lowercase letters, and numbers)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "tAmAr1234567"})

@pytest.mark.failed
def test_post_account_wrong_password_lowercase_uppercase_special_character(start):
    """
    Check if posting an account with the wrong password (Only uppercase and lowercase letters, and special_character)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "tAmAr@$&*$"})

@pytest.mark.failed
def test_post_account_wrong_password_numbers_lowercase_special_character(start):
    """
    Check if posting an account with the wrong password (Only lowercase, numbers and special_character)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "tamar123@$&*$"})

@pytest.mark.failed
def test_post_account_wrong_password_numbers_uppercase_special_character(start):
    """
    Check if posting an account with the wrong password (Only uppercase, numbers and special_character)
    failed 400
    """
    post_account_wrong_password(start, {"userName": "tamar", "password": "TAMAR123@$&*$"})

@pytest.mark.failed
def test_post_account_empty_password(start):
    """
    Check if posting an account with an empty password
    failed 400
    """
    logging.info('posting an account with an empty password')
    res = start.post_account_user({"userName": "tamar", "password": ""})
    logging.info(f'Successfully posted a new account, status code: {res.status_code}')
    logging.warning(f'{res.reason}, status code: {res.status_code}, {res.text.split(":")[-1][1:-2]}')
    assert res.text.split(":")[-1][1:-2] != 'UserName and Password required.'
    assert res.status_code == 200

@pytest.mark.failed
def test_post_account_empty_username_and_password(start):
    """
    Check if posting an account with an empty username and password
    failed 400
    """
    logging.info('posting an account with an empty username and password')
    res = start.post_account_user({"userName": "", "password": ""})
    logging.info(f'Successfully posted a new account, status code: {res.status_code}')
    logging.warning(f'{res.reason}, status code: {res.status_code}, {res.text.split(":")[-1][1:-2]}')
    assert res.text.split(":")[-1][1:-2] != 'UserName and Password required.'
    assert res.status_code == 201


@pytest.mark.passed
def test_post_login_account_generate_token(start):
    """
    tries to get an authorized token for said account
    passed 200
    """
    logging.info("trying to get a token")
    res = start.post_login_account_generate_token(accountAuth)
    logging.info(f'Successfully posted a new account, status code: {res.status_code}')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}, {res.text.split(":")[-1][1:-2]}')
    assert res.status_code == 200
    assert res.reason == 'OK'
    assert res.text.split(":")[-1][1:-2] == 'User authorized successfully.'


@pytest.mark.failed
def test_post_login_account_generate_token_with_empty_username_and_password(start):
    """
    check post login account generate token with empty username and password
    failed 400
    """
    api = start
    logging.info("send an empty password and empty username")
    res = api.post_login_account_generate_token(empty_account)
    logging.info(f'Successfully posted a new account, status code: {res.status_code}')
    logging.warning(f'Error: {res.reason}, status code is: {res.status_code}, {res.text.split(":")[-1][1:-2]}')
    assert res.text.split(":")[-1][1:-2] != "UserName and Password required."
    assert res.status_code == 200



@pytest.mark.passed
def test_get_account(start):

    res = start.get_user(usedID_tamauth)

    assert res.status_code == 200

@pytest.mark.passed
def test_delete_user_non_existent(start):
    """
    Check to delete a non-existent account
    passed
    """
    logging.info("trying to delete a user with a 30 character userID")
    res = start.delete_user2("80bc26d5-01ac-471d-9346-779b86b60b9b")
    logging.info(f'Successfully delete a user account, status code is {res.status_code}')
    logging.warning(f'Error, unsuccessful user account deletion, status code is {res.status_code}')
    assert response.status_code != 200

