# Mini Amazon – Console-Based E-Commerce System

📌 Project Overview

This project is a console-based Mini Amazon system developed in Python.

It simulates a simplified e-commerce platform where users can:
- Register and login
- Browse and search products
- Add products to a shopping cart
- Checkout and generate orders
- View order history

The system uses JSON files for persistent data storage and follows object-oriented design principles.

⚠️⚠️⚠️HOW TO RUN⚠️⚠️⚠️:
1. create a folder and name it "mini amazon"
2. download the files and place them inside the folder you created
3. open VS and select the folder then go to main.py and run

Project Structure


"mini_amazon" is the main folder then inside is:
main.py
users.py
products.py
cart.py
orders.py
storage.py
users.json
products.json
carts.json
orders.json

The program will start with the Welcome Menu.



User System
- User registration (unique username)
- Password validation (minimum 6 characters)
- User login authentication
- Persistent user storage (users.json)
Product Catalog
- List all available products
- Search products (case-insensitive)
- View product details
- Stock validation
- Persistent product storage (products.json)
Cart System
- Add items to cart
- Prevent adding more than available stock
- View cart with subtotal and total
- Clear cart after checkout
- Persistent cart storage (carts.json)
Checkout System
- Stock re-validation before purchase
- Deduct stock after successful checkout
- Generate unique Order ID
- Save order with timestamp
- View order history
- Persistent order storage (orders.json)
Error Handling
- Input validation
- Invalid menu choice handling
- Prevention of negative quantities
- Prevention of duplicate usernames


How Data Is Stored

The system uses JSON files for data persistence:

- users.json Stores registered users
- products.json Stores product catalog
- carts.json Stores user carts
- orders.json Stores order history

Data is loaded and saved using a reusable storage module (`storage.py`) that handles reading and writing JSON safely.

Example product format:

{
  "product_id": "P1001",
  "name": "USB-C Cable",
  "price": 9.99,
  "stock": 30
}


Example order format:


{
  "order_id": "O0001",
  "username": "alice",
  "items": [
     {"product_id": "P1002", "qty": 1, "unit_price": 19.99}
  ],
  "total": 19.99,
  "timestamp": "2026-02-10 18:12:44"
}


Known Limitations

- Passwords are stored in plain text (not hashed).
- No concurrency handling (single-user console system).
- No graphical user interface (console only).
- No database integration (JSON used instead).
- No admin panel for product management.

Possible Future Improvements

- Password hashing using hashlib
- Admin mode to manage products
- Discount code system
- Shipping cost calculation
- Export receipts to text files
- Unit testing
- Migration to SQLite or web framework (Flask/Django)




