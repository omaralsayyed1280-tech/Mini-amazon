
from storage import load_data, save_data

PRODUCTS_FILE = "products.json"

class ProductSystem:

    def list_products(self):
        products = load_data(PRODUCTS_FILE)
        for p in products:
            print(f'{p["product_id"]} - {p["name"]} | ${p["price"]} | Stock: {p["stock"]}')

    def search_product(self):
        keyword = input("Search keyword: ").lower()
        products = load_data(PRODUCTS_FILE)

        for p in products:
            if keyword in p["name"].lower():
                print(f'{p["product_id"]} - {p["name"]} | ${p["price"]}')

    def get_product(self, product_id):
        products = load_data(PRODUCTS_FILE)
        for p in products:
            if p["product_id"] == product_id:
                return p
        return None

    def update_stock(self, product_id, quantity):
        products = load_data(PRODUCTS_FILE)
        for p in products:
            if p["product_id"] == product_id:
                p["stock"] -= quantity
        save_data(PRODUCTS_FILE, products)