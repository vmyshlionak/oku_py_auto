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


# запускаем командой locust в консоли, переходим по адресу, предложенному в ответ.
# Там в браузере указываем нужный хост и количество юзеров. Наблюдаем. У task может быть приорити в скобочках.
# Task(1) and Task(3) - сила 3 вызывает метод в 3 раза чаще




