# This file holds everything a customer can do.
#
# A customer can:
#   - see every restaurant and what food is on sale
#   - place an order
#   - see the orders they have already placed
#   - cancel an order they have not collected yet
#
# A customer never sees food that has sold out, and never sees or
# touches another customer's orders.

import python_project_modules.design as design
from python_project_modules.data import DATA, save_data


def restaurants_with_food():
    """Return the usernames of every restaurant that still has food.

    We only want restaurants the customer can actually order from, so
    a restaurant whose kitchen is sold out is left out completely.
    """
    names = []

    for username in DATA["users"]:
        if DATA["users"][username]["role"] != "restaurant":
            continue

        for item_id in DATA["food"]:
            if DATA["food"][item_id]["restaurant"] == username:
                if DATA["food"][item_id]["available"]:
                    names.append(username)
                    break

    return names


def available_food(username):
    """Return the food IDs a restaurant is currently selling."""
    items = []

    for item_id in DATA["food"]:
        item = DATA["food"][item_id]

        if item["restaurant"] == username and item["available"]:
            items.append(item_id)

    return items


def food_line(item_id):
    """Turn one food item into a line of text for a box.

    The three columns are ID, name and price. design.columns lines
    them up, so every table in the program matches the others.
    """
    item = DATA["food"][item_id]
    name = design.pad_right(item["name"], 24) + item_id

    return design.columns(name, design.money(item["price"]), 32)


def browse(username):
    """Show every restaurant with the food it has on sale right now."""
    customer_name = DATA["users"][username]["name"]

    design.heading("Hello " + customer_name + ", what would you like?")

    places = restaurants_with_food()

    if len(places) == 0:
        design.warn("No restaurant has food available right now.")
        print()
        return []

    total_count = 0

    for place in places:
        items = available_food(place)
        place_name = DATA["users"][place]["name"]
        fee = DATA["users"][place]["fee"]

        design.box(place_name + "   -   delivery " + design.money(fee),
               [food_line(item_id) for item_id in items])

        total_count = total_count + len(items)

    design.line("Showing " + str(total_count) + " items from "
                + str(len(places)) + " restaurants.")
    print()

    return places


def show_food_of(place):
    """Show one restaurant's food on its own, for choosing an item."""
    items = available_food(place)
    place_name = DATA["users"][place]["name"]

    design.box(place_name, [food_line(item_id) for item_id in items])


def new_order_id():
    """Make a brand new order ID that is not being used yet.

    Same idea as new_food_id - count up until we find a free one, so
    a cancelled or deleted order can never make us repeat an ID.
    """
    number = len(DATA["orders"]) + 1001

    while ("O" + str(number)) in DATA["orders"]:
        number = number + 1

    return "O" + str(number)


def my_active_order(username):
    """Return the ID of an order this customer already has going.

    An order is still going if it is PLACED, ACCEPTED or PICKED_UP.
    Returns None if there is no such order.
    """
    for order_id in DATA["orders"]:
        order = DATA["orders"][order_id]

        if order["customer"] != username:
            continue

        if order["status"] == "PLACED":
            return order_id
        if order["status"] == "ACCEPTED":
            return order_id
        if order["status"] == "PICKED_UP":
            return order_id

    return None


def build_order(username, place, chosen):
    """Work out the bill for an order and save it.

    place is the restaurant's username.
    chosen is a dictionary like {"F101": 2, "F102": 1}

    Returns the new order ID, or None if we had to stop.
    """
    food_total = 0.0
    items = []
    quantities = {}

    for item_id in chosen:
        quantity = chosen[item_id]
        price = DATA["food"][item_id]["price"]

        food_total = food_total + price * quantity
        items.append(item_id)
        quantities[item_id] = quantity

    fee = DATA["users"][place]["fee"]
    total = round(food_total + fee, 2)

    order_id = new_order_id()

    DATA["orders"][order_id] = {
        "customer": username,
        "items": items,
        "quantities": quantities,
        "restaurant": place,
        "total": total,
        "status": "PLACED",
        "rider": None,
    }

    save_data()

    return order_id


