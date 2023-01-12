import json
from openapi_server.models import Order

DB_FILE = "db.json"
NEXT_KEY = "next_id"
ORDER_KEY = "orders"


def read_db() -> dict:
    with open(DB_FILE) as file:
        return json.load(file)


def save_db(data) -> None:
    with open(DB_FILE, 'w') as file:
        json.dump(data, file)


def reset_db() -> None:
    data = {}
    data[NEXT_KEY] = 1
    data[ORDER_KEY] = []


def get_value(data, key) -> Order:
    if key in data:
        return data[key]
    else:
        return None


def get_all_orders():
    data = read_db()
    return data[ORDER_KEY]


def insert_data(order_id, order_dict) -> bool:
    data = read_db()
    if order_id in data:
        return False
    else:
        data[NEXT_KEY] += 1
        data["orders"][order_id] = order_dict
        save_db(data)
        return True
