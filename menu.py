#import and use a table formatting library because writing homespun code for terminal  menus is messy
from tabulate import tabulate
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
menu_orders = []
# Abstract the item ordering logic into a function
def request_menu_order(menu_items):
    customer_choice = input('Enter the item number for the menu item you want to order: ')
    # Check if the customer typed a number
    if customer_choice.isnumeric():
        # Convert the menu selection to an integer
        customer_choice = int(customer_choice)

        # Check if the menu selection is in the menu items
        if customer_choice in menu_items.keys():
            # Store the item name as a variable
            ordered_item_name = menu_items[customer_choice]['Item name']
            print(f"{ordered_item_name} ordered item name")

            # Ask the customer for the quantity of the menu item
            quantity_ordered = input(f'How many {ordered_item_name} would you like? ')

            # Check if the quantity is a number, default to 1 if not
            if not quantity_ordered.isnumeric():
                quantity_ordered = 1
            else:
                quantity_ordered = int(quantity_ordered)

            # Add the item name, price, and quantity to the order list
            order_item = menu_items[customer_choice]
            order_item['Quantity'] = quantity_ordered
            menu_orders.append(order_item)
            
        else:
            # Tell the customer they didn't select a menu option
            print("That menu option is not available.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
#Put the menu printing code in its own function 
def print_menu(menu):
    print("From which menu would you like to order? ")
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # Call the request_menu_order function 
            request_menu_order(menu_items)
        else: 
            print("You entered a number that is not on the menu.")


# Put the order printing logic in a function for clarity 
def print_order(menu_orders):
    # Use list comprehension to destructure the order into a format suitable for the tabulate function
    table = [[order_item['Item name'], order_item["Quantity"], order_item['Price']] for order_item in menu_orders]
    #configure table with headers
    table_result = tabulate(table, ['Item name', 'Quantity', 'Price'])
    #print table
    print(table_result)
    # calculate order total
    total_price = sum([item['Price'] * item['Quantity'] for item in menu_orders])
    #print total
    print(f"The total price of your order is ${total_price:0.2f}")


# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print_menu(menu)
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        if keep_ordering.lower() in ['y', 'yes']:
            keep_ordering_bool = True
        elif keep_ordering.lower() in ['n', 'no']:
            keep_ordering_bool = False
        else:
            #If the user enters an invalid response
            keep_ordering_bool = None
        match keep_ordering_bool:
            case  True:
        # Set the ordering condition to a boolean True if user says yes
        # 5. Check the customer's input
                request_menu_order(menu_items)
                # Keep ordering
            case False: 
                break 
            case _:
                input('Your answer was invalid. Please try again')  
    print('Thanks for ordering!')
    print_order(menu_orders)
