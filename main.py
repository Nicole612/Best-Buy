import sys
from products import Product
from store import Store


def display_list_products(store):
    """Displays all active products in the store, each with index, name, price, and quantity."""
    print("------")
    for index, product in enumerate(store.get_all_products(), start=1):
        print(f"{index}. {product.show()}")
    print("------")


def get_total_quantity(store):
    """# Prints the total quantity of all products currently in the store."""
    print(f"Total of {store.get_total_quantity()} items in store")


def place_order(store):
    """  Allows user to select products and quantities in a loop,
         builds an order list, and processes the total order.
         Ends when the user presses Enter without input.
    """
    all_products = store.get_all_products()
    order_list = []

    print("------")
    display_list_products(store)
    print("When you want to finish order, enter empty text.")

    while True:
        selected_index = input("Which Product # do you want? ")
        selected_quantity = input("What amount do you want? ").strip()
        if not selected_index or not selected_quantity:
            break
        product_index = int(selected_index) - 1
        if product_index < 0 or product_index >= len(all_products):
            print("Invalid number to choose a product. Please try again!")
            continue

        try:
            order = all_products[product_index], int(selected_quantity)
            order_list.append(order)
            print("Product added to list!\n")
        except ValueError:
            print("Your order ist fail. Start your order again.")

    if order_list:
        print()
        print("********")
        total = store.order(order_list)
        print(f"Order made! Total payment: ${total}")
        display_list_products(store)


def initial_menu(menu):
    """ Displays the store menu using the keys and labels from the `menu` dictionary. """
    print()
    print("   Store Menu")
    print("   ----------")
    for menu_choice, description in menu.items():
        print(f"{menu_choice}: {description[0]}")


def action_choice(input_choice, store):
    """ Executes the appropriate action based on user input."""
    try:
        if input_choice == 1:
            display_list_products(store)
        elif input_choice == 2:
            get_total_quantity(store)
        elif input_choice == 3:
            place_order(store)
        elif input_choice == 4:
            sys.exit()
    except ValueError:
        print("Invalid menu selection. Please choose a vadid number!")


def start(store):
    """ Main menu loop that keeps prompting the user for actions.
        Calls `action_choice()` after displaying the menu."""
    menu = {
        1: ["List all products in store", display_list_products],
        2: ["Show total amount in store", get_total_quantity],
        3: ["Make an order", place_order],
        4: ["Quit", None]
    }

    while True:
        initial_menu(menu)
        try:
            choose_number = int(input("Please choose a number: "))
            action_choice(choose_number, store)
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")


def main():
    """ Initializes a list of sample products, creates a Store instance with them,
            and starts the interactive store menu where the user can browse products,
            check inventory, and place orders. """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]
    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
    start(best_buy)


if __name__=="__main__":
    main()
