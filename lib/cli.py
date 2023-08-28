from db.models import Salon, Nail_Polish, Place_Order
from simple_term_menu import TerminalMenu
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettycli import red
import random, datetime



# Create a SQLAlchemy engine to connect to the SQLite database
engine = create_engine('sqlite:///db/data.db')
# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()



# Define the start of the application
def start():
    # ASCII art & main page layout
    print("     _       _           _            _")
    print("    / \\   __| |_ __ ___ (_)_ __      / \\   ___ ___ ___  ___ ___")
    print("   / _ \\ / _` | '_ ` _ \\| | '_ \\    / _ \\ / __/ __/ _ \\/ __/ __|")
    print("  / ___ \\ (_| | | | | | | | | | |  / ___ \\ (_| (_|  __/\\__ \\__ \\")
    print(" /_/   \\_\\__,_|_| |_| |_|_|_| |_| /_/   \\_\\___\\___\\___||___/___/")

    print("\n")
    print("----------------- NAIL SALON - RESTRICTED PORTAL -----------------")
    print("\n")


    # Define menu options using dictionaries
    options = [
    {"label": "1. View Current Inventory", "action": "view_inventory"},
    {"label": "2. Update Inventory", "action": "update_inventory"},
    {"label": "3. Place Order", "action": "place_order"},
    {"label": "4. Exit", "action": "exit"}
]
    terminal_menu = TerminalMenu([option["label"] for option in options])
    menu_entry = terminal_menu.show()


    # Create a menu with options
    # options = ["1. View Current Inventory", "2. Update Inventory", "3. Place order", "4. Exit"]
    # terminal_menu = TerminalMenu(options)
    # menu_entry = terminal_menu.show()

    
    # conditional based on user's menu entry option
    if menu_entry == 0:
        view_current_inventory()
    elif menu_entry == 1:
        update_inventory()
    elif menu_entry == 2:
        place_order()
        



# Function to view the current inventory
def view_current_inventory():
    inventory_items = session.query(Salon).all()
    for item in inventory_items:
        print(f"Product: {item.product} | Unit: {item.unit} | Price: {item.price} | Quantity: {item.quantity}")
        print()



# Function to update the inventory, interactive questions and a user's follow through 
def update_inventory():

    # Asks the user whether to add or delete inventory
    update_inventory_input_1 = input("Would you like to add or delete inventory? ")
    
    # Handles adding inventory by updating quantities
    if update_inventory_input_1 == "add":
        products = session.query(Salon.product).all()
        print("\n".join([f"{product[0]}" for product in products]))
        product_name = input("Enter the name of the product to add: ")
        salon = session.query(Salon).filter_by(product=product_name).first()

        if salon:
            print(f"Current quantity for {product_name}: {salon.quantity}")
            update_inventory_input_add_3 = int(input(f"How many units would you like to add? "))
            salon.quantity += update_inventory_input_add_3
            session.commit()
            print(f"Updated quantity for {product_name}: {salon.quantity}")
        else:
            print(f"Product {product_name} not found in inventory.")

    # Handles deleting inventory by updating quantities
    elif update_inventory_input_1 == "delete":
        products = session.query(Salon.product).all()
        print("\n".join([f"{product[0]}" for product in products]))
        product_name = input("Enter the name of the product to delete: ")
        salon = session.query(Salon).filter_by(product=product_name).first()

        if salon:
            print(f"Current quantity for {product_name}: {salon.quantity}")
            update_inventory_input_add_3 = int(input(f"How many units would you like to delete? "))
            salon.quantity -= update_inventory_input_add_3
            session.commit()
            print(f"Updated quantity for {product_name}: {salon.quantity}")
        else:
            print(f"Product {product_name} not found in inventory.")
    # Warns user of invalid selection
    else:
        print(red("invalid selection"))




# Function to place an order
def place_order():
    products = session.query(Salon.product).all()
    print("\n".join([f"{product[0]}" for product in products]))
    product_name = input("Enter the name of the product to order: ")
    salon = session.query(Salon).filter_by(product=product_name).first()

    if salon:
        quantity = int(input(f"How many units of {product_name} would you like to order? "))
        place_order_input = input(f"Are you sure you want to order {quantity} of {product_name}? y/n ")
        if place_order_input == 'y':
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            digits = "0123456789"
            order_number = ''.join(random.choice(letters) for _ in range(3)) + ''.join(random.choice(digits) for _ in range(5))
            # print(f"Order {order_number} placed")
            current_datetime = datetime.datetime.now()
            print(f"Order {order_number} placed on {current_datetime.strftime('%Y-%m-%d %H:%M')}")


            # Create a new Place_Order instance and add it to the database
            new_order = Place_Order(product_id=salon.id, quantity=quantity, order_number=order_number, date_order_placed=current_datetime)
            session.add(new_order)
            session.commit()
            print("Order saved to the database.")

        elif place_order_input == 'n':
            place_order()
        else:
            print("invalid selection")

    else:
        print(f"Product {red(product_name)} is not an authorized product to order.")


# Entry point for the script
if __name__ == "__main__":
    
    start()

