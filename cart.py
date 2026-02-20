# cart.py
from storage import load_data, save_data
from products import ProductSystem

CART_FILE = "carts.json"

class CartSystem:

    def add_to_cart(self, username):
        carts = load_data(CART_FILE)
        product_system = ProductSystem()

        product_id = input("Enter product ID: ")
        product = product_system.get_product(product_id)

        if not product:
            print("Product not found.")
            return

        quantity = int(input("Quantity: "))
        if quantity <= 0 or quantity > product["stock"]:
            print("Invalid quantity.")
            return

        # Find user cart
        user_cart = next((c for c in carts if c["username"] == username), None)

        if not user_cart:
            user_cart = {"username": username, "items": []}
            carts.append(user_cart)

        user_cart["items"].append({
            "product_id": product_id,
            "qty": quantity,
            "unit_price": product["price"]
        })

        save_data(CART_FILE, carts)
        print("Item added to cart.")

    def view_cart(self, username):
        carts = load_data(CART_FILE)
        user_cart = next((c for c in carts if c["username"] == username), None)

        if not user_cart or not user_cart["items"]:
            print("Cart is empty.")
            return 0

        total = 0
        for item in user_cart["items"]:
            subtotal = item["qty"] * item["unit_price"]
            total += subtotal
            print(f'{item["product_id"]} | Qty: {item["qty"]} | Subtotal: ${subtotal}')

        print("Total:", total)
        return total

    def clear_cart(self, username):
        carts = load_data(CART_FILE)
        carts = [c for c in carts if c["username"] != username]
        save_data(CART_FILE, carts)