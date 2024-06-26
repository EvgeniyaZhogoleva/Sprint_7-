import requests
import pytest
import allure


class TestOrders:
    @allure.title('Получение списка заказов без указания id курьера')
    def test_orders_list_returns_orders(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert 200 == response.status_code
        assert "orders" in response.json()
