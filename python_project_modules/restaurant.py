# This file holds everything a restaurant can do.
#
# A restaurant can:
#   - see its own food
#   - add a new food item
#   - change a price
#   - mark an item as sold out, or back in stock
#   - delete an item completely
#
# Nothing here ever touches another restaurant's food. Every time we
# look for an item we check whose it is.

import python_project_modules.design as design
from python_project_modules.data import DATA, save_data


def my_items(username):
    """Return a list of this restaurant's own food items.

    username is the restaurant that is logged in.
    The returned list holds the food IDs, not the whole item.
    """
    items = []

    for item_id in DATA["food"]:
        if DATA["food"][item_id]["restaurant"] == username:
            items.append(item_id)

    return items


def new_food_id():
    """Make a brand new food ID that is not being used yet.

    We start counting from the number of items we have and add 101.
    If that ID is already taken we move to the next one, until we find
    a free one. This matters because deleting an item makes the list
    shorter, which could otherwise repeat an old ID.
    """
    number = len(DATA["food"]) + 101

    while ("F" + str(number)) in DATA["food"]:
        number = number + 1

    return "F" + str(number)


def read_price():
    """Ask for a price and make sure it is a real number.

    Returns the price as a float, or None if what was typed was not
    a number we can use.
    """
    text = input("Price: ")

    # remove one point, so that "250" and "250.50" both pass
    cleaned = text.replace(".", "", 1)

    # isalpha means it is only letters, isdigit means only numbers
    # if it is not letters and it is digits, it is a number
    if cleaned.isdigit():
        price = float(text)

        if price < 0:
            design.warn("The price cannot be less than zero.")
            return None

        return price

    design.warn("Please type a number for the price, like 250 or 250.50.")
    return None


def ask_item_id(username, action):
    """Ask which food item we are working on, and check it is theirs.

    Returns the item ID, or None if it was not found.
    """
    item_id = input("Food ID (for example F101): ")
    item_id = item_id.upper()

    if item_id not in DATA["food"]:
        design.warn("There is no food item with the ID " + item_id + ".")
        return None

    if DATA["food"][item_id]["restaurant"] != username:
        design.warn("That item belongs to a different restaurant.")
        return None

    return item_id


def show_my_food(username):
    """Show this restaurant's food in two tables.

    The available items are in the first table and the sold out items
    are in the second one, so it is easy to see what needs restocking.
    """
    items = my_items(username)

    if len(items) == 0:
        design.heading("My food")
        design.warn("You have not added any food yet.")
        print()
        return

    available = []
    sold_out = []

    for item_id in items:
        item = DATA["food"][item_id]

        if item["available"]:
            available.append(food_line(item_id))
        else:
            sold_out.append(food_line(item_id))

    design.heading("Available now")

    if len(available) == 0:
        design.line("Nothing available right now.")
        print()
    else:
        design.box("ON SALE", available)

    design.heading("Sold out")

    if len(sold_out) == 0:
        design.line("Nothing is sold out.")
        print()
    else:
        design.box("SOLD OUT", sold_out)

    design.line("Total items: " + str(len(items))
                + "   |   On sale: " + str(len(available))
                + "   |   Sold out: " + str(len(sold_out)))
    print()


def food_line(item_id):
    """Turn one food item into a line of text for a box.

    The columns are name, then ID, then price. customer.py uses the
    same helper from design.py, so both menus look the same.
    """
    item = DATA["food"][item_id]
    name = design.pad_right(item["name"], 24) + item_id

    return design.columns(name, design.money(item["price"]), 32)


def add_food(username):
    """Add one new food item to the restaurant's menu."""
    design.heading("Add a new food item")

    name = input("Name of the food: ")

    if len(name) == 0:
        design.warn("The name cannot be empty.")
        return

    # the name has to fit inside one line of the table, otherwise the
    # table would run off the side of the screen
    if len(name) > 24:
        design.warn("Please keep the name under 25 letters.")
        return

    price = read_price()

    if price is None:
        return

    item_id = new_food_id()

    DATA["food"][item_id] = {
        "name": name,
        "price": price,
        "restaurant": username,
        "available": True,
    }

    save_data()

    print()
    design.ok("Added " + name + " as " + item_id + ".")


def change_price(username):
    """Change the price of one food item."""
    design.heading("Change a price")
    show_my_food(username)

    item_id = ask_item_id(username, "change")

    if item_id is None:
        return

    item = DATA["food"][item_id]
    design.line("Current price of " + item["name"] + " is "
                + design.money(item["price"]))
    print()

    price = read_price()

    if price is None:
        return

    item["price"] = price
    save_data()

    print()
    design.ok("New price for " + item["name"] + " is " + design.money(price) + ".")


def toggle_available(username):
    """Mark an item as sold out, or put it back on sale."""
    design.heading("Sold out, or back in stock?")
    show_my_food(username)

    item_id = ask_item_id(username, "toggle")

    if item_id is None:
        return

    item = DATA["food"][item_id]

    # "not" flips True into False and False into True
    item["available"] = not item["available"]

    save_data()

    print()

    if item["available"]:
        design.ok(item["name"] + " is back on sale.")
    else:
        design.ok(item["name"] + " is marked sold out.")


def delete_food(username):
    """Delete one food item for good.

    We warn the restaurant first, because this cannot be undone.
    Old orders keep their own copy of the details, so past orders
    are not affected by this.
    """
    design.heading("Delete a food item")
    show_my_food(username)

    item_id = ask_item_id(username, "delete")

    if item_id is None:
        return

    name = DATA["food"][item_id]["name"]

    print()
    design.warn("This will remove " + name + " from your menu for good.")
    answer = input("Type YES to confirm: ")

    if answer != "YES":
        design.line("Nothing was deleted.")
        return

    del DATA["food"][item_id]
    save_data()

    print()
    design.ok("Deleted " + name + " (" + item_id + ").")


