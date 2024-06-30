import allure
import requests
from data import DataURL
from data import DataAnswerText


base_url = f'{DataURL.BASE_URL}/api/v1/courier/login'

class TestCourierLogin:

    @allure.title('Тест авторизации курьера')
    @allure.description('Тест авторизации курьера с корректными данными')
    def test_successful_login(self):
        payload = {
            "login": "1ninja1",
            "password": "1234"
        }
        response = requests.post(base_url, data=payload)
        assert 200 == response.status_code
        assert 'id' in response.json()

    @allure.title('Тест авторизации курьера без параметра логин')
    @allure.description('Тест авторизации курьера без передачи логина в теле запроса')
    def test_missing_fields(self):
        payload = {
            "password": "1234"
        }
        response = requests.post(base_url, json=payload)
        assert 400 == response.status_code
        assert response.json()["message"] == DataAnswerText.INSUFFICIENT_LOGIN["message"]

    @allure.title('Тест авторизации курьера с некорректными паролем')
    @allure.description('Тест авторизации курьера с передаваемым в теле запроса пароля со значением "wrong_password"')
    def test_invalid_credentials(self):
        payload = {
            "login": "ninja",
            "password": "wrong_password"
        }
        response = requests.post(base_url, json=payload)
        assert 404 == response.status_code
        assert response.json()["message"] == DataAnswerText.ACCOUNT_NOT_FOUND["message"]

    @allure.title('Тест авторизации курьера с несуществующем пользователем')
    @allure.description('Тест авторизации курьера с передаваемым в теле запроса логина со значением "nonexistent_user"')
    def test_nonexistent_user(self):
        payload = {
            "login": "nonexistent_user",
            "password": "1234"
        }
        response = requests.post(base_url, json=payload)
        assert 404 == response.status_code
        assert response.json()["message"] == DataAnswerText.ACCOUNT_NOT_FOUND["message"]