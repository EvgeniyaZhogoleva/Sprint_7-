import requests
import allure
from data import TestCourier
from data import DataURL
from data import DataAnswerText


base_url = f'{DataURL.BASE_URL}/api/v1/courier'

class TestCreateNewCourier:

    @allure.title('Тест создания нового курьера')
    @allure.description('Тест создания нового курьера с заполнением всех обязательных полей')
    def test_create_new_courier(self):
        test_courier = TestCourier()
        payload = test_courier.NEW_COURIER
        response = requests.post(base_url, json=payload)
        assert 201 == response.status_code
        assert response.json()["ok"] == DataAnswerText.OK_TRUE

    @allure.title('Тест не возможности создания 2-х одинаковых курьеров')
    @allure.description('Тест не возможности создания 2-х курьеров с одинаковым логином')
    def test_create_courier_duplicate_login(self):
        payload = {
            "login": "ninja",
            "password": "1234",
            "firstName": "saske"
        }

        response = requests.post(base_url, json=payload)
        assert 409 == response.status_code
        assert response.json()["message"] == DataAnswerText.LOGIN_EXIST["message"]

    @allure.title('Тест не возможности создания курьера без логина')
    @allure.description('Тест не возможности создания курьера без передачи логина в теле запроса')
    def test_create_courier_without_login(self):
        payload = {
            "password": "1234",
            "firstName": "saske"
        }

        response = requests.post(base_url, json=payload)
        assert 400 == response.status_code
        assert response.json()["message"] == DataAnswerText.NOT_ENOUGH_DATA_FOR_CREATE["message"]

    @allure.title('Тест не возможности создания курьера без пароля')
    @allure.description('Тест не возможности создания курьера без передачи пароля в теле запроса')
    def test_create_courier_without_password(self):
        payload = {
            "login": "ninja",
            "firstName": "saske"
        }

        response = requests.post(base_url, json=payload)
        assert 400 == response.status_code
        assert response.json()["message"] == DataAnswerText.NOT_ENOUGH_DATA_FOR_CREATE["message"]
