import pytest
import requests

# файлик conftest хранит общие для файлов с тестами фикстуры. Если нужна кастомная фикстура для тестов папки, то файлик заводится
# в папке. Если для тестов конкретного файла - то прямо с этими тестами. Пайтест сначала берет файловские, потом папковские, потом корневого файла

@pytest.fixture()
def number():
    return 1


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
    print('\ndeleting pet')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pet_id}')


@pytest.fixture(scope='session') # начало фикстуры вызывается в первом тесте, где она указана. Окончание (после yield) вызывается после выполнения последнего теста
def hello():
    print('\nHello')
    yield
    print('\nBye')