import requests
import unittest
import sys

# название файла, класса и методов с ассертами должно начинаться с test

class TestPet(unittest.TestCase):

    def setUp(self):
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
        self.pet_id = response['id']

    def tearDown(self):
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.pet_id}')

    @unittest.skipIf(sys.platform == 'win32', 'Not for Windows')
    def test_get_one_pet(self):
        response = requests.get(f'https://api.petstoreapi.com/v1/pets/{self.pet_id}')
        self.assertEqual(response.json().get('name'), 'Isabella')
        self.assertEqual(response.json().get('size'), 'SMALL')
        self.assertEqual(response.json().get('status'), 'AVAILABLE')
        self.assertEqual(response.status_code, 200)

class TestIndependent(unittest.TestCase):

    @unittest.skip("Known issue")
    def test_get_all_pets(self):
        response = requests.get('https://api.petstoreapi.com/v1/pets').json()
        first_pet = response['data'][0]
        self.assertEqual(first_pet['name'], 'MedicalPet')

    def test_post_a_pets(self):
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
        self.assertEqual(response, 201)


