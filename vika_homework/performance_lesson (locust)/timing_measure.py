import requests
import datetime

from werkzeug.datastructures import Authorization


#дедовский метод
# start = datetime.datetime.now()
# response = requests.get('https://api.petstoreapi.com/v1/pets')
# print(response)
# end = datetime.datetime.now()
# print (end - start)



def get_token(username, password):
    response = requests.post(
            "https://piton.sft.by/api_v2/token",
            json={
                "username": username,
                "password": password
            }
        )

    token = response.json().get('access')
    return token

access_token = get_token("PPiter", "Luna6666")
print(access_token)

def get_applications():
    response = requests.get(
        'https://piton.sft.by/api_v2/applications',
        headers={f'Authorization': f'Bearer {access_token}'})
    print(response)


get_applications()