# ============================================================
#  THE RESTAURANT'S ORDERS
#  The rules come from SPEC-orders.md:
#    PLACED     the restaurant can accept it, or say no
#    ACCEPTED   the restaurant can still back out
#    PICKED_UP  too late, a rider is carrying it
#    DELIVERED  finished, nobody may touch it again
# ============================================================


def my_orders(username):
    """Return the IDs of every order placed at this restaurant."""
    orders = []

    for order_id in DATA["orders"]:
        if DATA["orders"][order_id]["restaurant"] == username:
            orders.append(order_id)

    return sorted(orders)


def orders_with_status(username, wanted):
    """Return this restaurant's orders that are in one of the given statuses.

    wanted is a list, so that "PLACED" and "ACCEPTED" can both be asked
    for in one call.
    """
    matching = []

    for order_id in my_orders(username):
        if DATA["orders"][order_id]["status"] in wanted:
            matching.append(order_id)

    return matching


def show_orders(order_ids):
    """Print a small table of orders, one row each."""
    rows = []

    for order_id in order_ids:
        order = DATA["orders"][order_id]
        customer = DATA["users"][order["customer"]]["name"]

        left = design.pad_right(order_id, 8) \
            + design.pad_right(customer, 20) \
            + order["status"]

        rows.append(design.columns(left, design.money(order["total"]), 44))

    design.box("Order ID    Customer            Status", rows)


def ask_order_id(username, action, allowed):
    """Show the orders this restaurant may act on, and ask for one.

    action is the word used in the question, like "accept".
    allowed is a list of the statuses we are allowed to act on.

    Returns the order ID, or None if nothing was chosen. The status is
    checked here, not at each action, so a DELIVERED order can never be
    reached by any of them.
    """
    open_orders = orders_with_status(username, allowed)

    if len(open_orders) == 0:
        design.warn("There is no order you can " + action + " right now.")
        print()
        return None

    show_orders(open_orders)

    print()
    order_id = input("Which order to " + action + "? ").upper()

    if order_id not in DATA["orders"]:
        design.warn("No order found with the ID " + order_id + ".")
        print()
        return None

    # the order exists, but it is not ours to touch. This one check
    # stops us reaching another restaurant's orders, and stops us
    # reaching a DELIVERED one, because those are never in open_orders.
    if order_id not in open_orders:
        design.warn("You cannot " + action + " that order.")
        print()
        return None

    return order_id


def accept_order(username):
    """Say yes to an order that was just placed."""
    design.heading("Accept an order")

    order_id = ask_order_id(username, "accept", ["PLACED"])

    if order_id is None:
        return

    order = DATA["orders"][order_id]
    order["status"] = "ACCEPTED"
    save_data()

    print()
    design.ok("Accepted " + order_id + ". A rider can now collect it.")
    design.line("It stays this way until a rider takes it.")


def reject_order(username):
    """Say no to an order that was just placed."""
    design.heading("Reject an order")

    order_id = ask_order_id(username, "reject", ["PLACED"])

    if order_id is None:
        return

    order = DATA["orders"][order_id]
    order["status"] = "CANCELLED"
    save_data()

    print()
    design.ok("Rejected " + order_id + ".")
    design.line("It is now CANCELLED, and it will not reach the customer.")


def cancel_order(username):
    """Back out of an order we had already accepted."""
    design.heading("Cancel an accepted order")

    order_id = ask_order_id(username, "cancel", ["PLACED", "ACCEPTED"])

    if order_id is None:
        return

    order = DATA["orders"][order_id]

    # if a rider had already picked this up, let them off the hook,
    # otherwise they would stay stuck as BUSY with no order to deliver
    if order["rider"] is not None:
        rider = DATA["riders"][order["rider"]]
        rider["status"] = "FREE"
        rider["order"] = None
        design.line("Rider " + rider["name"] + " has been freed up.")

    order["status"] = "CANCELLED"
    save_data()

    print()
    design.ok("Cancelled " + order_id + ".")


def order_history(username):
    """Show every order this restaurant has ever had."""
    design.heading("My orders")

    mine = my_orders(username)

    if len(mine) == 0:
        design.warn("You have not received any orders yet.")
        print()
        return

    show_orders(mine)

    print()
    design.line("Total orders received: " + str(len(mine)))
    print()


def restaurant_menu(username):
    """Keep showing the restaurant menu until they choose to leave."""
    restaurant_name = DATA["users"][username]["name"]

    while True:
        design.banner()
        design.ok(restaurant_name + " - restaurant")
        design.line("Signed in as " + restaurant_name)
        print()

        design.heading("What would you like to do?")
        design.options([
            "See my food",
            "Add a new food item",
            "Change a price",
            "Sold out / back in stock",
            "Delete a food item",
            "See my orders",
            "Accept an order",
            "Reject an order",
            "Cancel an accepted order",
        ])

        choice = input("Your choice: ")
        print()

        if choice == "1":
            show_my_food(username)
        elif choice == "2":
            add_food(username)
        elif choice == "3":
            change_price(username)
        elif choice == "4":
            toggle_available(username)
        elif choice == "5":
            delete_food(username)
        elif choice == "6":
            order_history(username)
        elif choice == "7":
            accept_order(username)
        elif choice == "8":
            reject_order(username)
        elif choice == "9":
            cancel_order(username)
        elif choice == "0":
            design.line("Leaving the restaurant menu.")
            print()
            return
        else:
            design.warn("Please choose a number from 0 to 9.")
            print()