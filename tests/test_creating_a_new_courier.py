import string
import random
import requests
import allure

class TestCreateNewCourier:

    @allure.title('Тест создания нового курьера')
    @allure.description('Тест создания нового курьера с заполнением всех обязательных полей')
    def test_create_new_courier(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)

        assert response.status_code == 201
        assert "ok" in response.json()
        assert response.json()["ok"] == True

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass

    @allure.title('Тест не возможности создания 2-х одинаковых курьеров')
    @allure.description('Тест не возможности создания 2-х курьеров с одинаковым логином')
    def test_create_courier_duplicate_login(self):
        payload = {
            "login": "ninja",
            "password": "1234",
            "firstName": "saske"
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert 409 == response.status_code
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Тест не возможности создания курьера без логина')
    @allure.description('Тест не возможности создания курьера без передачи логина в теле запроса')
    def test_create_courier_without_login(self):
        payload = {
            "password": "1234",
            "firstName": "saske"
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert 400 == response.status_code
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Тест не возможности создания курьера без пароля')
    @allure.description('Тест не возможности создания курьера без передачи пароля в теле запроса')
    def test_create_courier_without_password(self):
        payload = {
            "login": "ninja",
            "firstName": "saske"
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert 400 == response.status_code
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
