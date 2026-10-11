# CraveFlow - Food Delivery Management System
# This file starts the program. It asks who you are, and then opens the
# right menu for that person.

import python_project_modules.data as data
import python_project_modules.design as design
import python_project_modules.restaurant as restaurant
import python_project_modules.customer as customer
import python_project_modules.rider as rider
import python_project_modules.reports as reports
from python_project_modules.data import DATA, save_data


def login():
    """Ask for a username and password until we get in, or the user quits.

    Returns the username if they got in, and None if they typed exit.
    """
    while True:
        design.banner()
        design.heading("Please sign in")

        username = input("Username: ")

        # typing exit leaves the program. We check this before asking
        # for a password, because someone who wants to leave should not
        # be stopped by a question they have no reason to answer.
        if username == "exit":
            return None

        password = input("Password: ")

        # is that username in our list of people at all?
        if username not in DATA["users"]:
            design.warn("No account found with that username.")
            print()

        # the username is real, so now check the password
        elif password != DATA["users"][username]["password"]:
            design.warn("Wrong password.")
            print()

        # both are correct, so we are in
        else:
            return username


def welcome(username):
    """Say hello, and show which menu they are about to get."""
    person = DATA["users"][username]

    design.banner()
    design.ok("Signed in as " + person["name"])
    print()
    design.line("Role: " + person["role"])
    print()


def customer_menu(username):
    customer.customer_menu(username)


def restaurant_menu(username):
    restaurant.restaurant_menu(username)


def rider_menu(username):
    rider.rider_menu(username)


def owner_menu(username):
    reports.owner_menu(username)


def open_menu(username):
    """Send the user to the menu that matches their role."""
    role = DATA["users"][username]["role"]

    if role == "customer":
        customer_menu(username)
    elif role == "restaurant":
        restaurant_menu(username)
    elif role == "rider":
        rider_menu(username)
    else:
        owner_menu(username)


def run():
    """Keep signing in and out until the user quits."""
    while True:
        username = login()

        # login returns None when they type exit
        if username is None:
            design.banner()
            design.line("Thank you for using CraveFlow.")
            print()
            break

        welcome(username)
        open_menu(username)

        # they are signing out now, so save whatever they changed
        save_data()

        design.banner()
        design.line("You have been signed out.")
        print()


run()