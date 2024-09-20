# Ирина Коробкова, 21-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

BASE_URL = 'https://f6c28cec-f406-431b-9c08-5f784ad72b6e.serverhub.praktikum-services.ru/api/v1'


def test_create_and_get_order():
    # Шаг 1: Выполнить запрос на создание заказа
    create_order_payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"],
    }

    create_response = requests.post(
        f"{BASE_URL}/orders", json=create_order_payload
    )
    assert create_response.status_code == 201

    # Шаг 2: Сохранить номер трека заказа
    track = create_response.json().get('track')
    assert track is not None

    # Шаг 3: Выполнить запрос на получение заказа по треку заказа
    get_response = requests.get(f"{BASE_URL}/orders/track?t={track}")

    # Шаг 4: Проверить, что код ответа равен 200
    assert get_response.status_code == 200

