from locust import task, HttpUser


class SkrepkaUser(HttpUser):

    token = None


    def on_start(self):
        response = self.client.post(
            "https://piton.sft.by/api_v2/token",
            json={
                "username": "PPiter",
                "password": "Luna6666"
            }
        )
        self.token = response.json().get('access')


    @task
    def get_all_applications(self):
        response = self.client.get(
            'https://piton.sft.by/api_v2/applications',
             headers={f'Authorization': f'Bearer {self.token}'})