def bill_lines(order_id):
    """Work out the lines that show one order's bill.

    Returns a list of text lines, one per row. The order screen and the
    receipt both use this, so the two can never disagree about the bill.

    The food total is worked out from the prices again here, because it
    is only a display. The amount the customer actually paid is the
    stored total, and we never change that.
    """
    order = DATA["orders"][order_id]
    lines = []
    food_total = 0.0

    for item_id in order["items"]:
        item = DATA["food"].get(item_id)
        quantity = order["quantities"][item_id]

        # the item may have been deleted from the menu since, so if it
        # is gone we show the ID alone instead of crashing
        if item is None:
            lines.append(design.columns(item_id + "  (removed from menu)",
                                        "x" + str(quantity), 32))
            continue

        amount = item["price"] * quantity
        food_total = food_total + amount

        left = design.pad_right(item["name"], 24) + "  x" + str(quantity)
        lines.append(design.columns(left, design.money(amount), 32))

    fee = DATA["users"][order["restaurant"]]["fee"]

    lines.append("")
    lines.append(design.columns("Food total", design.money(food_total), 32))
    lines.append(design.columns("Delivery fee", design.money(fee), 32))
    lines.append(design.columns("To pay", design.money(order["total"]), 32))

    return lines


def show_order(order_id):
    """Print one order nicely, with its items and its bill."""
    order = DATA["orders"][order_id]
    place_name = DATA["users"][order["restaurant"]]["name"]

    design.box("Order " + order_id + "   [" + order["status"] + "]",
               bill_lines(order_id))

    design.line("Ordered from " + place_name
                + "   -   delivered to "
                + DATA["users"][order["customer"]]["name"])

    if order["rider"] is not None:
        rider = DATA["users"][order["rider"]]["name"]
        design.line("Rider: " + rider)

    print()


def show_receipt(order_id):
    """Print the receipt for an order that has just been delivered.

    This is the thank you. It says who it was for, who brought it, and
    exactly what they paid for.
    """
    order = DATA["orders"][order_id]
    customer_name = DATA["users"][order["customer"]]["name"]
    place_name = DATA["users"][order["restaurant"]]["name"]

    if order["rider"] is None:
        rider_name = "None"
    else:
        rider_name = DATA["users"][order["rider"]]["name"]

    print()
    design.ok("Thank you for ordering with CraveFlow.")
    print()

    design.box("Receipt   " + order_id, [
        "Billed to    : " + customer_name,
        "Kitchen      : " + place_name,
        "Delivered by : " + rider_name,
        "",
    ] + bill_lines(order_id))

    print()
    design.line("Your food has arrived. Enjoy your meal.")
    print()


def my_orders(username):
    """Show this customer's own orders, newest ID last."""
    mine = []

    for order_id in DATA["orders"]:
        if DATA["orders"][order_id]["customer"] == username:
            mine.append(order_id)

    if len(mine) == 0:
        design.heading("My orders")
        design.warn("You have not placed any orders yet.")
        print()
        return

    design.heading("My orders")

    for order_id in sorted(mine):
        order = DATA["orders"][order_id]
        count = len(order["items"])
        design.ok(order_id + "  [" + order["status"] + "]  -  "
                  + design.money(order["total"])
                  + "  -  " + str(count) + " item(s)")
        show_order(order_id)


