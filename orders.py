# orders.py
from storage import load_data, save_data
from datetime import datetime
import uuid

ORDERS_FILE = "orders.json"

class OrderSystem:

    def create_order(self, username, items, total):
        orders = load_data(ORDERS_FILE)

        order = {
            "order_id": str(uuid.uuid4())[:8],
            "username": username,
            "items": items,
            "total": total,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        orders.append(order)
        save_data(ORDERS_FILE, orders)

    def view_orders(self, username):
        orders = load_data(ORDERS_FILE)
        for order in orders:
            if order["username"] == username:
                print(order)