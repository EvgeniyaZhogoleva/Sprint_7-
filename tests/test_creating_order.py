import requests
import allure
from data import DataURL
from data import TestData


base_url = f'{DataURL.BASE_URL}/api/v1/orders'

class TestScooterOrders:

    @allure.title('Создание нового заказа с выбором одного из цветов: серый или чёрный')
    def test_create_order_with_single_color(self):
        payload = TestData.ORDER_PAYLOAD.copy()
        payload["color"] = ["BLACK"]

        response = requests.post(base_url, json=payload)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание нового заказа с выбором обоих цветов')
    def test_create_order_with_multiple_colors(self):
        payload = TestData.ORDER_PAYLOAD.copy()
        payload["color"] = ["BLACK", "GREY"]

        response = requests.post(base_url, json=payload)
        assert 201 == response.status_code
        assert 'track' in response.json()

    @allure.title('Создание нового заказа без выбора цвета')
    def test_create_order_without_color(self):
        payload = TestData.ORDER_PAYLOAD

        response = requests.post(base_url, json=payload)
        assert 201 == response.status_code
        assert 'track' in response.json()

