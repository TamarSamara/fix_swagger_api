import pytest
import logging
from api.user_api import UserApi
from models.user import User

my_user = User(10, "theUser1", "John1", "James1", "john1@email.com", "12345", "12345", 11)
my_user1 = User(11, "tamarSamara", "tamar", "samara", "tamar.samara@email.com", "12345", "12345", 12)
my_user_list = [
    {
        "id": 10,
        "username": "theUsereer",
        "firstName": "Johnw",
        "lastName": "Jamese",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    }
]


@pytest.mark.failed
def test_post_new_user():
    """
    Check to add an existing user
    failed
    """
    logging.info("add a new user to the store")
    getUser = UserApi().get_user_by_username(my_user.username)
    if getUser == 400 or getUser == 404:
        new_user = UserApi().post_new_user(my_user)
        logging.info("Successful Post user")
        assert new_user.id == my_user.id
    else:
        logging.warning("You are trying to add an existing user")
        assert False


@pytest.mark.passed
def test_post_new_list_of_users_without_login():
    """
    Check to post a list of users without logging in
    passed
    """
    logging.info("Creates a list of users with a given input array")
    user_list = UserApi().post_list_of_new_users(my_user_list.__str__())
    logging.info("There was an error processing your request. It has been logged (ID: 8230d60247b4cbee)")
    assert user_list == 500


@pytest.mark.passed
def test_get_user_login():
    """
    Verify that the user is logged into the system
    passed
    """
    logging.info("logging in user")
    getlogin = UserApi().get_user_login("username=tamarsamara&password=12345")
    if isinstance(getlogin, str):
        logging.warning(f"successful operation, {getlogin} ")
        assert True
    else:
        logging.warning(f'{getlogin} ')
        assert False


@pytest.mark.passed
def test_get_user_logout():
    """
    Verify that the user is logout into the system
    passed
    """
    logging.info("User logout from the system")
    get_logout = UserApi().get_user_logout()
    logging.info(f"successful operation, {get_logout}")
    assert get_logout.status_code == 200


@pytest.mark.passed
def test_get_user_by_username_exists():
    """
    get user by username exists
    passed
    """
    logging.info("get user by username exists")
    get_user = UserApi().get_user_by_username("theUser")
    assert get_user.status_code == 200


@pytest.mark.failed
def test_get_user_by_username_not_exists():
    """
    Verify get user by username not found
    failed
    """
    logging.info("get user by username not found")
    get_user = UserApi().get_user_by_username("tamarsamara")
    print(f'there was an error processing your request {get_user.status_code}')
    logging.warning(f"Error: response status is {get_user.status_code}")
    assert get_user.status_code == 200


@pytest.mark.failed
def test_put_user():
    """
    Check to update a non-existent user to the default state in the Store
    failed
    """
    get_user = UserApi().put_user("theUser")
    if not isinstance(get_user, int):
        assert get_user == my_user.id
    else:
        logging.warning(f"Error: response status is {get_user}")
        assert get_user == 200


@pytest.mark.passed
def test_delete_user():
    """
    finds user by name and deletes it
    passed
    """
    logging.info("the name that needs to be deleted")
    deleted_user = UserApi().delete_user("theUser")
    if isinstance(deleted_user, User):
        logging.warning("Error: response status is 502")
        assert False
    else:
        logging.warning(f"status code {deleted_user} from delete user which means success!")
        assert True
