import allure
import requests
import pytest

class TestCourierLogin:

    @allure.title('Тест авторизации курьера')
    @allure.description('Тест авторизации курьера с корректными данными')
    def test_successful_login(self):
        payload = {
            "login": "1ninja1",
            "password": "1234"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert 200 == response.status_code
        assert 'id' in response.json()

    @allure.title('Тест авторизации курьера без параметра логин')
    @allure.description('Тест авторизации курьера без передачи логина в теле запроса')
    def test_missing_fields(self):
        payload = {
            "password": "1234"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert 400 == response.status_code
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Тест авторизации курьера с некорректными паролем')
    @allure.description('Тест авторизации курьера с передаваемым в теле запроса пароля со значением "wrong_password"')
    def test_invalid_credentials(self):
        payload = {
            "login": "ninja",
            "password": "wrong_password"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert 404 == response.status_code
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Тест авторизации курьера с несуществующем пользователем')
    @allure.description('Тест авторизации курьера с передаваемым в теле запроса логина со значением "nonexistent_user"')
    def test_nonexistent_user(self):
        payload = {
            "login": "nonexistent_user",
            "password": "1234"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert 404 == response.status_code
        assert response.json()["message"] == "Учетная запись не найдена"
