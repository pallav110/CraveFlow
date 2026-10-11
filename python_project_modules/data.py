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

    # Two small helpers live inside this function. They only exist while
    # we are building the demo data, and they save us writing the same
    # six lines over and over for every kitchen and every dish.
    #
    # Viva answer, if asked:
    #   "I wrote two small functions inside make_data() so that adding
    #    a restaurant or a dish takes one line instead of six. They
    #    put the values into the dictionary for me."

    def add_place(username, name, genre, fee):
        """Put one restaurant into the users dictionary."""
        data["users"][username] = {
            "name": name,
            "role": "restaurant",
            "password": "1234",
            "genre": genre,
            "fee": fee,
        }

    def add_food(item_id, name, price, restaurant, available=True):
        """Put one dish into the food dictionary."""
        data["food"][item_id] = {
            "name": name,
            "price": price,
            "restaurant": restaurant,
            "available": available,
        }

    # ---- The people -----------------------------------------------

    data["users"] = {}

    data["users"]["yajat"] = {
        "name": "Yajat Sharma",
        "role": "customer",
        "password": "1234",
    }

    # ---- The restaurants ------------------------------------------
    # "genre" is the kind of food the kitchen cooks. It is only a label,
    # but it lets the customer browse by style instead of by alphabet.
    # "fee" is what that kitchen charges for delivery, and it is added
    # to the bill once, at the end, whatever is ordered.

    # North Indian
    add_place("tandoor", "Tandoor House", "North Indian", 25.00)
    add_place("punjabi", "Punjabi Darbar", "North Indian", 30.00)
    add_place("old_delhi", "Old Delhi Waqf", "North Indian", 20.00)
    add_place("curry_pot", "Curries and Pots", "North Indian", 35.00)

    # South Indian
    add_place("madras", "Madras Cafe", "South Indian", 20.00)
    add_place("udupi", "Udupi Bhavan", "South Indian", 22.00)
    add_place("andhra", "Andhra Spice", "South Indian", 28.00)
    add_place("kerala", "Kerala Kitchen", "South Indian", 32.00)

    # Biryani and thalis
    add_place("biryani_adda", "Biryani Adda", "Biryani and Thalis", 35.00)
    add_place("thali_house", "Thali House", "Biryani and Thalis", 40.00)

    # Snacks and street food
    add_place("chaat", "Chaat Junction", "Snacks and Street Food", 15.00)
    add_place("momo_house", "Momo House", "Snacks and Street Food", 20.00)
    add_place("rollwala", "Rollwala", "Snacks and Street Food", 18.00)
    add_place("halidirams", "Haldiram's", "Snacks and Street Food", 12.00)

    # Tea and drinks
    add_place("chai_point", "Chai Point", "Tea and Beverages", 10.00)
    add_place("coffee_day", "Coffee Day", "Tea and Beverages", 15.00)
    add_place("juice_factory", "Juice Factory", "Tea and Beverages", 20.00)
    add_place("bubble_blast", "Bubble Blast", "Tea and Beverages", 25.00)

    # Sweets
    add_place("sweet_house", "Sweet House", "Sweets and Desserts", 15.00)
    add_place("baker_street", "Baker Street", "Sweets and Desserts", 20.00)
    add_place("kulfi_corner", "Kulfi Corner", "Sweets and Desserts", 18.00)

    # Italian - pizza and pasta
    add_place("dominoes", "Domino's Pizza", "Pizza and Pasta", 40.00)
    add_place("pizza_hut", "Pizza Hut", "Pizza and Pasta", 45.00)
    add_place("la_pinos", "La Pino's", "Pizza and Pasta", 35.00)
    add_place("pasta_fresco", "Pasta Fresco", "Pizza and Pasta", 40.00)
    add_place("pizza_square", "Pizza Square", "Pizza and Pasta", 30.00)

    # Burgers and sandwiches
    add_place("burger_king", "Burger King", "Burgers and Sandwiches", 35.00)
    add_place("subway", "Subway", "Burgers and Sandwiches", 30.00)
    add_place("grill_master", "Grill Master", "Burgers and Sandwiches", 25.00)

    # ---- The riders and the owner ---------------------------------

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
    # A dish name has to stay under 25 letters, or it will not fit in
    # the table when it is printed.

    data["food"] = {}

    # North Indian

    add_food("F201", "Butter Chicken", 280.00, "tandoor")
    add_food("F202", "Paneer Tikka", 220.00, "tandoor")
    add_food("F203", "Dal Makhani", 190.00, "tandoor")
    add_food("F204", "Chicken Korma", 310.00, "tandoor")
    add_food("F205", "Tandoori Roti", 45.00, "tandoor", False)

    add_food("F301", "Sarson Da Saag", 180.00, "punjabi")
    add_food("F302", "Kadhai Paneer", 240.00, "punjabi")
    add_food("F303", "Chicken Tikka", 320.00, "punjabi")
    add_food("F304", "Paneer Tikka Plate", 260.00, "punjabi")
    add_food("F305", "Sweet Lassi", 80.00, "punjabi")

    add_food("F311", "Chole Bhature", 150.00, "old_delhi")
    add_food("F312", "Rajma Chawal", 130.00, "old_delhi")
    add_food("F313", "Paratha Platter", 110.00, "old_delhi")
    add_food("F314", "Butter Naan", 55.00, "old_delhi")
    add_food("F315", "Gulab Jamun", 60.00, "old_delhi")

    add_food("F321", "Butter Chicken", 290.00, "curry_pot")
    add_food("F322", "Malai Kofta", 230.00, "curry_pot")
    add_food("F323", "Egg Curry", 210.00, "curry_pot")
    add_food("F324", "Paneer Butter Masala", 250.00, "curry_pot")
    add_food("F325", "Garlic Naan", 50.00, "curry_pot")

    # South Indian

    add_food("F401", "Idli Sambar", 90.00, "madras")
    add_food("F402", "Plain Dosa", 110.00, "madras")
    add_food("F403", "Masala Dosa", 140.00, "madras")
    add_food("F404", "Filter Coffee", 50.00, "madras")
    add_food("F405", "Vada Sambar", 80.00, "madras")

    add_food("F411", "Ghee Roast Dosa", 160.00, "udupi")
    add_food("F412", "Mangalorean Fish", 340.00, "udupi")
    add_food("F413", "Konkani Chicken", 300.00, "udupi")
    add_food("F414", "Podi Idli", 120.00, "udupi")
    add_food("F415", "Buttermilk", 40.00, "udupi")

    add_food("F421", "Andhra Chicken Biryani", 260.00, "andhra")
    add_food("F422", "Ghee Roast Dosa", 150.00, "andhra")
    add_food("F423", "Mutton Rogan Josh", 380.00, "andhra")
    add_food("F424", "Pulihora Rice", 180.00, "andhra")
    add_food("F425", "Coconut Chutney", 30.00, "andhra")

    add_food("F431", "Kerala Fish Curry", 340.00, "kerala")
    add_food("F432", "Appam with Stew", 220.00, "kerala")
    add_food("F433", "Chicken Sukka", 300.00, "kerala")
    add_food("F434", "Sadhya Plate", 450.00, "kerala")
    add_food("F435", "Payasam", 110.00, "kerala")

    # Biryani and thalis

    add_food("F501", "Chicken Dum Biryani", 320.00, "biryani_adda")
    add_food("F502", "Mutton Biryani", 420.00, "biryani_adda")
    add_food("F503", "Veg Dum Biryani", 280.00, "biryani_adda")
    add_food("F504", "Raita", 50.00, "biryani_adda")
    add_food("F505", "Gulab Jamun", 60.00, "biryani_adda")

    add_food("F511", "Veg Thali", 220.00, "thali_house")
    add_food("F512", "Non Veg Thali", 340.00, "thali_house")
    add_food("F513", "Paneer Thali", 260.00, "thali_house")
    add_food("F514", "Dal Rice", 120.00, "thali_house")
    add_food("F515", "Sweet", 40.00, "thali_house")

    # Snacks and street food

    add_food("F601", "Golgappa", 60.00, "chaat")
    add_food("F602", "Papdi Chaat", 80.00, "chaat")
    add_food("F603", "Dahi Bhalla", 90.00, "chaat")
    add_food("F604", "Aloo Tikki", 70.00, "chaat")
    add_food("F605", "Pani Puri", 50.00, "chaat")

    add_food("F611", "Steamed Momo", 70.00, "momo_house")
    add_food("F612", "Fried Momo", 90.00, "momo_house")
    add_food("F613", "Chilli Garlic Momo", 110.00, "momo_house")
    add_food("F614", "Momo Soup", 60.00, "momo_house")
    add_food("F615", "Chilli Momo", 120.00, "momo_house", False)

    add_food("F621", "Chicken Roll", 100.00, "rollwala")
    add_food("F622", "Paneer Roll", 90.00, "rollwala")
    add_food("F623", "Egg Roll", 70.00, "rollwala")
    add_food("F624", "Masala Maggi", 60.00, "rollwala")
    add_food("F625", "Chicken Cheese Roll", 140.00, "rollwala")

    add_food("F631", "Aloo Bhujia", 40.00, "halidirams")
    add_food("F632", "Bikaneri Bhalla", 60.00, "halidirams")
    add_food("F633", "Samosa", 50.00, "halidirams")
    add_food("F634", "Poha Chunks", 45.00, "halidirams")
    add_food("F635", "Laddoo", 70.00, "halidirams")

    # Tea and beverages

    add_food("F701", "Masala Chai", 25.00, "chai_point")
    add_food("F702", "Kadak Chai", 30.00, "chai_point")
    add_food("F703", "Chai Biscuit", 20.00, "chai_point")
    add_food("F704", "Samosa With Chutney", 40.00, "chai_point")
    add_food("F705", "Lemon Iced Tea", 60.00, "chai_point")

    add_food("F711", "Cappuccino", 140.00, "coffee_day")
    add_food("F712", "Cold Coffee", 160.00, "coffee_day")
    add_food("F713", "Cafe Latte", 130.00, "coffee_day")
    add_food("F714", "Thick Shake", 180.00, "coffee_day")
    add_food("F715", "Blueberry Muffin", 80.00, "coffee_day")

    add_food("F721", "Fresh Lime Soda", 80.00, "juice_factory")
    add_food("F722", "Watermelon Juice", 90.00, "juice_factory")
    add_food("F723", "Orange Juice", 110.00, "juice_factory")
    add_food("F724", "Mixed Fruit Juice", 120.00, "juice_factory")
    add_food("F725", "Green Tea", 50.00, "juice_factory")

    add_food("F731", "Classic Milk Tea", 90.00, "bubble_blast")
    add_food("F732", "Taro Milk Tea", 110.00, "bubble_blast")
    add_food("F733", "Matcha Latte", 130.00, "bubble_blast")
    add_food("F734", "Mango Ice Blast", 120.00, "bubble_blast")
    add_food("F735", "Cheese Foam Tea", 140.00, "bubble_blast")

    # Sweets and desserts

    add_food("F801", "Gulab Jamun", 70.00, "sweet_house")
    add_food("F802", "Rasmalai", 90.00, "sweet_house")
    add_food("F803", "Kaju Katli", 120.00, "sweet_house")
    add_food("F804", "Milk Cake", 60.00, "sweet_house")
    add_food("F805", "Barfi", 80.00, "sweet_house")

    add_food("F811", "Chocolate Brownie", 120.00, "baker_street")
    add_food("F812", "Vanilla Cupcake", 90.00, "baker_street")
    add_food("F813", "Butter Croissant", 110.00, "baker_street")
    add_food("F814", "Egg Tart", 100.00, "baker_street")
    add_food("F815", "Chocolate Cookie", 60.00, "baker_street")

    add_food("F821", "Malai Kulfi", 50.00, "kulfi_corner")
    add_food("F822", "Kulfi Falooda", 130.00, "kulfi_corner")
    add_food("F823", "Gola Kulfi", 90.00, "kulfi_corner")
    add_food("F824", "Rabri Falooda", 150.00, "kulfi_corner")
    add_food("F825", "Chocolate Kulfi", 70.00, "kulfi_corner")

    # Pizza and pasta

    add_food("F101", "Margherita Pizza", 250.00, "dominoes")
    add_food("F102", "Garlic Bread", 120.00, "dominoes")
    add_food("F103", "Cold Drink", 60.00, "dominoes", False)
    add_food("F104", "Farmhouse Pizza", 420.00, "dominoes")
    add_food("F105", "Paneer Tikka Pizza", 390.00, "dominoes")

    add_food("F901", "Pepperoni Pizza", 480.00, "pizza_hut")
    add_food("F902", "Cheese Burst Pizza", 440.00, "pizza_hut")
    add_food("F903", "Chicken Wings", 260.00, "pizza_hut")
    add_food("F904", "Garlic Bread Sticks", 150.00, "pizza_hut")
    add_food("F905", "Choco Lava Cake", 180.00, "pizza_hut")

    add_food("F911", "Four Cheese Pizza", 460.00, "la_pinos")
    add_food("F912", "Chicken Supreme", 500.00, "la_pinos")
    add_food("F913", "Red Sauce Pasta", 260.00, "la_pinos")
    add_food("F914", "Baked Fish", 380.00, "la_pinos")
    add_food("F915", "Cold Coffee", 120.00, "la_pinos")

    add_food("F921", "Alfredo Pasta", 280.00, "pasta_fresco")
    add_food("F922", "Arrabbiata Pasta", 250.00, "pasta_fresco")
    add_food("F923", "Penne Arrabbiata", 240.00, "pasta_fresco")
    add_food("F924", "Lasagna", 340.00, "pasta_fresco")
    add_food("F925", "Garlic Bread", 130.00, "pasta_fresco")

    add_food("F931", "Tandoori Pizza", 340.00, "pizza_square")
    add_food("F932", "Paneer Tikka Pizza", 320.00, "pizza_square")
    add_food("F933", "Spicy Chicken Pizza", 360.00, "pizza_square")
    add_food("F934", "Garlic Bread", 100.00, "pizza_square")

    # Burgers and sandwiches

    add_food("F1001", "Whopper", 280.00, "burger_king")
    add_food("F1002", "Chicken Burger", 220.00, "burger_king")
    add_food("F1003", "Double Cheeseburger", 340.00, "burger_king")
    add_food("F1004", "French Fries", 120.00, "burger_king")
    add_food("F1005", "Onion Rings", 140.00, "burger_king")

    add_food("F1011", "Chicken Subway", 260.00, "subway")
    add_food("F1012", "Veggie Delight", 200.00, "subway")
    add_food("F1013", "Paneer Tikka Sub", 240.00, "subway")
    add_food("F1014", "Cookies Cream Shake", 150.00, "subway")

    add_food("F1021", "Grilled Sandwich", 180.00, "grill_master")
    add_food("F1022", "Club Sandwich", 240.00, "grill_master")
    add_food("F1023", "Chicken Grill", 280.00, "grill_master")
    add_food("F1024", "Nachos", 160.00, "grill_master")
    add_food("F1025", "Cold Drink", 70.00, "grill_master", False)

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


# The order we show the genres in when the customer is browsing.
# It is written out like this, instead of being built from the data,
# because a fixed list always comes out in the same order, and that
# makes the screen look the same every time the program is run.
GENRES = [
    "North Indian",
    "South Indian",
    "Biryani and Thalis",
    "Snacks and Street Food",
    "Tea and Beverages",
    "Sweets and Desserts",
    "Pizza and Pasta",
    "Burgers and Sandwiches",
]


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