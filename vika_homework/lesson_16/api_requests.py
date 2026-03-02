import requests

def get_all_pets():
    response = requests.get('https://api.petstoreapi.com/v1/pets').json()
    first_pet = response['data'][0]
    print(first_pet)
    assert (first_pet['name']) == 'MedicalPe', 'Incorrect name'

# get_all_pets()

def post_a_pet():
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
    response = requests.post('https://api.petstoreapi.com/v1/pets', json = body, headers = headers).json()
    print(response)

def new_pet():
    body = {
    "name": "Isabella",
    "species": "DOG",
    "breed": "Chihuahua",
    "ageMonths": 18,
    "size": "SMALL",
    "color": "Golden",
    "gender": "FEMALE",
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
    response = requests.post('https://api.petstoreapi.com/v1/pets', json = body, headers = headers).json()
    return response['id']


def put_a_pet():
    pet_id = new_pet()
    body = {
        "price": "3500.00"
    }
    headers = {'Authorization': 'Bearer {{bearerToken}}'}
    response = requests.put(f'https://api.petstoreapi.com/v1/pets/{pet_id}', json=body, headers=headers).json()
    print(response)

put_a_pet()