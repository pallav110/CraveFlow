# All of CraveFlow's data lives in one dictionary, called DATA.
# It has four parts, and each part holds more dictionaries:
#
#   DATA["users"]    -> every person, and whether they are a
#                       customer, a restaurant, a rider or the owner
#   DATA["food"]     -> every food item, and what it costs
#   DATA["orders"]   -> every order someone has placed
#   DATA["riders"]   -> every rider, and whether they are free or busy
#
# We build it inside a function so we can make a fresh copy any time
# we want to go back to the starting point.


def make_data():
    """Build the dictionary, already filled with demo examples."""

    data = {}

    # ---- The people -----------------------------------------------

    data["users"] = {}

    data["users"]["yajat"] = {
        "name": "Yajat Sharma",
        "role": "customer",
        "password": "1234",
    }

    data["users"]["dominoes"] = {
        "name": "Domino's Pizza",
        "role": "restaurant",
        "password": "1234",
        "fee": 40.00,
    }

    data["users"]["tandoor"] = {
        "name": "Tandoor House",
        "role": "restaurant",
        "password": "1234",
        "fee": 25.00,
    }

    data["users"]["raj"] = {
        "name": "Raj Kumar",
        "role": "rider",
        "password": "1234",
    }

    data["users"]["meera"] = {
        "name": "Meera Singh",
        "role": "rider",
        "password": "1234",
    }

    data["users"]["owner"] = {
        "name": "Store Owner",
        "role": "owner",
        "password": "1234",
    }

    # ---- The food -------------------------------------------------
    # "available" is True or False. False means it has sold out, so the
    # customer will not see it, but the restaurant can still see it.

    data["food"] = {}

    data["food"]["F101"] = {
        "name": "Margherita Pizza",
        "price": 250.00,
        "restaurant": "dominoes",
        "available": True,
    }

    data["food"]["F102"] = {
        "name": "Garlic Bread",
        "price": 120.00,
        "restaurant": "dominoes",
        "available": True,
    }

    data["food"]["F103"] = {
        "name": "Cold Drink",
        "price": 60.00,
        "restaurant": "dominoes",
        "available": False,
    }

    data["food"]["F201"] = {
        "name": "Butter Chicken",
        "price": 280.00,
        "restaurant": "tandoor",
        "available": True,
    }

    data["food"]["F202"] = {
        "name": "Paneer Tikka",
        "price": 220.00,
        "restaurant": "tandoor",
        "available": True,
    }

    # ---- The orders -----------------------------------------------
    # status can only ever be one of these five words:
    #   PLACED     the customer just ordered
    #   ACCEPTED   the restaurant said yes
    #   PICKED_UP  a rider has collected it
    #   DELIVERED  it reached the customer
    #   CANCELLED  it will not happen

    data["orders"] = {}

    # 2 x Margherita (250) + 1 x Garlic Bread (120) = 620
    # 620 + Domino's fee of 40 = 660
    data["orders"]["O1001"] = {
        "customer": "yajat",
        "items": ["F101", "F102"],
        "quantities": {"F101": 2, "F102": 1},
        "restaurant": "dominoes",
        "total": 660.00,
        "status": "DELIVERED",
        "rider": "raj",
    }

    # 1 x Butter Chicken (280) + Tandoor's fee of 25 = 305
    data["orders"]["O1002"] = {
        "customer": "yajat",
        "items": ["F201"],
        "quantities": {"F201": 1},
        "restaurant": "tandoor",
        "total": 305.00,
        "status": "ACCEPTED",
        "rider": None,
    }

    # 1 x Paneer Tikka (220) + Tandoor's fee of 25 = 245
    data["orders"]["O1003"] = {
        "customer": "yajat",
        "items": ["F202"],
        "quantities": {"F202": 1},
        "restaurant": "tandoor",
        "total": 245.00,
        "status": "CANCELLED",
        "rider": None,
    }

    # ---- The riders -----------------------------------------------
    # status is FREE or BUSY. This is the lock that stops one rider
    # picking up two orders at the same time.

    data["riders"] = {}

    data["riders"]["raj"] = {
        "name": "Raj Kumar",
        "status": "FREE",
        "order": None,
    }

    data["riders"]["meera"] = {
        "name": "Meera Singh",
        "status": "FREE",
        "order": None,
    }

    return data


# This is the one dictionary every other file uses.
DATA = make_data()


def show_data():
    """Print the whole dictionary, so we can see what is inside it."""
    print(DATA)


# ====================================================================
#  EXTENSION - SAVING THE DATA SO IT SURVIVES AFTER THE PROGRAM CLOSES
# ====================================================================
#
#  Everything ABOVE this line is the main part of the project.
#  Everything BELOW this line is an extra, and the program will still
#  work perfectly well if we delete all of it.
#
#  What this part adds:
#    When the program closes, the dictionary is written into a file
#    called data.json. The next time the program starts, it reads that
#    file instead of starting fresh. So the food we add stays added.
#
#  Three new things are used here, and only here:
#
#    1. "import json"  - a ready-made helper that Python already has,
#                        for turning a dictionary into text and back.
#
#    2. "open(name, r)" - opens a file so we can read from it.
#                        "r" means read. We use "w" to write instead.
#                        "f" is the handle we use to refer to the file.
#                        "f.close()" shuts it when we are finished.
#
#    3. "os.path.exists(name)" - asks the yes or no question
#                         "is this file already there?"
#
#  Viva answer, if asked:
#    "I used the json module to save my dictionary into a file, and
#     json.load to read it back the next time the program starts."

import json
import os

DATA_FILE = "output_data/data.json"


def data_path():
    """Work out exactly where the data file is.

    We do not just write "data.json", because that saves the file in
    whatever folder the program happens to be run from. If a teacher
    double clicks main.py from a different place, the data would be
    saved somewhere else and look lost.

    __file__ is the folder this data.py file is sitting in. We use it
    to build a full path, so the file is always found in the same
    place, no matter where the program was started from.

    os.path.join glues pieces of a path together with the right
    separator for the computer.
    """
    here = os.path.dirname(__file__)
    return os.path.join(here, "..", "output_data", "data.json")


def save_data():
    """Write the whole dictionary into the file as JSON."""
    full_path = data_path()

    # make the output_data folder if it is not there yet, otherwise
    # saving would stop with an error
    folder = os.path.dirname(full_path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    file = open(full_path, "w")
    json.dump(DATA, file, indent=2)
    file.close()


def load_data():
    """Read the dictionary back out of the file."""
    file = open(data_path(), "r")
    data = json.load(file)
    file.close()
    return data


def start_data():
    """Use the saved file if it is there, otherwise make a fresh start.

    A brand new computer has no data.json yet. Without this check the
    program would stop before the menu even appears.
    """
    if os.path.exists(data_path()):
        return load_data()

    save_data()
    return DATA


# Now read the saved data, so every file that imports DATA gets the
# version from the file rather than the fresh one.
DATA = start_data()


# To wipe everything and start over from the demo examples, delete the
# file output_data/data.json, or run this once by hand:
#
#     import data
#     import os
#     os.remove("output_data/data.json")