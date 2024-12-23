import os
import json


def init_store(filename = 'data.json'):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump([], f)

def get_store(filename = 'data.json'):
    with open(filename, "r") as f:
        return json.load(f)

def update_store(data, filename = 'data.json'):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def add_order(order):
    Orders = get_store()
    Orders.append(order)
    update_store(Orders)


def get_order(orderId):
    Orders = get_store()
    return next((order for order in Orders if order.get('orderId') == orderId), None)