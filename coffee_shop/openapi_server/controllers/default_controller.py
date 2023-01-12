import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.order import Order  # noqa: E501
from openapi_server import util
from openapi_server import db_utils

from datetime import datetime

def delete_order(id_):  # noqa: E501

    """Cancels an order
    Canceles an order # noqa: E501
    :param id: Order ID to delete
    :type id: int
    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    #Import the data base

    db = db_utils.read_db()
    #find the matching id and delete that order using pop
    order_found = False
    for k, v in db["orders"].items():
        if v['id'] == id_:

            print("deleting... ")
            print(id_)
            db["orders"].pop(k)
            order_found = True
            break 

    if not order_found:
        print('No order id found')
        return 'No Order with this ID Found', 406

    #rewrite the json file :)
    db_utils.save_db(db)

    return 'Order Deleted', 200


def order_id_get(id_):  # noqa: E501
    """Returns a given order id as json

     # noqa: E501

    :param id: The id associated with an order
    :type id: int

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    data = db_utils.read_db()['orders']
    order = db_utils.get_value(data, str(id_))

    if not order:
        return "No Order with this ID found", 406

    return order


def order_post(new_order=None):  # noqa: E501
    """Add a new order

    Place a new unique order onto the queue # noqa: E501

    :param new_order: 
    :type new_order: dict | bytes

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_order = connexion.request.get_json()
        db = db_utils.read_db()

        # If the order does not match the order schema the input was malformed
        required_keys = set(
            [
            'orderItems',
            'status',
            'customerName',
            'discount'
            ]
        )

        if set(new_order.keys()) != required_keys:
            return 'Required Order items not provided', 401
        _id = db["next_id"]
        new_order["id"] = _id
        new_order["createdTimestamp"] = str(datetime.now())


        # Attempt to insert
        inserted = db_utils.insert_data(_id, new_order)

        # Return if inserted, else return a internal error
        if inserted:
            return 'Order Inserted', 200
        else:
            return 'Error inserting order', 500

    # If json not provided then return 401
    return 'Input not in JSON Format', 401


def orders_get(customer_name=None):  # noqa: E501
    """Returns a list of all orders

    Gets all the orders that are currently open # noqa: E501

    :param customer_name: The name of the customer to filter the result by
    :type customer_name: str

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    all_orders = db_utils.get_all_orders()
    if customer_name:
        json_orders = {str(o["id"]): o for o in all_orders.values() if o["customerName"] == customer_name}
        return json_orders
    return all_orders, 200


def path_order(id, order):  # noqa: E501
    """Update an existing order

    Update an existing order # noqa: E501

    :param id: Id associated with order
    :type id: int
    :param order: 
    :type order: dict | bytes

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        order = Order.from_dict(connexion.request.get_json())  # noqa: E501
        db_obj = db_utils.get_value(id)
        if db_obj:
            db_order = Order.from_dict(db_obj)
            # todo
            return "updated"
        else:
            return "ID not found"
    return "Invalid object"
