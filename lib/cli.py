from db.models import Salon
from simple_term_menu import TerminalMenu
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///db/data.db')
Session = sessionmaker(bind=engine)
session = Session()



def start():
    print("     _       _           _            _")
    print("    / \\   __| |_ __ ___ (_)_ __      / \\   ___ ___ ___  ___ ___")
    print("   / _ \\ / _` | '_ ` _ \\| | '_ \\    / _ \\ / __/ __/ _ \\/ __/ __|")
    print("  / ___ \\ (_| | | | | | | | | | |  / ___ \\ (_| (_|  __/\\__ \\__ \\")
    print(" /_/   \\_\\__,_|_| |_| |_|_|_| |_| /_/   \\_\\___\\___\\___||___/___/")

    # for _ in range(3):
    print("\n")

    print("-----------------MARILYN'S NAIL SALON RESTRICTED PORTAL-----------------")

    print("\n")

    options = ["1. View Current Inventory", "2. Update Inventory", "3. SOS order", "4. Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry = terminal_menu.show()
    
    if menu_entry == 0:
        view_current_inventory()


def view_current_inventory():
    inventory_items = session.query(Salon).all()
    for item in inventory_items:
        print(f"Product: {item.product}, Price: {item.price}, Quantity: {item.quantity}")

if __name__ == "__main__":
    start()












# from simple_term_menu import TerminalMenu
# from models import Salon, Nail_Polish
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# def start():
#     print("     _       _           _            _")
#     print("    / \\   __| |_ __ ___ (_)_ __      / \\   ___ ___ ___  ___ ___")
#     print("   / _ \\ / _` | '_ ` _ \\| | '_ \\    / _ \\ / __/ __/ _ \\/ __/ __|")
#     print("  / ___ \\ (_| | | | | | | | | | |  / ___ \\ (_| (_|  __/\\__ \\__ \\")
#     print(" /_/   \\_\\__,_|_| |_| |_|_|_| |_| /_/   \\_\\___\\___\\___||___/___/")

#     # for _ in range(3):
#     print("\n")

#     print("-----------------MARILYN'S NAIL SALON RESTRICTED PORTAL-----------------")

#     print("\n")

#     options = ["1. View Current Inventory", "2. Update Inventory", "3. SOS order", "4. Exit"]
#     terminal_menu = TerminalMenu(options)
#     menu_entry = terminal_menu.show()
#     # print(f"Confirm selection: {options[menu_entry]}")

# start()





    # print("1. View Current Inventory")
    # print("2. Update Inventory")
    # print("3. SOS order")
    # print("4. Exit")
    # user_input = input("Please make a selection (1-3): ")

 





