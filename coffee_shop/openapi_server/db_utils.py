import json
from openapi_server.models import Order

DB_FILE = "db.json"
NEXT_KEY = "next_id"
ORDER_KEY = "orders"


def read_db() -> dict:
    with open(DB_FILE) as file:
        return json.load(file)


def save_db(data) -> None:
    with open(DB_FILE) as file:
        json.dump(data, file)


def reset_db() -> None:
    data = {}
    data[NEXT_KEY] = 1
    data[ORDER_KEY] = []


def get_value(key) -> Order:
    data = read_db()
    if key in data:
        return data[key]
    else:
        return None


def get_all_orders():
    data = read_db()
    return data[ORDER_KEY]


def insert_data(order_id, order_obj) -> bool:
    data = read_db()
    if order_id in data:
        return False
    elif not isinstance(order_obj, Order):
        print("object_obj is not an instance of Order")
        return False
    else:
        next_id = data[NEXT_KEY]
        data[ORDER_KEY][next_id] = order_obj
        data[NEXT_KEY] = next_id + 1
        save_db(data)
        return True
