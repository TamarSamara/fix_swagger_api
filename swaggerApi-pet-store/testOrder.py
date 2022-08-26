import pytest
import logging
from api import pet_api
from api import order_api
from api.user_api import UserApi
from models.user import User
from models import Pet
from models.order import Order, Status

files = 'doggy.jpg'
url = "https://petstore3.swagger.io/api/v3"
header = {'accept': 'application/json'}
dog_category = {"id": 1, "name": "Dogs"}
my_dog = Pet.Pet(11110, "my_dog", dog_category, "available")
my_user = User(10, "Me", "Noam", "Barkai", "barkai@email.com", "12345", "12345", 2)
my_user1 = User(11, "you", "Mishel", "Barkai", "barkai23@email.com", "12332", "12344", 3)
my_user_list = [{"id": 12,
                 "username": "User",
                 "firstName": "John",
                 "lastName": "James",
                 "email": "john@email.com",
                 "password": "12345",
                 "phone": "12345",
                 "userStatus": 1}]
my_order = Order(10, 198772, 7, "2022-08-06T23:31:28.815+00:00", Status.approved, False)
apiP = pet_api.PetApi()
apiO = order_api.OrderApi()
apiU = UserApi()


@pytest.mark.passed
def test_get_store_inventory():
    """
    Check if it returns the map of status codes to quantities
    passed
    """
    # in constant change ****** -> failed
    logging.info("get store inventory")
    getinventory = order_api.OrderApi().get_inventory()
    print(f'\"sold": {getinventory.sold}')
    dictinventory = {"sold": getinventory.sold, "approved": getinventory.approved, "placed": getinventory.placed,
                     "delivered": getinventory.delivered}
    print(dictinventory)
    assert getinventory.sold == 742006
    logging.warning("\"Sold\" is not correct")
    assert getinventory.approved == 69
    logging.warning("\"approved\" is not correct")
    assert getinventory.placed == 100
    logging.warning("\"placed\" is not correct")
    assert getinventory.delivered == 50  #
    logging.warning("\"delivered\" is not correct")
    logging.info(f"successful operation: {dictinventory}")


@pytest.mark.passed
def test_post_order():
    """
    Post a new order for a pet
    passed
    """
    logging.info("place a new order in the store")
    postorder = order_api.OrderApi().post_new_order(my_order)
    logging.info(f"successful operation {postorder}")
    assert postorder.petId == my_order.petId


@pytest.mark.passed
def test_get_order_by_id():
    """
    check get order by id
    passed
    """
    logging.info("ID of order that needs to be fetched")
    response = order_api.OrderApi().get_order_by_id(10)
    assert response.id == 10


@pytest.mark.failed
def test_delete_order():
    """
    Verify that the order has not been deleted by order ID not found
    failed
    """
    logging.info("delete store order by order id ")
    logging.info("For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.")
    deleted_order = order_api.OrderApi().delete_order_by_id(0)
    if deleted_order == 200:
        logging.info(f"successful operation {deleted_order}")
        assert True
    else:
        logging.warning("Order not found")
        assert False
