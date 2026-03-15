import requests
import pytest
import allure

# запуск в консоли 'pytest -v -s' - это с деталями и принтами (-s), если они есть внутри функций, а так они скипаются

@allure.feature('Pets')
@allure.story('Get pets')
@allure.title('Получаем данные по конкретному животному')
def test_get_one_pet(new_pet_id, hello):
        print('Testing get_one_pet()')
        with allure.step('Testing get_one_pet()'):
          response = requests.get(f'https://api.petstoreapi.com/v1/pets/{new_pet_id}')
        with allure.step('Check if name is Isabella'):
          assert response.json().get('name') == 'Isabella'
        with allure.step('Checking if size is small'):
          assert response.json().get('size') == 'SMALL'
        with allure.step('Checking if status code is 200'):
          assert response.status_code == 200

@allure.feature('Pets')
@allure.story('Get pets')
def test_get_all_pets():
        response = requests.get('https://api.petstoreapi.com/v1/pets').json()
        first_pet = response['data'][0]
        assert first_pet['name'] == 'PhotoPet'

@allure.feature('Pets')
@allure.story('Manipulate pets')
def test_post_a_pets():
        body = {
            "name": "Maxine",
            "species": "DOG",
            "breed": "Golden Retriever",
            "ageMonths": 24,
            "size": "LARGE",
            "color": "Golden",
            "gender": "FEMALE",
            "goodWithKids": True,
            "price": "2500.00",
            "currency": "USD",
            "status": "AVAILABLE",
            "description": "Friendly golden retriever looking for an active family",
            "medicalInfo": {
                "vaccinated": True,
                "spayedNeutered": True,
                "microchipped": True,
                "specialNeeds": False,
                "healthNotes": "Up to date on all vaccinations"
            }
        }
        headers = {'Authorization': 'Bearer {{bearerToken}}'}
        response = requests.post('https://api.petstoreapi.com/v1/pets', json = body, headers = headers).status_code
        assert response == 201


@pytest.mark.smoke()
@allure.feature('Example')
@allure.story('True')
def test_smth():
    assert True

@pytest.mark.parametrize('logins', ['', '   ', '#$%^&*'])
@allure.feature('Example')
@allure.story('True2')
def test_smth2(logins):
    assert True

@pytest.mark.parametrize('a, b', [(1, 2), (3, 0), (2, 1)])
@allure.feature('Example')
@allure.story('Sum=3')
def test_smth3(a, b):
    assert a + b == 3
    