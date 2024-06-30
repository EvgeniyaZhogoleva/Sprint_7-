import requests
import allure
from data import DataURL


class TestOrders:
    @allure.title('Получение списка заказов без указания id курьера')
    def test_orders_list_returns_orders(self):
        base_url = f'{DataURL.BASE_URL}/api/v1/orders'
        payload = {}
        response = requests.get(base_url, data=payload)
        assert 200 == response.status_code
        assert "orders" in response.json()