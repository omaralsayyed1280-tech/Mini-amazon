# main.py
from users import UserSystem
from products import ProductSystem
from cart import CartSystem
from orders import OrderSystem
from storage import load_data

user_system = UserSystem()
product_system = ProductSystem()
cart_system = CartSystem()
order_system = OrderSystem()

def store_menu(username):
    while True:
        print("\n1. Browse\n2. Search\n3. Add to cart\n4. View cart\n5. Checkout\n6. Orders\n7. Logout")
        choice = input("Choice: ")

        if choice == "1":
            product_system.list_products()

        elif choice == "2":
            product_system.search_product()

        elif choice == "3":
            cart_system.add_to_cart(username)

        elif choice == "4":
            cart_system.view_cart(username)

        elif choice == "5":
            carts = load_data("carts.json")
            user_cart = next((c for c in carts if c["username"] == username), None)

            if not user_cart:
                print("Cart empty.")
                continue

            total = cart_system.view_cart(username)
            order_system.create_order(username, user_cart["items"], total)

            # reduce stock
            for item in user_cart["items"]:
                product_system.update_stock(item["product_id"], item["qty"])

            cart_system.clear_cart(username)
            print("Checkout successful.")

        elif choice == "6":
            order_system.view_orders(username)

        elif choice == "7":
            break

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choice: ")

        if choice == "1":
            user_system.register()

        elif choice == "2":
            user = user_system.login()
            if user:
                store_menu(user)

        elif choice == "3":
            break

if __name__ == "__main__":
    main()