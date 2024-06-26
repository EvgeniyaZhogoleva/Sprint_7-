import requests
import pytest
import allure


class TestScooterOrders:

    @allure.title('Создание нового заказа с выбором одного из цветов: серый или чёрный')
    @pytest.mark.parametrize("color", ["BLACK", "GREY", None])
    def test_create_order_with_single_color(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }
        if color is not None:
            payload["color"] = [color]
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)
        assert 201 == response.status_code
        assert 'track' in response.json()

    @allure.title('Создание нового заказа с выбором обоих цветов')
    def test_create_order_with_multiple_colors(self):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK", "GREY"]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)
        assert 201 == response.status_code
        assert 'track' in response.json()

    @allure.title('Создание нового заказа без выбора цвета')
    def test_create_order_without_color(self):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)
        assert 201 == response.status_code
        assert 'track' in response.json()