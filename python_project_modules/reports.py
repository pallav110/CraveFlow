# This file holds the three reports the store owner can see.
#
# The owner can:
#   - see total sales
#   - see how many orders were cancelled, and how much money that cost
#   - see which food item sells the best
#
# IMPORTANT: nothing in this file ever changes an order. Reports only
# read the data. If a mistake happened in here, it must not be able to
# damage the thing being reported on.

import python_project_modules.design as design
from python_project_modules.data import DATA


def all_orders():
    """Return every order ID we have."""
    orders = []

    for order_id in DATA["orders"]:
        orders.append(order_id)

    return sorted(orders)


def orders_with_status(status):
    """Return every order ID that is in one given status."""
    matching = []

    for order_id in all_orders():
        if DATA["orders"][order_id]["status"] == status:
            matching.append(order_id)

    return matching


def sum_of_totals(order_ids):
    """Add up the stored total of each order we were given.

    We read order["total"] and never work it out again from the food
    prices. The total was worked out once, when the order was made,
    and it is only ever read after that.
    """
    amount = 0.0

    for order_id in order_ids:
        amount = amount + DATA["orders"][order_id]["total"]

    return round(amount, 2)


# ----------------------------------------------------------------
#  REPORT 1 - TOTAL SALES
# ----------------------------------------------------------------


def total_sales():
    """Work out the total money earned from delivered orders."""
    return sum_of_totals(orders_with_status("DELIVERED"))


# ----------------------------------------------------------------
#  REPORT 2 - CANCELLED ORDERS, AND WHAT THEY COST US
# ----------------------------------------------------------------


def cancelled_count():
    """How many orders were cancelled."""
    return len(orders_with_status("CANCELLED"))


def money_lost():
    """How much money the cancelled orders were worth.

    This is NOT subtracted from the sales figure. It is shown on its
    own line, because hiding it would hide a real problem.
    """
    return sum_of_totals(orders_with_status("CANCELLED"))


# ----------------------------------------------------------------
#  REPORT 3 - BEST SELLING ITEM
# ----------------------------------------------------------------


def best_seller():
    """Work out which food item has sold the most, and what it made.

    Only DELIVERED orders are counted. An order that was cancelled
    never sold anything, and one that is still on the way has not sold
    anything yet.

    We count using the quantities dictionary, NOT the items list.

    That is the one decision worth explaining. Look at this order:

        "items"       ["F101"]              what was ordered
        "quantities"  {"F101": 2}           how many of each

    F101 is written down only ONCE in the items list, even though two
    pizzas were ordered. So counting the items list would tell us one
    pizza was sold, when two actually left the kitchen. The quantities
    dictionary already has the real number, so we just read it.

    Returns a list of three things:

        [ the food's ID , times sold , money made ]

    For example ["F101", 5, 1250.00]. Returns None if nothing has been
    delivered yet, because then there is no best seller to name.
    """
    counts = {}

    # 1. add up how many of each item went out in a delivered order
    for order_id in orders_with_status("DELIVERED"):
        order = DATA["orders"][order_id]

        for item_id in order["quantities"]:
            how_many = order["quantities"][item_id]

            # .get means "give me this value if it is there, and if it
            # is not there give me 0 instead of stopping the program."
            already = counts.get(item_id, 0)
            counts[item_id] = already + how_many

    # 2. nothing was delivered, so there is no best seller
    if len(counts) == 0:
        return None

    # 3. walk through the counts and keep whichever is highest
    best_id = None
    best_count = 0

    for item_id in counts:
        if counts[item_id] > best_count:
            best_count = counts[item_id]
            best_id = item_id

    # 4. now work out how much money that one item brought in
    money = 0.0

    for order_id in orders_with_status("DELIVERED"):
        order = DATA["orders"][order_id]

        if best_id in order["quantities"]:
            how_many = order["quantities"][best_id]

            # the item might have been deleted from the menu after it
            # was sold, so check before we use its price
            item = DATA["food"].get(best_id)

            if item is not None:
                money = money + item["price"] * how_many

    return [best_id, best_count, round(money, 2)]


def owner_menu(username):
    """Keep showing the owner menu until they choose to leave.

    The owner is signed in once, and main.welcome() already says so.
    Nothing about the owner changes from one choice to the next, so
    there is nothing here that needs to be printed again.
    """

    while True:
        design.rule()

        design.heading("What would you like to see?")
        design.options([
            "Total sales",
            "Cancelled orders",
            "Best selling item",
            "Everything on one page",
        ])

        choice = input("Your choice: ")
        print()

        if choice == "1":
            show_sales()
        elif choice == "2":
            show_cancelled()
        elif choice == "3":
            show_best_seller()
        elif choice == "4":
            show_everything()
        elif choice == "0":
            design.line("Leaving the owner menu.")
            print()
            return
        else:
            design.warn("Please choose a number from 0 to 4.")
            print()


def show_sales():
    """Print the total sales report."""
    design.heading("Total sales")

    delivered = orders_with_status("DELIVERED")
    money = total_sales()

    design.box("Total sales", [
        "Orders delivered : " + str(len(delivered)),
        "Total sales      : " + design.money(money),
    ])

    design.line("Only DELIVERED orders are counted here.")
    print()

    return money


def show_cancelled():
    """Print the cancelled orders report."""
    design.heading("Cancelled orders")

    cancelled = orders_with_status("CANCELLED")
    lost = money_lost()

    lines = [
        "Cancelled orders : " + str(len(cancelled)),
        "Money lost       : " + design.money(lost),
    ]

    # show each cancelled order on its own row, so the owner can see
    # exactly which ones went wrong
    for order_id in cancelled:
        order = DATA["orders"][order_id]
        customer = DATA["users"][order["customer"]]["name"]
        lines.append("")
        lines.append(design.columns(order_id + "  -  " + customer,
                                    design.money(order["total"]), 32))

    design.box("Cancellations", lines)

    design.line("This is kept separate from sales, on purpose.")
    print()

    return lost


def show_best_seller():
    """Print the best selling item report."""
    design.heading("Best selling item")

    result = best_seller()

    if result is None:
        design.warn("Nothing has been delivered yet.")
        design.line("So there is no best selling item to show.")
        print()
        return

    item_id = result[0]
    count = result[1]
    money = result[2]

    # the item may have been taken off the menu since it was sold
    item = DATA["food"].get(item_id)

    if item is None:
        name = "(removed from menu)"
    else:
        name = item["name"]

    design.box("Best seller", [
        "Item        : " + name,
        "Food ID     : " + item_id,
        "Sold        : " + str(count) + " time(s)",
        "Money made  : " + design.money(money),
    ])

    print()

    return result


def show_everything():
    """Print all three reports on one page."""
    design.heading("All reports")
    print()

    show_sales()
    show_cancelled()
    show_best_seller()

    design.line("That is every report CraveFlow can produce.")
    print()