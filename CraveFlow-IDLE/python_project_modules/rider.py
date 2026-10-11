# This file holds everything a rider can do.
#
# A rider can:
#   - see the orders waiting for someone to collect them
#   - claim one, which locks them to that single order
#   - mark it picked up
#   - mark it delivered, which frees them up again
#   - cancel an order they are holding, which also frees them up
#
# The lock is the whole point of this file. Each rider is either
# FREE or BUSY. A BUSY rider cannot claim a second order, because a
# rider can only carry one thing at a time.

import python_project_modules.design as design
import python_project_modules.customer as customer
from python_project_modules.data import DATA, save_data


def my_lock(username):
    """Return this rider's own record from DATA["riders"]."""
    return DATA["riders"][username]


def open_orders():
    """Return the orders that are waiting for a rider to collect them.

    An order is waiting when the restaurant has accepted it and no
    rider has taken it yet. That is status ACCEPTED and rider None.
    """
    waiting = []

    for order_id in DATA["orders"]:
        order = DATA["orders"][order_id]

        if order["status"] == "ACCEPTED" and order["rider"] is None:
            waiting.append(order_id)

    return sorted(waiting)


def order_line(order_id):
    """Turn one order into a line of text for a box."""
    order = DATA["orders"][order_id]
    place = DATA["users"][order["restaurant"]]["name"]

    # build a short description of what is inside, like "2x Margherita"
    parts = []
    for item_id in order["items"]:
        name = DATA["food"][item_id]["name"]
        parts.append(str(order["quantities"][item_id]) + "x " + name)

    left = design.pad_right(order_id, 8) + design.pad_right(place, 18)
    left = left + design.pad_right(", ".join(parts), 24)

    return design.columns(left, design.money(order["total"]), 52)


def show_open_orders():
    """Show every order a rider is allowed to claim."""
    waiting = open_orders()

    if len(waiting) == 0:
        design.heading("Orders waiting")
        design.warn("No orders are waiting for a rider right now.")
        print()
        return []

    design.heading("Orders waiting for collection")
    design.box("Order    Restaurant", [order_line(o) for o in waiting])
    design.line("Total waiting: " + str(len(waiting)))
    print()

    return waiting


def ask_order_id(waiting, action):
    """Ask which of the waiting orders we mean. Returns None if refused."""
    if len(waiting) == 0:
        design.warn("There is no order you can " + action + " right now.")
        print()
        return None

    order_id = input("Which order to " + action + "? ").upper()

    if order_id not in waiting:
        design.warn("That order is not waiting to be collected.")
        print()
        return None

    return order_id


def claim_order(username):
    """Take an order, and become BUSY holding it.

    The four checks below are the whole lock. They are in this order
    on purpose, so that a rider who is already busy is told the real
    reason rather than a confusing one.
    """
    design.heading("Claim an order")

    # 1. is the order there at all?
    waiting = open_orders()

    if len(waiting) == 0:
        design.warn("No orders are waiting for a rider right now.")
        print()
        return

    order_id = ask_order_id(waiting, "claim")

    if order_id is None:
        return

    # 2. is this rider free? If not, they cannot take anything.
    rider = my_lock(username)

    if rider["status"] != "FREE":
        design.warn("You are already delivering order "
                    + str(rider["order"]) + ".")
        design.line("Finish or cancel that one before claiming another.")
        print()
        return

    # 3. stamp the order with this rider, and lock them to it
    order = DATA["orders"][order_id]
    order["rider"] = username

    # 4. and now the rider is busy with exactly this one order
    rider["order"] = order_id
    rider["status"] = "BUSY"

    save_data()

    print()
    design.ok("You claimed " + order_id + ". You are now BUSY.")
    design.line("Mark it picked up when you have collected it.")


def my_current_order(username):
    """Return the ID of the order this rider is holding, or None."""
    rider = my_lock(username)

    if rider["status"] != "BUSY":
        return None

    return rider["order"]


