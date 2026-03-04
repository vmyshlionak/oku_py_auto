import requests
import pytest

# запуск в консоли 'pytest -v -s' - это с деталями и принтами (-s), если они есть внутри функций, а так они скипаются

@pytest.fixture()
def new_pet_id():
    body = {
        "name": "Isabella",
        "species": "DOG",
        "breed": "Chihuahua",
        "ageMonths": 18,
        "size": "SMALL",
        "color": "Golden",
        "goodWithKids": False,
        "price": "5000.00",
        "currency": "USD",
        "status": "AVAILABLE",
        "description": "Pure evil is looking for its victims",
        "medicalInfo": {
            "vaccinated": True,
            "spayedNeutered": True,
            "microchipped": True,
            "specialNeeds": False,
            "healthNotes": "Up to date on all vaccinations"
        }
    }
    headers = {'Authorization': 'Bearer {{bearerToken}}'}
    response = requests.post('https://api.petstoreapi.com/v1/pets', json=body, headers=headers).json()
    pet_id = response['id']
    print(pet_id)
    yield pet_id
    print('deleting pet')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pet_id}')

@pytest.fixture(scope='session') # начало фикстуры вызывается в первом тесте, где она указана. Окончание (после yield) вызывается после выполнения последнего теста
def hello():
    print('Hello')
    yield
    print('Bye')

def test_get_one_pet(new_pet_id, hello):
        print('Testing get_one_pet()')
        response = requests.get(f'https://api.petstoreapi.com/v1/pets/{new_pet_id}')
        assert response.json().get('name') == 'Isabella'
        assert response.json().get('size') == 'SMALL'
        assert response.status_code == 200


def test_get_all_pets():
        response = requests.get('https://api.petstoreapi.com/v1/pets').json()
        first_pet = response['data'][0]
        assert first_pet['name'] == 'MedicalPet'

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
def test_smth():
    assert True

@pytest.mark.parametrize('logins', ['', '   ', '#$%^&*'])
def test_smth2(logins):
    assert True