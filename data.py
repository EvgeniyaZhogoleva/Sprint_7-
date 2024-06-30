import random
import string

class DataURL:

    BASE_URL = 'http://qa-scooter.praktikum-services.ru'

class TestCourier:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def __init__(self):
        self.login = self.generate_random_string(10)
        self.password = self.generate_random_string(10)
        self.first_name = self.generate_random_string(10)
        self.NEW_COURIER = {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }

class TestData:
    ORDER_PAYLOAD = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    }


class DataAnswerText:
    OK_TRUE = True
    LOGIN_EXIST = {"message": "Этот логин уже используется. Попробуйте другой."}
    NOT_ENOUGH_DATA_FOR_CREATE = {"message": "Недостаточно данных для создания учетной записи"}
    ACCOUNT_NOT_FOUND = {"message": "Учетная запись не найдена"}
    INSUFFICIENT_LOGIN = {"message": "Недостаточно данных для входа"}