def pick_up(username):
    """Say we have collected the food."""
    design.heading("Mark picked up")

    order_id = my_current_order(username)

    if order_id is None:
        design.warn("You are not carrying any order.")
        design.line("Claim an order first, then you can mark it picked up.")
        print()
        return

    order = DATA["orders"][order_id]

    # the order must still be ACCEPTED. It cannot jump straight from
    # claimed to delivered, because PICKED_UP is the step that proves
    # the food actually moved.
    if order["status"] != "ACCEPTED":
        design.warn("Order " + order_id + " is not ACCEPTED any more.")
        print()
        return

    order["status"] = "PICKED_UP"
    save_data()

    print()
    design.ok("Order " + order_id + " is now PICKED_UP.")
    design.line("Deliver it, then mark it delivered.")


def deliver(username):
    """Say the food has reached the customer, and free the rider up."""
    design.heading("Mark delivered")

    order_id = my_current_order(username)

    if order_id is None:
        design.warn("You are not carrying any order.")
        print()
        return

    order = DATA["orders"][order_id]

    # an order has to pass through PICKED_UP before it can be
    # delivered, so this refuses if they skipped that step
    if order["status"] != "PICKED_UP":
        design.warn("Order " + order_id + " has not been picked up yet.")
        design.line("Mark it picked up before marking it delivered.")
        print()
        return

    order["status"] = "DELIVERED"

    # the rider's lock is released, so they can claim another order
    rider = my_lock(username)
    rider["status"] = "FREE"
    rider["order"] = None

    save_data()

    print()
    design.ok("Order " + order_id + " is now DELIVERED.")
    design.line("You are FREE again. Thank you.")

    # the order has arrived, so this is the moment the customer gets
    # their receipt
    customer.show_receipt(order_id)


def cancel_order(username):
    """Cancel the order we are carrying, and free the rider up."""
    design.heading("Cancel the order you are carrying")

    order_id = my_current_order(username)

    if order_id is None:
        design.warn("You are not carrying any order.")
        print()
        return

    order = DATA["orders"][order_id]

    # a delivered order is final, nobody may change it
    if order["status"] == "DELIVERED":
        design.warn("Order " + order_id + " is already delivered.")
        design.line("A delivered order cannot be changed.")
        print()
        return

    order["status"] = "CANCELLED"

    # the lock is released, so the rider is not stuck as BUSY with
    # nothing to deliver
    rider = my_lock(username)
    rider["status"] = "FREE"
    rider["order"] = None

    save_data()

    print()
    design.ok("Order " + order_id + " has been cancelled.")
    design.line("You are FREE again.")


def my_status(username):
    """Show whether this rider is free or busy, and with what."""
    design.heading("My status")

    rider = my_lock(username)
    name = rider["name"]

    if rider["status"] == "FREE":
        design.ok(name + " is FREE.")
        design.line("You can claim any order that is waiting.")
    else:
        order_id = rider["order"]
        order = DATA["orders"][order_id]
        customer = DATA["users"][order["customer"]]["name"]

        design.warn(name + " is BUSY with " + order_id + ".")
        design.line("Status of that order: " + order["status"])
        design.line("Delivering to " + customer + "  -  "
                    + design.money(order["total"]))

    print()


def rider_menu(username):
    """Keep showing the rider menu until they choose to leave.

    The rider's name is printed once, by main.welcome(), at the moment
    they sign in.

    Whether the rider is FREE or BUSY is the one thing here that really
    changes, so it is worth showing. It is printed only when it has
    actually changed, which means a rider idly browsing the menu does
    not push their own answer down the screen over and over.
    """
    last_status = ""

    while True:
        design.rule()

        lock = my_lock(username)

        if lock["status"] == "FREE":
            status = "You are FREE. You can claim a waiting order."
        else:
            status = "You are BUSY carrying " + str(lock["order"]) + "."

        if status != last_status:
            design.line(status)
            print()
            last_status = status

        design.heading("What would you like to do?")
        design.options([
            "See orders waiting",
            "Claim an order",
            "Mark picked up",
            "Mark delivered",
            "Cancel the order I am carrying",
            "My status",
        ])

        choice = input("Your choice: ")
        print()

        if choice == "1":
            show_open_orders()
        elif choice == "2":
            claim_order(username)
        elif choice == "3":
            pick_up(username)
        elif choice == "4":
            deliver(username)
        elif choice == "5":
            cancel_order(username)
        elif choice == "6":
            my_status(username)
        elif choice == "0":
            design.line("Leaving the rider menu.")
            print()
            return
        else:
            design.warn("Please choose a number from 0 to 6.")
            print()