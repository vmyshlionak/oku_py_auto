import pytest
import requests
import allure

@pytest.fixture()
def number():
    return 3

@allure.feature('Pets')
@allure.story('Manipulate pets')
def test_delete_pet_by_id(new_pet_id, hello):
    print('Testing deleting_one_pet()')
    headers = {'Authorization': 'Bearer {{bearerToken}}'}
    response = requests.delete(f'https://api.petstoreapi.com/v1/pets/{new_pet_id}', headers = headers)
    assert response.status_code == 204

@allure.feature('Example')
@allure.story('Print')
def test_number(number):
    print(number)