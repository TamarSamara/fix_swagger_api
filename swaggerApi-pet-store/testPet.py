import json
import pytest
import logging
import requests
from api import pet_api
from models import Pet
from models.Pet import Status

url = "https://petstore3.swagger.io/api/v3"
header = {'accept': 'application/json'}
cat_category = {"id": 231, "name": "Cats"}
my_Cat = Pet.Pet(213, "my_cat", cat_category, "available")


def get_pet(pet_id: int) -> json:
    response = requests.get(f"{url}/pet/{pet_id}", headers=header)
    return response.json()


@pytest.mark.passed
def test_put_pet():
    """
    Check Find Pet by Status
    passed
    """
    logging.info("trying to find and update the pet")
    putpet = pet_api.PetApi().put_pet({'name': 'Small_cat'})
    assert putpet.name == "Small_cat"
    for pet in putpet:
        if pet.status != Status.available.name:
            logging.warning("Error: There is a case not available!")
            assert False
    logging.info(f'Successful update : {putpet.name}')
    assert True


@pytest.mark.failed
def test_post_new_pet():
    """
    Check to add an existing pet
    failed
    """
    logging.info("add a new pet to the store")
    if pet_api.PetApi().get_pet_by_id(my_Cat.id) == 404 or pet_api.PetApi().get_pet_by_id(my_Cat.id) == 400:
        new_pet = pet_api.PetApi().post_new_pet(my_Cat)
        logging.info("Successful Post pet")
        assert new_pet.id == my_Cat.id
    else:
        logging.warning("You are trying to add an existing pet")
        assert False


@pytest.mark.passed
def test_put_pet():
    """
    Check if the pet exists, then update the name from my_cat to Small_cat, check if the update worked
    passed
    """
    check_pet = pet_api.PetApi().get_pet_by_id(my_Cat.id)
    logging.info(f"Update an existing pet from {check_pet.name} to Small_Cat")
    print(f"Update an existing pet from {check_pet.name} to Small_Cat")
    if check_pet != 400 or check_pet != 404 or check_pet != 405:
        new_pet = pet_api.PetApi().put_pet({'name': 'Small_Cat'})
        print(f'Successful update : {check_pet.name}')
        logging.info(f'Successful update : {check_pet.name}')
        assert True

    else:
        logging.warning("You are trying to update a pet that does not exist")
        assert False


@pytest.mark.passed
def test_get_pet_by_tags():
    """
    Check Find a Pet by Tags (cat)
    passed
    """
    logging.info("trying to find pets with given tags")
    pet_list = pet_api.PetApi().get_pet_by_tags("tags=cat")
    for pet in pet_list:
        if pet.tags != "cat":
            logging.warning("tag cat does not exist in list tags=cat")
            assert False
    logging.info("successful operation")
    assert True


@pytest.mark.passed
def test_get_pet_by_id():
    """
    Check get a pet test by ID (7), then check the pet ID if it is not correct
    passed
    """
    logging.info("trying to find pets with given id")
    pet_with_id = pet_api.PetApi().get_pet_by_id(7)
    logging.info("Successful get pet by id")
    logging.warning("Didn't get me the correct ID")
    assert pet_with_id.id == 7


@pytest.mark.failed
def test_post_pet():
    """
    Check to update pet
    failed
    """
    logging.info("finding pet by id and updating name and status")
    updated_pet = pet_api.PetApi().post_update_pet("name=smallcat&status=available")
    assert updated_pet.name == "smallcat"


@pytest.mark.passed
def test_delete_pet():
    """
    Check Delete Pets by ID
    passed
    """
    logging.info("Check Delete Pets by ID")
    deleted_pet = pet_api.PetApi().delete_pet(346)
    print(f' deleteee pet : {deleted_pet}')
    print(f' type deleteee pet : {type(deleted_pet)}')
    if isinstance(deleted_pet, int):
        logging.warning(f"didn't find the deleted pet, good.")
        assert True

    else:
        logging.warning(f"couldn't delete pet for some reason")
        assert False


@pytest.mark.failed
def test_post_upload_image():
    """
    finds pet with id and uploads an image for it
    failed
    """
    pet = pet_api.PetApi().post_new_pet(my_Cat)
    logging.info("finding pet by id and uploads an image for it")
    pet_with_image = pet_api.PetApi().post_upload_image("additionalMetadata=string", pet.id, 'Small_Cat.jpg')
    logging.warning(f"Error: response status is: {pet_with_image}")
    assert pet_with_image.photourls == 'Small_Cat.jpg'