def place_order(username):
    """Ask what the customer wants, and create the order.

    There are four checks we must get past before an order is made:
      1. they must pick at least one thing
      2. everything must come from one restaurant
      3. nothing they picked may have sold out since they looked
      4. they cannot already have an order on the way
    """
    design.heading("Place a new order")

    busy = my_active_order(username)

    if busy is not None:
        design.warn("You already have order " + busy
                    + " on the way.")
        design.line("Please wait for it, or cancel it, before ordering again.")
        print()
        return

    places = browse(username)

    if len(places) == 0:
        return

    while True:
        number = 1
        for place in places:
            design.line("  " + str(number) + ". "
                        + DATA["users"][place]["name"])
            number = number + 1

        print()
        choice = input("Which restaurant? (0 to go back): ")

        if choice == "0":
            return

        if not choice.isdigit():
            design.warn("Please type a number.")
            print()
            continue

        position = int(choice)

        if position < 1 or position > len(places):
            design.warn("There is no restaurant number " + choice + ".")
            print()
            continue

        break

    place = places[position - 1]
    show_food_of(place)

    chosen = {}

    while True:
        print()
        design.line("Type the food ID and how many, for example F101 2")
        design.line("Type 0 on its own when you are done.")

        answer = input("Food: ")

        if answer == "0":
            break

        parts = answer.split()

        if len(parts) != 2:
            design.warn("Type an ID and a number, like F101 2")
            print()
            continue

        item_id = parts[0].upper()
        quantity_text = parts[1]

        if item_id not in DATA["food"]:
            design.warn("There is no food item with the ID " + item_id + ".")
            print()
            continue

        if not quantity_text.isdigit():
            design.warn("The number must be 1 or more.")
            print()
            continue

        quantity = int(quantity_text)

        if quantity < 1:
            design.warn("The number must be 1 or more.")
            print()
            continue

        item = DATA["food"][item_id]

        if item["restaurant"] != place:
            design.warn(item["name"] + " is from a different restaurant.")
            print()
            continue

        if not item["available"]:
            design.warn(item["name"]
                        + " is sold out, so it cannot be ordered.")
            print()
            continue

        # if they already asked for this one, add to it instead of
        # throwing the first number away
        if item_id in chosen:
            chosen[item_id] = chosen[item_id] + quantity
        else:
            chosen[item_id] = quantity

    if len(chosen) == 0:
        design.warn("Nothing was selected, so no order was made.")
        print()
        return

    order_id = build_order(username, place, chosen)

    print()
    design.ok("Order placed! Your order ID is " + order_id + ".")
    print()
    show_order(order_id)


def cancel_order(username):
    """Cancel one of this customer's orders, if it is still allowed."""
    design.heading("Cancel an order")

    mine = []

    for order_id in DATA["orders"]:
        order = DATA["orders"][order_id]

        if order["customer"] != username:
            continue

        if order["status"] == "PLACED":
            mine.append(order_id)
        elif order["status"] == "ACCEPTED":
            mine.append(order_id)

    if len(mine) == 0:
        design.warn("You have no order that can be cancelled.")
        design.line("An order can be cancelled until a rider collects it.")
        print()
        return

    for order_id in mine:
        order = DATA["orders"][order_id]
        design.ok(order_id + "  -  " + design.money(order["total"])
                  + "  -  " + order["status"])

    print()
    order_id = input("Which order ID? ").upper()

    if order_id not in mine:
        design.warn("That order cannot be cancelled.")
        print()
        return

    order = DATA["orders"][order_id]

    if order["rider"] is not None:
        design.warn("A rider is already carrying that order.")
        print()
        return

    order["status"] = "CANCELLED"
    save_data()

    print()
    design.ok("Order " + order_id + " has been cancelled.")


def customer_menu(username):
    """Keep showing the customer menu until they choose to leave."""
    customer_name = DATA["users"][username]["name"]

    while True:
        design.banner()
        design.ok(customer_name + " - customer")
        design.line("Signed in as " + username)
        print()

        active = my_active_order(username)

        if active is not None:
            design.line("You have an order on the way: " + active)
            print()

        design.heading("What would you like to do?")
        design.options([
            "See all food",
            "Place a new order",
            "My orders",
            "Cancel an order",
        ])

        choice = input("Your choice: ")
        print()

        if choice == "1":
            browse(username)
        elif choice == "2":
            place_order(username)
        elif choice == "3":
            my_orders(username)
        elif choice == "4":
            cancel_order(username)
        elif choice == "0":
            design.line("Leaving the customer menu.")
            print()
            return
        else:
            design.warn("Please choose a number from 0 to 4.")
            print()