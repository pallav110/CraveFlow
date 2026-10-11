# -*- coding: utf-8 -*-
# ============================================================
# CraveFlow - Food Delivery Management System
# From craving to delivery, seamlessly.
#
# Student : Yajat Sharma
# Class   : 11-A
#
# IDLE ONLY - no terminal needed, no colours, no modules.
# Run with F5 in IDLE.
# TIP: Options > Configure IDLE > Fonts/Tabs > choose Consolas
#      so that the big block letters line up properly.
#
# FUTURE PLAN (this same file will run the whole project):
#   1. DATA    -> add FOOD, ORDERS dicts below USERS
#   2. DESIGN  -> add line(), ok(), warn(), options(), box() here
#   3. SCREENS -> add customer_menu(), restaurant_menu() etc. in Sec.4
#   4. LOGIN   -> already done, don't touch
# ============================================================

# ---------- 1. DATA (our small database using a nested dictionary) ----------

WIDTH = 70
TAGLINE = "From craving to delivery, seamlessly."

USERS = {
    "yajat": {"name": "Yajat Sharma", "password": "1234", "role": "customer"},
    # FUTURE: uncomment as you build each role
    # "tandoor": {"name": "Tandoor House", "password": "1234", "role": "restaurant"},
    # "raj": {"name": "Raj Kumar", "password": "1234", "role": "rider"},
    # "owner": {"name": "Store Owner", "password": "1234", "role": "owner"},
}

# FUTURE DATA - keep commented until you need them:
# FOOD = {}    # item_id -> {"name":..., "price":..., "restaurant":..., "available": True}
# ORDERS = {}  # order_id -> {"customer":..., "items":..., "total":..., "status":..., "rider":...}

# The big CRAVEFLOW title. Each line of the title is one item in a list.
LOGO = [
    " ████  ████    ███   █   █  █████  █████  █       ███   █   █",
    "█      █   █  █   █  █   █  █      █      █      █   █  █   █",
    "█      ████   █████  █   █  ████   ████   █      █   █  █ █ █",
    "█      █  █   █   █   █ █   █      █      █      █   █  ██ ██",
    " ████  █   █  █   █    █    █████  █      █████   ███   █   █",
]


# ---------- 2. FUNCTIONS FOR DESIGN (only print statements) ----------

def line():
    print("=" * WIDTH)


def banner():
    print()
    line()
    print()
    for row in LOGO:
        print(row.center(WIDTH))
    print()
    print(TAGLINE.center(WIDTH))
    line()
    print()


def heading(text):
    print()
    print("-- " + text + " " + "-" * (WIDTH - len(text) - 4))
    print()


# FUTURE DESIGN HELPERS - add here when you need them:
# def ok(text):
#     print("[OK] " + str(text))
#
# def warn(text):
#     print("[X] " + str(text))


# ---------- 3. FUNCTIONS FOR LOGIN ----------

def login():
    # The user gets 3 chances to log in
    chances = 3
    while chances > 0:
        username = input("Username: ").strip().lower()
        if username == "exit":
            return None
        password = input("Password: ").strip()

        if username in USERS and USERS[username]["password"] == password:
            return username

        chances -= 1
        print()
        print("[X] Wrong username or password. Chances left:", chances)
        print()
    return None


def welcome(username):
    person = USERS[username]
    print()
    print("[OK] Signed in as", person["name"])
    print("     Role :", person["role"])
    print()


# ---------- 4. FUTURE SCREENS (one function per menu goes here) ----------
# FUTURE:
# def customer_menu(username):
#     heading("What would you like to do?")
#     ...
# def restaurant_menu(username):
#     ...


# ---------- 5. MAIN PROGRAM ----------

def main():
    banner()
    heading("Please sign in")
    print("(type exit as username to quit)")
    print()
    username = login()
    if username is None:
        print()
        print("Thank you for using CraveFlow.")
        print()
    else:
        welcome(username)
        # FUTURE: route by role here
        # role = USERS[username]["role"]
        # if role == "customer":
        #     customer_menu(username)


main()



# ============================================================
# PARKED FULL PROJECT - all 6 modules, commented out.
# HOW TO UNLOCK (one step at a time, press F5 after each):
#   Week 1: uncomment PART 2 DATA (add FOOD + ORDERS dicts)
#   Week 2: uncomment PART 1 DESIGN helpers (ok, warn, options, box)
#   Week 3: uncomment PART 3 CUSTOMER + route it in main()
#   Week 4: uncomment PART 4 RESTAURANT + PART 5 RIDER + PART 6 REPORTS
# RULE: remove ONE '# ' prefix per line in that part only.
# Do NOT uncomment everything at once.
# Imports inside parked code are already fixed (design.xxx -> xxx).
# ============================================================


# ---------------- PART: DESIGN (logo, headings, boxes) [design.py] ----------------
# STATUS: PARKED - uncomment this whole part when its week comes.
#
# # ============================================================
# # CraveFlow | Terminal User Interface
# # Food Delivery Management System
# # ============================================================
#
# AMBER = "\033[38;5;215m"
# WHITE = "\033[38;5;255m"
# GREY = "\033[38;5;245m"
# RED = "\033[38;5;203m"
# GREEN = "\033[38;5;114m"
# END = "\033[0m"
#
# WIDTH = 76
#
# # The logo is drawn with a 5 x 5 letter pattern, which keeps it compact.
# # Each letter is just five ordinary strings, five characters wide.
# #
# # Every letter is built out of one character, the block character.
# # The block character is the solid square that looks like this: (█)
# # It is not a normal letter, which is exactly why it makes a logo look
# # like a logo and not like a sentence.
# #
# # A # would also draw a letter, but a row of hashes reads as a
# # separator, not as a word. The block character reads as a solid shape.
# FONT = {
#     "C": [" ███ ", "█   █", "█    ", "█   █", " ███ "],
#     "R": ["████ ", "█   █", "████ ", "█  █ ", "█   █"],
#     "A": [" ███ ", "█   █", "█████", "█   █", "█   █"],
#     "V": ["█   █", "█   █", "█   █", " █ █ ", "  █  "],
#     "E": ["█████", "█    ", "████ ", "█    ", "█████"],
#     "F": ["█████", "█    ", "████ ", "█    ", "█    "],
#     "L": ["█    ", "█    ", "█    ", "█    ", "█████"],
#     "O": [" ███ ", "█   █", "█   █", "█   █", " ███ "],
#     "W": ["█   █", "█   █", "█ █ █", "██ ██", "█   █"],
# }
#
#
# def make_logo(word="CRAVEFLOW"):
#     """Build the wordmark using the letter patterns."""
#     rows = []
#
#     for row_number in range(5):
#         row = " ".join(FONT[letter][row_number] for letter in word)
#         rows.append(row)
#
#     return rows
#
#
# LOGO_ROWS = make_logo()
# TAGLINE = "From craving to delivery, seamlessly."
#
#
# def clear_screen():
#     """Clear the terminal."""
#     print("\033[2J\033[H", end="")
#
#
# def center_text(text, width):
#     """Center text inside a fixed width."""
#     text = str(text)[:width]
#     return text.center(width)
#
#
# def pad_right(text, width):
#     """Align text to the left."""
#     return str(text)[:width].ljust(width)
#
#
# def pad_left(text, width):
#     """Align text to the right."""
#     return str(text)[:width].rjust(width)
#
#
# def cut(text, length):
#     """Shorten text without exceeding the available space."""
#     text = str(text)
#
#     if len(text) <= length:
#         return text
#
#     if length <= 3:
#         return text[:length]
#
#     return text[:length - 3] + "..."
#
#
# def banner():
#     """Display the CraveFlow logo and tagline.
#
#     This is called once, at the start of the program. It does not clear
#     the screen, so nothing the user has already read gets thrown away.
#     """
#     logo_width = max(len(row) for row in LOGO_ROWS)
#     inside = max(WIDTH, logo_width)
#     border = "+" + "-" * (inside + 2) + "+"
#
#     print()
#     print(AMBER + border + END)
#
#     for row in LOGO_ROWS:
#         print(
#             AMBER + "| " + END
#             + AMBER + pad_right(row, inside) + END
#             + AMBER + " |" + END
#         )
#
#     print(
#         AMBER + "| " + END
#         + GREY + center_text(TAGLINE, inside) + END
#         + AMBER + " |" + END
#     )
#
#     print(AMBER + border + END)
#     print()
#
#
# def rule():
#     """Draw a thin divider between two screens.
#
#     This is what separates one round of a menu from the next. It does
#     not clear the screen, so the user can still scroll back and read
#     anything that was printed above it.
#     """
#     print()
#     print(GREY + "-" * WIDTH + END)
#
#
# def heading(text):
#     """Print a section heading."""
#     text = " " + str(text) + " "
#     available = max(0, WIDTH - len(text) - 2)
#
#     print()
#     print(
#         AMBER + "--" + END
#         + WHITE + text + END
#         + AMBER + "-" * available + END
#     )
#     print()
#
#
# def line(text=""):
#     """Print secondary information."""
#     print(GREY + str(text) + END)
#
#
# def ok(text):
#     """Print a successful operation."""
#     print(GREEN + "[OK] " + str(text) + END)
#
#
# def warn(text):
#     """Print an error or warning."""
#     print(RED + "[!] " + str(text) + END)
#
#
# def columns(left, right, left_width, gap=2):
#     """Print two aligned columns.
#
#     The whole row comes out exactly WIDTH characters wide, so it lines
#     up with heading() and rule(), and still fits inside box().
#     """
#     left_width = max(0, min(left_width, WIDTH - gap))
#     gap = max(0, min(gap, WIDTH - left_width))
#     right_width = WIDTH - left_width - gap
#
#     left_text = pad_right(cut(left, left_width), left_width)
#     right_text = pad_left(cut(right, right_width), right_width)
#
#     return left_text + " " * gap + right_text
#
#
# def box(title, lines):
#     """Draw a bordered panel."""
#     # A content row is "| " + WIDTH characters + " |", so the row is
#     # WIDTH + 4 wide. The top border has to be that same width, and it
#     # is built out of: a +, a -, the title, then dashes for the rest.
#     # Those first two characters leave WIDTH + 1 of dashes to share
#     # between the title and the tail.
#     title = " " + cut(title, WIDTH - 6) + " "
#     remaining = WIDTH + 1 - len(title)
#
#     top = "+" + "-" + title + "-" * max(0, remaining) + "+"
#     bottom = "+" + "-" * (len(top) - 2) + "+"
#
#     print()
#     print(AMBER + top + END)
#
#     for text in lines:
#         content = pad_right(cut(text, WIDTH), WIDTH)
#         print(
#             AMBER + "| " + END
#             + WHITE + content + END
#             + AMBER + " |" + END
#         )
#
#     print(AMBER + bottom + END)
#
#
# def options(items):
#     """Display numbered menu choices."""
#     print()
#
#     for number, item in enumerate(items, start=1):
#         print(
#             "   " + AMBER + str(number) + "." + END
#             + "  " + WHITE + str(item) + END
#         )
#
#     print("   " + GREY + "0. Go back" + END)
#     print()
#
#
# def money(amount):
#     """Format a numeric amount as Indian rupees."""
#     return "Rs. " + format(round(float(amount), 2), ".2f")


# ---------------- PART: DATA (users, food, orders, riders) [data.py] ----------------
# STATUS: PARKED - uncomment this whole part when its week comes.
# # All of CraveFlow's data lives in one dictionary, called FULL_DATA.
# # It has four parts, and each part holds more dictionaries:
# #
# #   FULL_DATA["users"]    -> every person, and whether they are a
# #                       customer, a restaurant, a rider or the owner
# #   FULL_DATA["food"]     -> every food item, and what it costs
# #   FULL_DATA["orders"]   -> every order someone has placed
# #   FULL_DATA["riders"]   -> every rider, and whether they are free or busy
# #
# # We build it inside a function so we can make a fresh copy any time
# # we want to go back to the starting point.
#
#
# def make_data():
#     """Build the dictionary, already filled with demo examples."""
#
#     data = {}
#
#     # Two small helpers live inside this function. They only exist while
#     # we are building the demo data, and they save us writing the same
#     # six lines over and over for every kitchen and every dish.
#     #
#     # Viva answer, if asked:
#     #   "I wrote two small functions inside make_data() so that adding
#     #    a restaurant or a dish takes one line instead of six. They
#     #    put the values into the dictionary for me."
#
#     def add_place(username, name, genre, fee):
#         """Put one restaurant into the users dictionary."""
#         data["users"][username] = {
#             "name": name,
#             "role": "restaurant",
#             "password": "1234",
#             "genre": genre,
#             "fee": fee,
#         }
#
#     def add_food(item_id, name, price, restaurant, available=True):
#         """Put one dish into the food dictionary."""
#         data["food"][item_id] = {
#             "name": name,
#             "price": price,
#             "restaurant": restaurant,
#             "available": available,
#         }
#
#     # ---- The people -----------------------------------------------
#
#     data["users"] = {}
#
#     data["users"]["yajat"] = {
#         "name": "Yajat Sharma",
#         "role": "customer",
#         "password": "1234",
#     }
#
#     # ---- The restaurants ------------------------------------------
#     # "genre" is the kind of food the kitchen cooks. It is only a label,
#     # but it lets the customer browse by style instead of by alphabet.
#     # "fee" is what that kitchen charges for delivery, and it is added
#     # to the bill once, at the end, whatever is ordered.
#
#     # North Indian
#     add_place("tandoor", "Tandoor House", "North Indian", 25.00)
#     add_place("punjabi", "Punjabi Darbar", "North Indian", 30.00)
#     add_place("old_delhi", "Old Delhi Waqf", "North Indian", 20.00)
#     add_place("curry_pot", "Curries and Pots", "North Indian", 35.00)
#
#     # South Indian
#     add_place("madras", "Madras Cafe", "South Indian", 20.00)
#     add_place("udupi", "Udupi Bhavan", "South Indian", 22.00)
#     add_place("andhra", "Andhra Spice", "South Indian", 28.00)
#     add_place("kerala", "Kerala Kitchen", "South Indian", 32.00)
#
#     # Biryani and thalis
#     add_place("biryani_adda", "Biryani Adda", "Biryani and Thalis", 35.00)
#     add_place("thali_house", "Thali House", "Biryani and Thalis", 40.00)
#
#     # Snacks and street food
#     add_place("chaat", "Chaat Junction", "Snacks and Street Food", 15.00)
#     add_place("momo_house", "Momo House", "Snacks and Street Food", 20.00)
#     add_place("rollwala", "Rollwala", "Snacks and Street Food", 18.00)
#     add_place("halidirams", "Haldiram's", "Snacks and Street Food", 12.00)
#
#     # Tea and drinks
#     add_place("chai_point", "Chai Point", "Tea and Beverages", 10.00)
#     add_place("coffee_day", "Coffee Day", "Tea and Beverages", 15.00)
#     add_place("juice_factory", "Juice Factory", "Tea and Beverages", 20.00)
#     add_place("bubble_blast", "Bubble Blast", "Tea and Beverages", 25.00)
#
#     # Sweets
#     add_place("sweet_house", "Sweet House", "Sweets and Desserts", 15.00)
#     add_place("baker_street", "Baker Street", "Sweets and Desserts", 20.00)
#     add_place("kulfi_corner", "Kulfi Corner", "Sweets and Desserts", 18.00)
#
#     # Italian - pizza and pasta
#     add_place("dominoes", "Domino's Pizza", "Pizza and Pasta", 40.00)
#     add_place("pizza_hut", "Pizza Hut", "Pizza and Pasta", 45.00)
#     add_place("la_pinos", "La Pino's", "Pizza and Pasta", 35.00)
#     add_place("pasta_fresco", "Pasta Fresco", "Pizza and Pasta", 40.00)
#     add_place("pizza_square", "Pizza Square", "Pizza and Pasta", 30.00)
#
#     # Burgers and sandwiches
#     add_place("burger_king", "Burger King", "Burgers and Sandwiches", 35.00)
#     add_place("subway", "Subway", "Burgers and Sandwiches", 30.00)
#     add_place("grill_master", "Grill Master", "Burgers and Sandwiches", 25.00)
#
#     # ---- The riders and the owner ---------------------------------
#
#     data["users"]["raj"] = {
#         "name": "Raj Kumar",
#         "role": "rider",
#         "password": "1234",
#     }
#
#     data["users"]["meera"] = {
#         "name": "Meera Singh",
#         "role": "rider",
#         "password": "1234",
#     }
#
#     data["users"]["owner"] = {
#         "name": "Store Owner",
#         "role": "owner",
#         "password": "1234",
#     }
#
#     # ---- The food -------------------------------------------------
#     # "available" is True or False. False means it has sold out, so the
#     # customer will not see it, but the restaurant can still see it.
#     # A dish name has to stay under 25 letters, or it will not fit in
#     # the table when it is printed.
#
#     data["food"] = {}
#
#     # North Indian
#
#     add_food("F201", "Butter Chicken", 280.00, "tandoor")
#     add_food("F202", "Paneer Tikka", 220.00, "tandoor")
#     add_food("F203", "Dal Makhani", 190.00, "tandoor")
#     add_food("F204", "Chicken Korma", 310.00, "tandoor")
#     add_food("F205", "Tandoori Roti", 45.00, "tandoor", False)
#
#     add_food("F301", "Sarson Da Saag", 180.00, "punjabi")
#     add_food("F302", "Kadhai Paneer", 240.00, "punjabi")
#     add_food("F303", "Chicken Tikka", 320.00, "punjabi")
#     add_food("F304", "Paneer Tikka Plate", 260.00, "punjabi")
#     add_food("F305", "Sweet Lassi", 80.00, "punjabi")
#
#     add_food("F311", "Chole Bhature", 150.00, "old_delhi")
#     add_food("F312", "Rajma Chawal", 130.00, "old_delhi")
#     add_food("F313", "Paratha Platter", 110.00, "old_delhi")
#     add_food("F314", "Butter Naan", 55.00, "old_delhi")
#     add_food("F315", "Gulab Jamun", 60.00, "old_delhi")
#
#     add_food("F321", "Butter Chicken", 290.00, "curry_pot")
#     add_food("F322", "Malai Kofta", 230.00, "curry_pot")
#     add_food("F323", "Egg Curry", 210.00, "curry_pot")
#     add_food("F324", "Paneer Butter Masala", 250.00, "curry_pot")
#     add_food("F325", "Garlic Naan", 50.00, "curry_pot")
#
#     # South Indian
#
#     add_food("F401", "Idli Sambar", 90.00, "madras")
#     add_food("F402", "Plain Dosa", 110.00, "madras")
#     add_food("F403", "Masala Dosa", 140.00, "madras")
#     add_food("F404", "Filter Coffee", 50.00, "madras")
#     add_food("F405", "Vada Sambar", 80.00, "madras")
#
#     add_food("F411", "Ghee Roast Dosa", 160.00, "udupi")
#     add_food("F412", "Mangalorean Fish", 340.00, "udupi")
#     add_food("F413", "Konkani Chicken", 300.00, "udupi")
#     add_food("F414", "Podi Idli", 120.00, "udupi")
#     add_food("F415", "Buttermilk", 40.00, "udupi")
#
#     add_food("F421", "Andhra Chicken Biryani", 260.00, "andhra")
#     add_food("F422", "Ghee Roast Dosa", 150.00, "andhra")
#     add_food("F423", "Mutton Rogan Josh", 380.00, "andhra")
#     add_food("F424", "Pulihora Rice", 180.00, "andhra")
#     add_food("F425", "Coconut Chutney", 30.00, "andhra")
#
#     add_food("F431", "Kerala Fish Curry", 340.00, "kerala")
#     add_food("F432", "Appam with Stew", 220.00, "kerala")
#     add_food("F433", "Chicken Sukka", 300.00, "kerala")
#     add_food("F434", "Sadhya Plate", 450.00, "kerala")
#     add_food("F435", "Payasam", 110.00, "kerala")
#
#     # Biryani and thalis
#
#     add_food("F501", "Chicken Dum Biryani", 320.00, "biryani_adda")
#     add_food("F502", "Mutton Biryani", 420.00, "biryani_adda")
#     add_food("F503", "Veg Dum Biryani", 280.00, "biryani_adda")
#     add_food("F504", "Raita", 50.00, "biryani_adda")
#     add_food("F505", "Gulab Jamun", 60.00, "biryani_adda")
#
#     add_food("F511", "Veg Thali", 220.00, "thali_house")
#     add_food("F512", "Non Veg Thali", 340.00, "thali_house")
#     add_food("F513", "Paneer Thali", 260.00, "thali_house")
#     add_food("F514", "Dal Rice", 120.00, "thali_house")
#     add_food("F515", "Sweet", 40.00, "thali_house")
#
#     # Snacks and street food
#
#     add_food("F601", "Golgappa", 60.00, "chaat")
#     add_food("F602", "Papdi Chaat", 80.00, "chaat")
#     add_food("F603", "Dahi Bhalla", 90.00, "chaat")
#     add_food("F604", "Aloo Tikki", 70.00, "chaat")
#     add_food("F605", "Pani Puri", 50.00, "chaat")
#
#     add_food("F611", "Steamed Momo", 70.00, "momo_house")
#     add_food("F612", "Fried Momo", 90.00, "momo_house")
#     add_food("F613", "Chilli Garlic Momo", 110.00, "momo_house")
#     add_food("F614", "Momo Soup", 60.00, "momo_house")
#     add_food("F615", "Chilli Momo", 120.00, "momo_house", False)
#
#     add_food("F621", "Chicken Roll", 100.00, "rollwala")
#     add_food("F622", "Paneer Roll", 90.00, "rollwala")
#     add_food("F623", "Egg Roll", 70.00, "rollwala")
#     add_food("F624", "Masala Maggi", 60.00, "rollwala")
#     add_food("F625", "Chicken Cheese Roll", 140.00, "rollwala")
#
#     add_food("F631", "Aloo Bhujia", 40.00, "halidirams")
#     add_food("F632", "Bikaneri Bhalla", 60.00, "halidirams")
#     add_food("F633", "Samosa", 50.00, "halidirams")
#     add_food("F634", "Poha Chunks", 45.00, "halidirams")
#     add_food("F635", "Laddoo", 70.00, "halidirams")
#
#     # Tea and beverages
#
#     add_food("F701", "Masala Chai", 25.00, "chai_point")
#     add_food("F702", "Kadak Chai", 30.00, "chai_point")
#     add_food("F703", "Chai Biscuit", 20.00, "chai_point")
#     add_food("F704", "Samosa With Chutney", 40.00, "chai_point")
#     add_food("F705", "Lemon Iced Tea", 60.00, "chai_point")
#
#     add_food("F711", "Cappuccino", 140.00, "coffee_day")
#     add_food("F712", "Cold Coffee", 160.00, "coffee_day")
#     add_food("F713", "Cafe Latte", 130.00, "coffee_day")
#     add_food("F714", "Thick Shake", 180.00, "coffee_day")
#     add_food("F715", "Blueberry Muffin", 80.00, "coffee_day")
#
#     add_food("F721", "Fresh Lime Soda", 80.00, "juice_factory")
#     add_food("F722", "Watermelon Juice", 90.00, "juice_factory")
#     add_food("F723", "Orange Juice", 110.00, "juice_factory")
#     add_food("F724", "Mixed Fruit Juice", 120.00, "juice_factory")
#     add_food("F725", "Green Tea", 50.00, "juice_factory")
#
#     add_food("F731", "Classic Milk Tea", 90.00, "bubble_blast")
#     add_food("F732", "Taro Milk Tea", 110.00, "bubble_blast")
#     add_food("F733", "Matcha Latte", 130.00, "bubble_blast")
#     add_food("F734", "Mango Ice Blast", 120.00, "bubble_blast")
#     add_food("F735", "Cheese Foam Tea", 140.00, "bubble_blast")
#
#     # Sweets and desserts
#
#     add_food("F801", "Gulab Jamun", 70.00, "sweet_house")
#     add_food("F802", "Rasmalai", 90.00, "sweet_house")
#     add_food("F803", "Kaju Katli", 120.00, "sweet_house")
#     add_food("F804", "Milk Cake", 60.00, "sweet_house")
#     add_food("F805", "Barfi", 80.00, "sweet_house")
#
#     add_food("F811", "Chocolate Brownie", 120.00, "baker_street")
#     add_food("F812", "Vanilla Cupcake", 90.00, "baker_street")
#     add_food("F813", "Butter Croissant", 110.00, "baker_street")
#     add_food("F814", "Egg Tart", 100.00, "baker_street")
#     add_food("F815", "Chocolate Cookie", 60.00, "baker_street")
#
#     add_food("F821", "Malai Kulfi", 50.00, "kulfi_corner")
#     add_food("F822", "Kulfi Falooda", 130.00, "kulfi_corner")
#     add_food("F823", "Gola Kulfi", 90.00, "kulfi_corner")
#     add_food("F824", "Rabri Falooda", 150.00, "kulfi_corner")
#     add_food("F825", "Chocolate Kulfi", 70.00, "kulfi_corner")
#
#     # Pizza and pasta
#
#     add_food("F101", "Margherita Pizza", 250.00, "dominoes")
#     add_food("F102", "Garlic Bread", 120.00, "dominoes")
#     add_food("F103", "Cold Drink", 60.00, "dominoes", False)
#     add_food("F104", "Farmhouse Pizza", 420.00, "dominoes")
#     add_food("F105", "Paneer Tikka Pizza", 390.00, "dominoes")
#
#     add_food("F901", "Pepperoni Pizza", 480.00, "pizza_hut")
#     add_food("F902", "Cheese Burst Pizza", 440.00, "pizza_hut")
#     add_food("F903", "Chicken Wings", 260.00, "pizza_hut")
#     add_food("F904", "Garlic Bread Sticks", 150.00, "pizza_hut")
#     add_food("F905", "Choco Lava Cake", 180.00, "pizza_hut")
#
#     add_food("F911", "Four Cheese Pizza", 460.00, "la_pinos")
#     add_food("F912", "Chicken Supreme", 500.00, "la_pinos")
#     add_food("F913", "Red Sauce Pasta", 260.00, "la_pinos")
#     add_food("F914", "Baked Fish", 380.00, "la_pinos")
#     add_food("F915", "Cold Coffee", 120.00, "la_pinos")
#
#     add_food("F921", "Alfredo Pasta", 280.00, "pasta_fresco")
#     add_food("F922", "Arrabbiata Pasta", 250.00, "pasta_fresco")
#     add_food("F923", "Penne Arrabbiata", 240.00, "pasta_fresco")
#     add_food("F924", "Lasagna", 340.00, "pasta_fresco")
#     add_food("F925", "Garlic Bread", 130.00, "pasta_fresco")
#
#     add_food("F931", "Tandoori Pizza", 340.00, "pizza_square")
#     add_food("F932", "Paneer Tikka Pizza", 320.00, "pizza_square")
#     add_food("F933", "Spicy Chicken Pizza", 360.00, "pizza_square")
#     add_food("F934", "Garlic Bread", 100.00, "pizza_square")
#
#     # Burgers and sandwiches
#
#     add_food("F1001", "Whopper", 280.00, "burger_king")
#     add_food("F1002", "Chicken Burger", 220.00, "burger_king")
#     add_food("F1003", "Double Cheeseburger", 340.00, "burger_king")
#     add_food("F1004", "French Fries", 120.00, "burger_king")
#     add_food("F1005", "Onion Rings", 140.00, "burger_king")
#
#     add_food("F1011", "Chicken Subway", 260.00, "subway")
#     add_food("F1012", "Veggie Delight", 200.00, "subway")
#     add_food("F1013", "Paneer Tikka Sub", 240.00, "subway")
#     add_food("F1014", "Cookies Cream Shake", 150.00, "subway")
#
#     add_food("F1021", "Grilled Sandwich", 180.00, "grill_master")
#     add_food("F1022", "Club Sandwich", 240.00, "grill_master")
#     add_food("F1023", "Chicken Grill", 280.00, "grill_master")
#     add_food("F1024", "Nachos", 160.00, "grill_master")
#     add_food("F1025", "Cold Drink", 70.00, "grill_master", False)
#
#     # ---- The orders -----------------------------------------------
#     # status can only ever be one of these five words:
#     #   PLACED     the customer just ordered
#     #   ACCEPTED   the restaurant said yes
#     #   PICKED_UP  a rider has collected it
#     #   DELIVERED  it reached the customer
#     #   CANCELLED  it will not happen
#
#     data["orders"] = {}
#
#     # ---- The riders -----------------------------------------------
#     # status is FREE or BUSY. This is the lock that stops one rider
#     # picking up two orders at the same time.
#
#     data["riders"] = {}
#
#     data["riders"]["raj"] = {
#         "name": "Raj Kumar",
#         "status": "FREE",
#         "order": None,
#     }
#
#     data["riders"]["meera"] = {
#         "name": "Meera Singh",
#         "status": "FREE",
#         "order": None,
#     }
#
#     return data
#
#
# # The order we show the genres in when the customer is browsing.
# # It is written out like this, instead of being built from the data,
# # because a fixed list always comes out in the same order, and that
# # makes the screen look the same every time the program is run.
# FULL_GENRES = [
#     "North Indian",
#     "South Indian",
#     "Biryani and Thalis",
#     "Snacks and Street Food",
#     "Tea and Beverages",
#     "Sweets and Desserts",
#     "Pizza and Pasta",
#     "Burgers and Sandwiches",
# ]
#
#
# # This is the one dictionary every other file uses.
# FULL_DATA = make_data()
#
#
# def show_data():
#     """Print the whole dictionary, so we can see what is inside it."""
#     print(FULL_DATA)
#
#
# # --------------------------------------------------------------------
# #  SAVING THE FULL_DATA TO A FILE - SWITCHED OFF ON PURPOSE
# # --------------------------------------------------------------------
# #
# #  This program used to save FULL_DATA into a file called data.json, and
# #  read it back the next time it started, so the food a kitchen added
# #  would still be there tomorrow.
# #
# #  That is switched off now, on purpose. A demo is much easier to follow
# #  when it always starts from exactly the same demo data, so the person
# #  watching can see the whole flow the same way every single time. The
# #  data now lives only while the program is open, and when the program
# #  closes it is gone.
# #
# #  Nothing above this line is affected. save_data() is still called
# #  everywhere it always was, it just does not have to do anything yet.
#
#
# def save_data():
#     """Save the data - but saving is switched off at the moment.
#
#     Every place in the program that changes something calls this at the
#     end, so turning saving back on later is a job of writing the body
#     of this one function. Nothing else has to change.
#     """
#     pass


# ---------------- PART: CUSTOMER (browse, order, cancel) [customer.py] ----------------
# STATUS: PARKED - uncomment this whole part when its week comes.
# # This file holds everything a customer can do.
# #
# # A customer can:
# #   - see every restaurant and what food is on sale
# #   - place an order
# #   - see the orders they have already placed
# #   - cancel an order they have not collected yet
# #
# # A customer never sees food that has sold out, and never sees or
# # touches another customer's orders.
#
# import design_helpers (same file)
# from data_block import FULL_DATA, FULL_GENRES, save_data
#
#
# def restaurants_with_food():
#     """Return the usernames of every restaurant that still has food.
#
#     We only want restaurants the customer can actually order from, so
#     a restaurant whose kitchen is sold out is left out completely.
#     """
#     names = []
#
#     for username in FULL_DATA["users"]:
#         if FULL_DATA["users"][username]["role"] != "restaurant":
#             continue
#
#         for item_id in FULL_DATA["food"]:
#             if FULL_DATA["food"][item_id]["restaurant"] == username:
#                 if FULL_DATA["food"][item_id]["available"]:
#                     names.append(username)
#                     break
#
#     return names
#
#
# def available_food(username):
#     """Return the food IDs a restaurant is currently selling."""
#     items = []
#
#     for item_id in FULL_DATA["food"]:
#         item = FULL_DATA["food"][item_id]
#
#         if item["restaurant"] == username and item["available"]:
#             items.append(item_id)
#
#     return items
#
#
# def food_line(item_id):
#     """Turn one food item into a line of text for a box.
#
#     The three columns are ID, name and price. columns lines
#     them up, so every table in the program matches the others.
#     """
#     item = FULL_DATA["food"][item_id]
#     name = pad_right(item["name"], 24) + item_id
#
#     return columns(name, money(item["price"]), 32)
#
#
# def places_by_genre():
#     """Group every restaurant that has food, by the kind of food it cooks.
#
#     FULL_GENRES holds the order we show them in, so the screen looks the same
#     every time the program is run. A kitchen we do not have a genre for
#     is still shown, at the end, so nothing can ever be hidden by mistake.
#     """
#     groups = []
#     open_places = restaurants_with_food()
#
#     for genre in FULL_GENRES:
#         names = []
#
#         for username in FULL_DATA["users"]:
#             if FULL_DATA["users"][username]["role"] != "restaurant":
#                 continue
#
#             if FULL_DATA["users"][username].get("genre") != genre:
#                 continue
#
#             if username in open_places:
#                 names.append(username)
#
#         if len(names) > 0:
#             groups.append([genre, names])
#
#     return groups
#
#
# def browse_one_genre(username, genre, places):
#     """Show the kitchens in one style of food, then let them order.
#
#     Browsing on its own used to be a dead end. The customer could read
#     the food, then had to go back to the menu and start ordering from
#     the beginning, which printed the same tables a second time. So
#     choosing a style now goes straight into choosing from it.
#
#     genre is the name of the style, shown as the heading. places is
#     the list of kitchens in it.
#
#     Returns the new order ID if one was placed, and None if they did
#     not end up ordering.
#     """
#     heading(genre)
#
#     total_count = 0
#
#     for place in places:
#         items = available_food(place)
#         place_name = FULL_DATA["users"][place]["name"]
#         fee = FULL_DATA["users"][place]["fee"]
#
#         box(place_name + "   -   delivery " + money(fee),
#                [food_line(item_id) for item_id in items])
#
#         total_count = total_count + len(items)
#
#     line("Showing " + str(total_count) + " items from "
#                 + str(len(places)) + " restaurants.")
#     print()
#
#     return choose_food(username, places)
#
#
# def pick_genre(question):
#     """Show the list of food styles and return the one they picked.
#
#     Both ways into ordering ask this the same way, so the screen a
#     customer sees is the same whichever door they came through.
#
#     Returns [genre, kitchens], or None if they went back.
#     """
#     groups = places_by_genre()
#
#     if len(groups) == 0:
#         warn("No restaurant has food available right now.")
#         print()
#         return None
#
#     heading(question)
#     options([group[0] for group in groups])
#
#     choice = input("Your choice: ")
#     print()
#
#     if not choice.isdigit():
#         warn("Please type a number.")
#         print()
#         return None
#
#     number = int(choice)
#
#     # 0 is what every menu uses to go back, so it has to work here too
#     if number == 0:
#         return None
#
#     if number < 1 or number > len(groups):
#         warn("There is no choice number " + choice + ".")
#         print()
#         return None
#
#     return groups[number - 1]
#
#
# def browse(username):
#     """Ask which kind of food they want, then show only those kitchens.
#
#     There are far too many kitchens and dishes to print all at once.
#     So we ask first, and then print one style of food at a time, which
#     keeps the screen short enough to actually read.
#     """
#     customer_name = FULL_DATA["users"][username]["name"]
#
#     picked = pick_genre("Hello " + customer_name + ", what kind of food?")
#
#     if picked is None:
#         return None
#
#     return browse_one_genre(username, picked[0], picked[1])
#
#
# def show_food_of(place):
#     """Show one restaurant's food on its own, for choosing an item."""
#     items = available_food(place)
#     place_name = FULL_DATA["users"][place]["name"]
#
#     box(place_name, [food_line(item_id) for item_id in items])
#
#
# def new_order_id():
#     """Make a brand new order ID that is not being used yet.
#
#     Same idea as new_food_id - count up until we find a free one, so
#     a cancelled or deleted order can never make us repeat an ID.
#     """
#     number = len(FULL_DATA["orders"]) + 1001
#
#     while ("O" + str(number)) in FULL_DATA["orders"]:
#         number = number + 1
#
#     return "O" + str(number)
#
#
# def my_active_order(username):
#     """Return the ID of an order this customer already has going.
#
#     An order is still going if it is PLACED, ACCEPTED or PICKED_UP.
#     Returns None if there is no such order.
#     """
#     for order_id in FULL_DATA["orders"]:
#         order = FULL_DATA["orders"][order_id]
#
#         if order["customer"] != username:
#             continue
#
#         if order["status"] == "PLACED":
#             return order_id
#         if order["status"] == "ACCEPTED":
#             return order_id
#         if order["status"] == "PICKED_UP":
#             return order_id
#
#     return None
#
#
# def build_order(username, place, chosen):
#     """Work out the bill for an order and save it.
#
#     place is the restaurant's username.
#     chosen is a dictionary like {"F101": 2, "F102": 1}
#
#     Returns the new order ID, or None if we had to stop.
#     """
#     food_total = 0.0
#     items = []
#     quantities = {}
#
#     for item_id in chosen:
#         quantity = chosen[item_id]
#         price = FULL_DATA["food"][item_id]["price"]
#
#         food_total = food_total + price * quantity
#         items.append(item_id)
#         quantities[item_id] = quantity
#
#     fee = FULL_DATA["users"][place]["fee"]
#     total = round(food_total + fee, 2)
#
#     order_id = new_order_id()
#
#     FULL_DATA["orders"][order_id] = {
#         "customer": username,
#         "items": items,
#         "quantities": quantities,
#         "restaurant": place,
#         "total": total,
#         "status": "PLACED",
#         "rider": None,
#     }
#
#     save_data()
#
#     return order_id
#
#
# def bill_lines(order_id):
#     """Work out the lines that show one order's bill.
#
#     Returns a list of text lines, one per row. The order screen and the
#     receipt both use this, so the two can never disagree about the bill.
#
#     The food total is worked out from the prices again here, because it
#     is only a display. The amount the customer actually paid is the
#     stored total, and we never change that.
#     """
#     order = FULL_DATA["orders"][order_id]
#     lines = []
#     food_total = 0.0
#
#     for item_id in order["items"]:
#         item = FULL_DATA["food"].get(item_id)
#         quantity = order["quantities"][item_id]
#
#         # the item may have been deleted from the menu since, so if it
#         # is gone we show the ID alone instead of crashing
#         if item is None:
#             lines.append(columns(item_id + "  (removed from menu)",
#                                         "x" + str(quantity), 32))
#             continue
#
#         amount = item["price"] * quantity
#         food_total = food_total + amount
#
#         left = pad_right(item["name"], 24) + "  x" + str(quantity)
#         lines.append(columns(left, money(amount), 32))
#
#     fee = FULL_DATA["users"][order["restaurant"]]["fee"]
#
#     lines.append("")
#     lines.append(columns("Food total", money(food_total), 32))
#     lines.append(columns("Delivery fee", money(fee), 32))
#     lines.append(columns("To pay", money(order["total"]), 32))
#
#     return lines
#
#
# def show_order(order_id):
#     """Print one order nicely, with its items and its bill."""
#     order = FULL_DATA["orders"][order_id]
#     place_name = FULL_DATA["users"][order["restaurant"]]["name"]
#
#     box("Order " + order_id + "   [" + order["status"] + "]",
#                bill_lines(order_id))
#
#     line("Ordered from " + place_name
#                 + "   -   delivered to "
#                 + FULL_DATA["users"][order["customer"]]["name"])
#
#     if order["rider"] is not None:
#         rider = FULL_DATA["users"][order["rider"]]["name"]
#         line("Rider: " + rider)
#
#     print()
#
#
# def show_receipt(order_id):
#     """Print the receipt for an order that has just been delivered.
#
#     This is the thank you. It says who it was for, who brought it, and
#     exactly what they paid for.
#     """
#     order = FULL_DATA["orders"][order_id]
#     customer_name = FULL_DATA["users"][order["customer"]]["name"]
#     place_name = FULL_DATA["users"][order["restaurant"]]["name"]
#
#     if order["rider"] is None:
#         rider_name = "None"
#     else:
#         rider_name = FULL_DATA["users"][order["rider"]]["name"]
#
#     print()
#     ok("Thank you for ordering with CraveFlow.")
#     print()
#
#     box("Receipt   " + order_id, [
#         "Billed to    : " + customer_name,
#         "Kitchen      : " + place_name,
#         "Delivered by : " + rider_name,
#         "",
#     ] + bill_lines(order_id))
#
#     print()
#     line("Your food has arrived. Enjoy your meal.")
#     print()
#
#
# def my_orders(username):
#     """Show this customer's own orders, newest ID last."""
#     mine = []
#
#     for order_id in FULL_DATA["orders"]:
#         if FULL_DATA["orders"][order_id]["customer"] == username:
#             mine.append(order_id)
#
#     if len(mine) == 0:
#         heading("My orders")
#         warn("You have not placed any orders yet.")
#         print()
#         return
#
#     heading("My orders")
#
#     for order_id in sorted(mine):
#         order = FULL_DATA["orders"][order_id]
#         count = len(order["items"])
#         ok(order_id + "  [" + order["status"] + "]  -  "
#                   + money(order["total"])
#                   + "  -  " + str(count) + " item(s)")
#         show_order(order_id)
#
#
# def choose_food(username, places):
#     """Pick a kitchen from a list, then pick food from that kitchen.
#
#     places is the list of kitchens we already printed, so the numbers
#     on screen are the numbers we accept. Both "Place a new order" and
#     "See food by type" come through here, so the two ways of ordering
#     behave exactly the same.
#
#     The rule that a customer cannot have two orders on the way at once
#     is checked here rather than in either caller, because this is the
#     only place an order is actually created.
#
#     Returns the new order ID if one was placed, and None if they did
#     not end up ordering.
#     """
#     busy = my_active_order(username)
#
#     if busy is not None:
#         warn("You already have order " + busy + " on the way.")
#         line("Please wait for it, or cancel it, before ordering again.")
#         print()
#         return None
#
#     line("Type the number of the kitchen you want.")
#     print()
#
#     while True:
#         number = 1
#         for place in places:
#             line("  " + str(number) + ". "
#                         + FULL_DATA["users"][place]["name"])
#             number = number + 1
#
#         print()
#         choice = input("Which restaurant? (0 to go back): ")
#
#         if choice == "0":
#             return None
#
#         if not choice.isdigit():
#             warn("Please type a number.")
#             print()
#             continue
#
#         position = int(choice)
#
#         if position < 1 or position > len(places):
#             warn("There is no restaurant number " + choice + ".")
#             print()
#             continue
#
#         break
#
#     place = places[position - 1]
#     show_food_of(place)
#
#     chosen = {}
#
#     while True:
#         print()
#         line("Type the food ID and how many, for example F101 2")
#         line("Type 0 on its own when you are done.")
#
#         answer = input("Food: ")
#
#         if answer == "0":
#             break
#
#         parts = answer.split()
#
#         if len(parts) != 2:
#             warn("Type an ID and a number, like F101 2")
#             print()
#             continue
#
#         item_id = parts[0].upper()
#         quantity_text = parts[1]
#
#         if item_id not in FULL_DATA["food"]:
#             warn("There is no food item with the ID " + item_id + ".")
#             print()
#             continue
#
#         if not quantity_text.isdigit():
#             warn("The number must be 1 or more.")
#             print()
#             continue
#
#         quantity = int(quantity_text)
#
#         if quantity < 1:
#             warn("The number must be 1 or more.")
#             print()
#             continue
#
#         item = FULL_DATA["food"][item_id]
#
#         if item["restaurant"] != place:
#             warn(item["name"] + " is from a different ")
#             print()
#             continue
#
#         if not item["available"]:
#             warn(item["name"]
#                         + " is sold out, so it cannot be ordered.")
#             print()
#             continue
#
#         # if they already asked for this one, add to it instead of
#         # throwing the first number away
#         if item_id in chosen:
#             chosen[item_id] = chosen[item_id] + quantity
#         else:
#             chosen[item_id] = quantity
#
#     if len(chosen) == 0:
#         warn("Nothing was selected, so no order was made.")
#         print()
#         return None
#
#     order_id = build_order(username, place, chosen)
#
#     print()
#     ok("Order placed! Your order ID is " + order_id + ".")
#     print()
#     show_order(order_id)
#
#     return order_id
#
#
# def place_order(username):
#     """Ask what the customer wants, and create the order.
#
#     There are four checks we must get past before an order is made:
#       1. they must pick at least one thing
#       2. everything must come from one restaurant
#       3. nothing they picked may have sold out since they looked
#       4. they cannot already have an order on the way
#
#     The first one and the last one are checked inside choose_food(),
#     because the customer also gets there through "See food by type"
#     and the rules have to be the same on both roads.
#     """
#     heading("Place a new order")
#
#     picked = pick_genre("Which kind of food?")
#
#     if picked is None:
#         return None
#
#     return browse_one_genre(username, picked[0], picked[1])
#
#
# def cancel_order(username):
#     """Cancel one of this customer's orders, if it is still allowed."""
#     heading("Cancel an order")
#
#     mine = []
#
#     for order_id in FULL_DATA["orders"]:
#         order = FULL_DATA["orders"][order_id]
#
#         if order["customer"] != username:
#             continue
#
#         if order["status"] == "PLACED":
#             mine.append(order_id)
#         elif order["status"] == "ACCEPTED":
#             mine.append(order_id)
#
#     if len(mine) == 0:
#         warn("You have no order that can be cancelled.")
#         line("An order can be cancelled until a rider collects it.")
#         print()
#         return
#
#     for order_id in mine:
#         order = FULL_DATA["orders"][order_id]
#         ok(order_id + "  -  " + money(order["total"])
#                   + "  -  " + order["status"])
#
#     print()
#     order_id = input("Which order ID? ").upper()
#
#     if order_id not in mine:
#         warn("That order cannot be cancelled.")
#         print()
#         return
#
#     order = FULL_DATA["orders"][order_id]
#
#     if order["rider"] is not None:
#         warn("A rider is already carrying that order.")
#         print()
#         return
#
#     order["status"] = "CANCELLED"
#     save_data()
#
#     print()
#     ok("Order " + order_id + " has been cancelled.")
#
#
# def customer_menu(username):
#     """Keep showing the customer menu until they choose to leave.
#
#     The name of the person is printed once, by main.welcome(), at the
#     moment they sign in. Repeating it before every choice would push
#     the actual answer down the screen and out of view.
#
#     What is repeated is only the one line that can change: whether
#     they still have an order on the way. It is shown the first time
#     it appears, and then left alone until it actually changes, so a
#     long session does not fill up with the same line again and again.
#     """
#     last_status = ""
#
#     while True:
#         rule()
#
#         active = my_active_order(username)
#
#         if active is not None:
#             status = "Order " + active + " is on the way."
#         else:
#             status = "You have no order on the way."
#
#         if status != last_status:
#             line(status)
#             print()
#             last_status = status
#
#         heading("What would you like to do?")
#         options([
#             "See food by type",
#             "Place a new order",
#             "My orders",
#             "Cancel an order",
#         ])
#
#         choice = input("Your choice: ")
#         print()
#
#         if choice == "1":
#             browse(username)
#         elif choice == "2":
#             place_order(username)
#         elif choice == "3":
#             my_orders(username)
#         elif choice == "4":
#             cancel_order(username)
#         elif choice == "0":
#             line("Leaving the customer menu.")
#             print()
#             return
#         else:
#             warn("Please choose a number from 0 to 4.")
#             print()


# ---------------- PART: RESTAURANT (menu, accept, reject) [restaurant.py] ----------------
# STATUS: PARKED - uncomment this whole part when its week comes.
# # This file holds everything a restaurant can do.
# #
# # A restaurant can:
# #   - see its own food
# #   - add a new food item
# #   - change a price
# #   - mark an item as sold out, or back in stock
# #   - delete an item completely
# #
# # Nothing here ever touches another restaurant's food. Every time we
# # look for an item we check whose it is.
#
# import design_helpers (same file)
# from data_block import FULL_DATA, save_data
#
#
# def my_items(username):
#     """Return a list of this restaurant's own food items.
#
#     username is the restaurant that is logged in.
#     The returned list holds the food IDs, not the whole item.
#     """
#     items = []
#
#     for item_id in FULL_DATA["food"]:
#         if FULL_DATA["food"][item_id]["restaurant"] == username:
#             items.append(item_id)
#
#     return items
#
#
# def new_food_id():
#     """Make a brand new food ID that is not being used yet.
#
#     We start counting from the number of items we have and add 101.
#     If that ID is already taken we move to the next one, until we find
#     a free one. This matters because deleting an item makes the list
#     shorter, which could otherwise repeat an old ID.
#     """
#     number = len(FULL_DATA["food"]) + 101
#
#     while ("F" + str(number)) in FULL_DATA["food"]:
#         number = number + 1
#
#     return "F" + str(number)
#
#
# def read_price():
#     """Ask for a price and make sure it is a real number.
#
#     Returns the price as a float, or None if what was typed was not
#     a number we can use.
#     """
#     text = input("Price: ")
#
#     # remove one point, so that "250" and "250.50" both pass
#     cleaned = text.replace(".", "", 1)
#
#     # isalpha means it is only letters, isdigit means only numbers
#     # if it is not letters and it is digits, it is a number
#     if cleaned.isdigit():
#         price = float(text)
#
#         if price < 0:
#             warn("The price cannot be less than zero.")
#             return None
#
#         return price
#
#     warn("Please type a number for the price, like 250 or 250.50.")
#     return None
#
#
# def ask_item_id(username, action):
#     """Ask which food item we are working on, and check it is theirs.
#
#     Returns the item ID, or None if it was not found.
#     """
#     item_id = input("Food ID (for example F101): ")
#     item_id = item_id.upper()
#
#     if item_id not in FULL_DATA["food"]:
#         warn("There is no food item with the ID " + item_id + ".")
#         return None
#
#     if FULL_DATA["food"][item_id]["restaurant"] != username:
#         warn("That item belongs to a different ")
#         return None
#
#     return item_id
#
#
# def show_my_food(username):
#     """Show this restaurant's food in two tables.
#
#     The available items are in the first table and the sold out items
#     are in the second one, so it is easy to see what needs restocking.
#     """
#     items = my_items(username)
#
#     if len(items) == 0:
#         heading("My food")
#         warn("You have not added any food yet.")
#         print()
#         return
#
#     available = []
#     sold_out = []
#
#     for item_id in items:
#         item = FULL_DATA["food"][item_id]
#
#         if item["available"]:
#             available.append(food_line(item_id))
#         else:
#             sold_out.append(food_line(item_id))
#
#     heading("Available now")
#
#     if len(available) == 0:
#         line("Nothing available right now.")
#         print()
#     else:
#         box("ON SALE", available)
#
#     heading("Sold out")
#
#     if len(sold_out) == 0:
#         line("Nothing is sold out.")
#         print()
#     else:
#         box("SOLD OUT", sold_out)
#
#     line("Total items: " + str(len(items))
#                 + "   |   On sale: " + str(len(available))
#                 + "   |   Sold out: " + str(len(sold_out)))
#     print()
#
#
# def food_line(item_id):
#     """Turn one food item into a line of text for a box.
#
#     The columns are name, then ID, then price. py uses the
#     same helper from py, so both menus look the same.
#     """
#     item = FULL_DATA["food"][item_id]
#     name = pad_right(item["name"], 24) + item_id
#
#     return columns(name, money(item["price"]), 32)
#
#
# def add_food(username):
#     """Add one new food item to the restaurant's menu."""
#     heading("Add a new food item")
#
#     name = input("Name of the food: ")
#
#     if len(name) == 0:
#         warn("The name cannot be empty.")
#         return
#
#     # the name has to fit inside one line of the table, otherwise the
#     # table would run off the side of the screen
#     if len(name) > 24:
#         warn("Please keep the name under 25 letters.")
#         return
#
#     price = read_price()
#
#     if price is None:
#         return
#
#     item_id = new_food_id()
#
#     FULL_DATA["food"][item_id] = {
#         "name": name,
#         "price": price,
#         "restaurant": username,
#         "available": True,
#     }
#
#     save_data()
#
#     print()
#     ok("Added " + name + " as " + item_id + ".")
#
#
# def change_price(username):
#     """Change the price of one food item."""
#     heading("Change a price")
#     show_my_food(username)
#
#     item_id = ask_item_id(username, "change")
#
#     if item_id is None:
#         return
#
#     item = FULL_DATA["food"][item_id]
#     line("Current price of " + item["name"] + " is "
#                 + money(item["price"]))
#     print()
#
#     price = read_price()
#
#     if price is None:
#         return
#
#     item["price"] = price
#     save_data()
#
#     print()
#     ok("New price for " + item["name"] + " is " + money(price) + ".")
#
#
# def toggle_available(username):
#     """Mark an item as sold out, or put it back on sale."""
#     heading("Sold out, or back in stock?")
#     show_my_food(username)
#
#     item_id = ask_item_id(username, "toggle")
#
#     if item_id is None:
#         return
#
#     item = FULL_DATA["food"][item_id]
#
#     # "not" flips True into False and False into True
#     item["available"] = not item["available"]
#
#     save_data()
#
#     print()
#
#     if item["available"]:
#         ok(item["name"] + " is back on sale.")
#     else:
#         ok(item["name"] + " is marked sold out.")
#
#
# def delete_food(username):
#     """Delete one food item for good.
#
#     We warn the restaurant first, because this cannot be undone.
#     Old orders keep their own copy of the details, so past orders
#     are not affected by this.
#     """
#     heading("Delete a food item")
#     show_my_food(username)
#
#     item_id = ask_item_id(username, "delete")
#
#     if item_id is None:
#         return
#
#     name = FULL_DATA["food"][item_id]["name"]
#
#     print()
#     warn("This will remove " + name + " from your menu for good.")
#     answer = input("Type YES to confirm: ")
#
#     if answer != "YES":
#         line("Nothing was deleted.")
#         return
#
#     del FULL_DATA["food"][item_id]
#     save_data()
#
#     print()
#     ok("Deleted " + name + " (" + item_id + ").")
#
#
# # ============================================================
# #  THE RESTAURANT'S ORDERS
# #  The rules come from SPEC-orders.md:
# #    PLACED     the restaurant can accept it, or say no
# #    ACCEPTED   the restaurant can still back out
# #    PICKED_UP  too late, a rider is carrying it
# #    DELIVERED  finished, nobody may touch it again
# # ============================================================
#
#
# def my_orders(username):
#     """Return the IDs of every order placed at this """
#     orders = []
#
#     for order_id in FULL_DATA["orders"]:
#         if FULL_DATA["orders"][order_id]["restaurant"] == username:
#             orders.append(order_id)
#
#     return sorted(orders)
#
#
# def orders_with_status(username, wanted):
#     """Return this restaurant's orders that are in one of the given statuses.
#
#     wanted is a list, so that "PLACED" and "ACCEPTED" can both be asked
#     for in one call.
#     """
#     matching = []
#
#     for order_id in my_orders(username):
#         if FULL_DATA["orders"][order_id]["status"] in wanted:
#             matching.append(order_id)
#
#     return matching
#
#
# def show_orders(order_ids):
#     """Print a small table of orders, one row each."""
#     rows = []
#
#     for order_id in order_ids:
#         order = FULL_DATA["orders"][order_id]
#         customer = FULL_DATA["users"][order["customer"]]["name"]
#
#         left = pad_right(order_id, 8) \
#             + pad_right(customer, 20) \
#             + order["status"]
#
#         rows.append(columns(left, money(order["total"]), 44))
#
#     box("Order ID    Customer            Status", rows)
#
#
# def ask_order_id(username, action, allowed):
#     """Show the orders this restaurant may act on, and ask for one.
#
#     action is the word used in the question, like "accept".
#     allowed is a list of the statuses we are allowed to act on.
#
#     Returns the order ID, or None if nothing was chosen. The status is
#     checked here, not at each action, so a DELIVERED order can never be
#     reached by any of them.
#     """
#     open_orders = orders_with_status(username, allowed)
#
#     if len(open_orders) == 0:
#         warn("There is no order you can " + action + " right now.")
#         print()
#         return None
#
#     show_orders(open_orders)
#
#     print()
#     order_id = input("Which order to " + action + "? ").upper()
#
#     if order_id not in FULL_DATA["orders"]:
#         warn("No order found with the ID " + order_id + ".")
#         print()
#         return None
#
#     # the order exists, but it is not ours to touch. This one check
#     # stops us reaching another restaurant's orders, and stops us
#     # reaching a DELIVERED one, because those are never in open_orders.
#     if order_id not in open_orders:
#         warn("You cannot " + action + " that order.")
#         print()
#         return None
#
#     return order_id
#
#
# def accept_order(username):
#     """Say yes to an order that was just placed."""
#     heading("Accept an order")
#
#     order_id = ask_order_id(username, "accept", ["PLACED"])
#
#     if order_id is None:
#         return
#
#     order = FULL_DATA["orders"][order_id]
#     order["status"] = "ACCEPTED"
#     save_data()
#
#     print()
#     ok("Accepted " + order_id + ". A rider can now collect it.")
#     line("It stays this way until a rider takes it.")
#
#
# def reject_order(username):
#     """Say no to an order that was just placed."""
#     heading("Reject an order")
#
#     order_id = ask_order_id(username, "reject", ["PLACED"])
#
#     if order_id is None:
#         return
#
#     order = FULL_DATA["orders"][order_id]
#     order["status"] = "CANCELLED"
#     save_data()
#
#     print()
#     ok("Rejected " + order_id + ".")
#     line("It is now CANCELLED, and it will not reach the ")
#
#
# def cancel_order(username):
#     """Back out of an order we had already accepted."""
#     heading("Cancel an accepted order")
#
#     order_id = ask_order_id(username, "cancel", ["PLACED", "ACCEPTED"])
#
#     if order_id is None:
#         return
#
#     order = FULL_DATA["orders"][order_id]
#
#     # if a rider had already picked this up, let them off the hook,
#     # otherwise they would stay stuck as BUSY with no order to deliver
#     if order["rider"] is not None:
#         rider = FULL_DATA["riders"][order["rider"]]
#         rider["status"] = "FREE"
#         rider["order"] = None
#         line("Rider " + rider["name"] + " has been freed up.")
#
#     order["status"] = "CANCELLED"
#     save_data()
#
#     print()
#     ok("Cancelled " + order_id + ".")
#
#
# def order_history(username):
#     """Show every order this restaurant has ever had."""
#     heading("My orders")
#
#     mine = my_orders(username)
#
#     if len(mine) == 0:
#         warn("You have not received any orders yet.")
#         print()
#         return
#
#     show_orders(mine)
#
#     print()
#     line("Total orders received: " + str(len(mine)))
#     print()
#
#
# def restaurant_menu(username):
#     """Keep showing the restaurant menu until they choose to leave.
#
#     The name of the kitchen is printed once, by main.welcome(), at the
#     moment they sign in. Printing it again before every choice would
#     push the actual answer down the screen and out of view, so all
#     that is left here is the list of things they can do.
#     """
#
#     while True:
#         rule()
#
#         heading("What would you like to do?")
#         options([
#             "See my food",
#             "Add a new food item",
#             "Change a price",
#             "Sold out / back in stock",
#             "Delete a food item",
#             "See my orders",
#             "Accept an order",
#             "Reject an order",
#             "Cancel an accepted order",
#         ])
#
#         choice = input("Your choice: ")
#         print()
#
#         if choice == "1":
#             show_my_food(username)
#         elif choice == "2":
#             add_food(username)
#         elif choice == "3":
#             change_price(username)
#         elif choice == "4":
#             toggle_available(username)
#         elif choice == "5":
#             delete_food(username)
#         elif choice == "6":
#             order_history(username)
#         elif choice == "7":
#             accept_order(username)
#         elif choice == "8":
#             reject_order(username)
#         elif choice == "9":
#             cancel_order(username)
#         elif choice == "0":
#             line("Leaving the restaurant menu.")
#             print()
#             return
#         else:
#             warn("Please choose a number from 0 to 9.")
#             print()


# ---------------- PART: RIDER (claim, pickup, deliver) [rider.py] ----------------
# STATUS: PARKED - uncomment this whole part when its week comes.
# # This file holds everything a rider can do.
# #
# # A rider can:
# #   - see the orders waiting for someone to collect them
# #   - claim one, which locks them to that single order
# #   - mark it picked up
# #   - mark it delivered, which frees them up again
# #   - cancel an order they are holding, which also frees them up
# #
# # The lock is the whole point of this file. Each rider is either
# # FREE or BUSY. A BUSY rider cannot claim a second order, because a
# # rider can only carry one thing at a time.
#
# import design_helpers (same file)
# import customer_block (same file)
# from data_block import FULL_DATA, save_data
#
#
# def my_lock(username):
#     """Return this rider's own record from FULL_DATA["riders"]."""
#     return FULL_DATA["riders"][username]
#
#
# def open_orders():
#     """Return the orders that are waiting for a rider to collect them.
#
#     An order is waiting when the restaurant has accepted it and no
#     rider has taken it yet. That is status ACCEPTED and rider None.
#     """
#     waiting = []
#
#     for order_id in FULL_DATA["orders"]:
#         order = FULL_DATA["orders"][order_id]
#
#         if order["status"] == "ACCEPTED" and order["rider"] is None:
#             waiting.append(order_id)
#
#     return sorted(waiting)
#
#
# def order_line(order_id):
#     """Turn one order into a line of text for a box."""
#     order = FULL_DATA["orders"][order_id]
#     place = FULL_DATA["users"][order["restaurant"]]["name"]
#
#     # build a short description of what is inside, like "2x Margherita"
#     parts = []
#     for item_id in order["items"]:
#         name = FULL_DATA["food"][item_id]["name"]
#         parts.append(str(order["quantities"][item_id]) + "x " + name)
#
#     left = pad_right(order_id, 8) + pad_right(place, 18)
#     left = left + pad_right(", ".join(parts), 24)
#
#     return columns(left, money(order["total"]), 52)
#
#
# def show_open_orders():
#     """Show every order a rider is allowed to claim."""
#     waiting = open_orders()
#
#     if len(waiting) == 0:
#         heading("Orders waiting")
#         warn("No orders are waiting for a rider right now.")
#         print()
#         return []
#
#     heading("Orders waiting for collection")
#     box("Order    Restaurant", [order_line(o) for o in waiting])
#     line("Total waiting: " + str(len(waiting)))
#     print()
#
#     return waiting
#
#
# def ask_order_id(waiting, action):
#     """Ask which of the waiting orders we mean. Returns None if refused."""
#     if len(waiting) == 0:
#         warn("There is no order you can " + action + " right now.")
#         print()
#         return None
#
#     order_id = input("Which order to " + action + "? ").upper()
#
#     if order_id not in waiting:
#         warn("That order is not waiting to be collected.")
#         print()
#         return None
#
#     return order_id
#
#
# def claim_order(username):
#     """Take an order, and become BUSY holding it.
#
#     The four checks below are the whole lock. They are in this order
#     on purpose, so that a rider who is already busy is told the real
#     reason rather than a confusing one.
#     """
#     heading("Claim an order")
#
#     # 1. is the order there at all?
#     waiting = open_orders()
#
#     if len(waiting) == 0:
#         warn("No orders are waiting for a rider right now.")
#         print()
#         return
#
#     order_id = ask_order_id(waiting, "claim")
#
#     if order_id is None:
#         return
#
#     # 2. is this rider free? If not, they cannot take anything.
#     rider = my_lock(username)
#
#     if rider["status"] != "FREE":
#         warn("You are already delivering order "
#                     + str(rider["order"]) + ".")
#         line("Finish or cancel that one before claiming another.")
#         print()
#         return
#
#     # 3. stamp the order with this rider, and lock them to it
#     order = FULL_DATA["orders"][order_id]
#     order["rider"] = username
#
#     # 4. and now the rider is busy with exactly this one order
#     rider["order"] = order_id
#     rider["status"] = "BUSY"
#
#     save_data()
#
#     print()
#     ok("You claimed " + order_id + ". You are now BUSY.")
#     line("Mark it picked up when you have collected it.")
#
#
# def my_current_order(username):
#     """Return the ID of the order this rider is holding, or None."""
#     rider = my_lock(username)
#
#     if rider["status"] != "BUSY":
#         return None
#
#     return rider["order"]
#
#
# def pick_up(username):
#     """Say we have collected the food."""
#     heading("Mark picked up")
#
#     order_id = my_current_order(username)
#
#     if order_id is None:
#         warn("You are not carrying any order.")
#         line("Claim an order first, then you can mark it picked up.")
#         print()
#         return
#
#     order = FULL_DATA["orders"][order_id]
#
#     # the order must still be ACCEPTED. It cannot jump straight from
#     # claimed to delivered, because PICKED_UP is the step that proves
#     # the food actually moved.
#     if order["status"] != "ACCEPTED":
#         warn("Order " + order_id + " is not ACCEPTED any more.")
#         print()
#         return
#
#     order["status"] = "PICKED_UP"
#     save_data()
#
#     print()
#     ok("Order " + order_id + " is now PICKED_UP.")
#     line("Deliver it, then mark it delivered.")
#
#
# def deliver(username):
#     """Say the food has reached the customer, and free the rider up."""
#     heading("Mark delivered")
#
#     order_id = my_current_order(username)
#
#     if order_id is None:
#         warn("You are not carrying any order.")
#         print()
#         return
#
#     order = FULL_DATA["orders"][order_id]
#
#     # an order has to pass through PICKED_UP before it can be
#     # delivered, so this refuses if they skipped that step
#     if order["status"] != "PICKED_UP":
#         warn("Order " + order_id + " has not been picked up yet.")
#         line("Mark it picked up before marking it delivered.")
#         print()
#         return
#
#     order["status"] = "DELIVERED"
#
#     # the rider's lock is released, so they can claim another order
#     rider = my_lock(username)
#     rider["status"] = "FREE"
#     rider["order"] = None
#
#     save_data()
#
#     print()
#     ok("Order " + order_id + " is now DELIVERED.")
#     line("You are FREE again. Thank you.")
#
#     # the order has arrived, so this is the moment the customer gets
#     # their receipt
#     show_receipt(order_id)
#
#
# def cancel_order(username):
#     """Cancel the order we are carrying, and free the rider up."""
#     heading("Cancel the order you are carrying")
#
#     order_id = my_current_order(username)
#
#     if order_id is None:
#         warn("You are not carrying any order.")
#         print()
#         return
#
#     order = FULL_DATA["orders"][order_id]
#
#     # a delivered order is final, nobody may change it
#     if order["status"] == "DELIVERED":
#         warn("Order " + order_id + " is already delivered.")
#         line("A delivered order cannot be changed.")
#         print()
#         return
#
#     order["status"] = "CANCELLED"
#
#     # the lock is released, so the rider is not stuck as BUSY with
#     # nothing to deliver
#     rider = my_lock(username)
#     rider["status"] = "FREE"
#     rider["order"] = None
#
#     save_data()
#
#     print()
#     ok("Order " + order_id + " has been cancelled.")
#     line("You are FREE again.")
#
#
# def my_status(username):
#     """Show whether this rider is free or busy, and with what."""
#     heading("My status")
#
#     rider = my_lock(username)
#     name = rider["name"]
#
#     if rider["status"] == "FREE":
#         ok(name + " is FREE.")
#         line("You can claim any order that is waiting.")
#     else:
#         order_id = rider["order"]
#         order = FULL_DATA["orders"][order_id]
#         customer = FULL_DATA["users"][order["customer"]]["name"]
#
#         warn(name + " is BUSY with " + order_id + ".")
#         line("Status of that order: " + order["status"])
#         line("Delivering to " + customer + "  -  "
#                     + money(order["total"]))
#
#     print()
#
#
# def rider_menu(username):
#     """Keep showing the rider menu until they choose to leave.
#
#     The rider's name is printed once, by main.welcome(), at the moment
#     they sign in.
#
#     Whether the rider is FREE or BUSY is the one thing here that really
#     changes, so it is worth showing. It is printed only when it has
#     actually changed, which means a rider idly browsing the menu does
#     not push their own answer down the screen over and over.
#     """
#     last_status = ""
#
#     while True:
#         rule()
#
#         lock = my_lock(username)
#
#         if lock["status"] == "FREE":
#             status = "You are FREE. You can claim a waiting order."
#         else:
#             status = "You are BUSY carrying " + str(lock["order"]) + "."
#
#         if status != last_status:
#             line(status)
#             print()
#             last_status = status
#
#         heading("What would you like to do?")
#         options([
#             "See orders waiting",
#             "Claim an order",
#             "Mark picked up",
#             "Mark delivered",
#             "Cancel the order I am carrying",
#             "My status",
#         ])
#
#         choice = input("Your choice: ")
#         print()
#
#         if choice == "1":
#             show_open_orders()
#         elif choice == "2":
#             claim_order(username)
#         elif choice == "3":
#             pick_up(username)
#         elif choice == "4":
#             deliver(username)
#         elif choice == "5":
#             cancel_order(username)
#         elif choice == "6":
#             my_status(username)
#         elif choice == "0":
#             line("Leaving the rider menu.")
#             print()
#             return
#         else:
#             warn("Please choose a number from 0 to 6.")
#             print()


# ---------------- PART: REPORTS (owner sales) [reports.py] ----------------
# STATUS: PARKED - uncomment this whole part when its week comes.
# # This file holds the three reports the store owner can see.
# #
# # The owner can:
# #   - see total sales
# #   - see how many orders were cancelled, and how much money that cost
# #   - see which food item sells the best
# #
# # IMPORTANT: nothing in this file ever changes an order. Reports only
# # read the data. If a mistake happened in here, it must not be able to
# # damage the thing being reported on.
#
# import design_helpers (same file)
# from data_block import FULL_DATA
#
#
# def all_orders():
#     """Return every order ID we have."""
#     orders = []
#
#     for order_id in FULL_DATA["orders"]:
#         orders.append(order_id)
#
#     return sorted(orders)
#
#
# def orders_with_status(status):
#     """Return every order ID that is in one given status."""
#     matching = []
#
#     for order_id in all_orders():
#         if FULL_DATA["orders"][order_id]["status"] == status:
#             matching.append(order_id)
#
#     return matching
#
#
# def sum_of_totals(order_ids):
#     """Add up the stored total of each order we were given.
#
#     We read order["total"] and never work it out again from the food
#     prices. The total was worked out once, when the order was made,
#     and it is only ever read after that.
#     """
#     amount = 0.0
#
#     for order_id in order_ids:
#         amount = amount + FULL_DATA["orders"][order_id]["total"]
#
#     return round(amount, 2)
#
#
# # ----------------------------------------------------------------
# #  REPORT 1 - TOTAL SALES
# # ----------------------------------------------------------------
#
#
# def total_sales():
#     """Work out the total money earned from delivered orders."""
#     return sum_of_totals(orders_with_status("DELIVERED"))
#
#
# # ----------------------------------------------------------------
# #  REPORT 2 - CANCELLED ORDERS, AND WHAT THEY COST US
# # ----------------------------------------------------------------
#
#
# def cancelled_count():
#     """How many orders were cancelled."""
#     return len(orders_with_status("CANCELLED"))
#
#
# def money_lost():
#     """How much money the cancelled orders were worth.
#
#     This is NOT subtracted from the sales figure. It is shown on its
#     own line, because hiding it would hide a real problem.
#     """
#     return sum_of_totals(orders_with_status("CANCELLED"))
#
#
# # ----------------------------------------------------------------
# #  REPORT 3 - BEST SELLING ITEM
# # ----------------------------------------------------------------
#
#
# def best_seller():
#     """Work out which food item has sold the most, and what it made.
#
#     Only DELIVERED orders are counted. An order that was cancelled
#     never sold anything, and one that is still on the way has not sold
#     anything yet.
#
#     We count using the quantities dictionary, NOT the items list.
#
#     That is the one decision worth explaining. Look at this order:
#
#         "items"       ["F101"]              what was ordered
#         "quantities"  {"F101": 2}           how many of each
#
#     F101 is written down only ONCE in the items list, even though two
#     pizzas were ordered. So counting the items list would tell us one
#     pizza was sold, when two actually left the kitchen. The quantities
#     dictionary already has the real number, so we just read it.
#
#     Returns a list of three things:
#
#         [ the food's ID , times sold , money made ]
#
#     For example ["F101", 5, 1250.00]. Returns None if nothing has been
#     delivered yet, because then there is no best seller to name.
#     """
#     counts = {}
#
#     # 1. add up how many of each item went out in a delivered order
#     for order_id in orders_with_status("DELIVERED"):
#         order = FULL_DATA["orders"][order_id]
#
#         for item_id in order["quantities"]:
#             how_many = order["quantities"][item_id]
#
#             # .get means "give me this value if it is there, and if it
#             # is not there give me 0 instead of stopping the program."
#             already = counts.get(item_id, 0)
#             counts[item_id] = already + how_many
#
#     # 2. nothing was delivered, so there is no best seller
#     if len(counts) == 0:
#         return None
#
#     # 3. walk through the counts and keep whichever is highest
#     best_id = None
#     best_count = 0
#
#     for item_id in counts:
#         if counts[item_id] > best_count:
#             best_count = counts[item_id]
#             best_id = item_id
#
#     # 4. now work out how much money that one item brought in
#     money = 0.0
#
#     for order_id in orders_with_status("DELIVERED"):
#         order = FULL_DATA["orders"][order_id]
#
#         if best_id in order["quantities"]:
#             how_many = order["quantities"][best_id]
#
#             # the item might have been deleted from the menu after it
#             # was sold, so check before we use its price
#             item = FULL_DATA["food"].get(best_id)
#
#             if item is not None:
#                 money = money + item["price"] * how_many
#
#     return [best_id, best_count, round(money, 2)]
#
#
# def owner_menu(username):
#     """Keep showing the owner menu until they choose to leave.
#
#     The owner is signed in once, and main.welcome() already says so.
#     Nothing about the owner changes from one choice to the next, so
#     there is nothing here that needs to be printed again.
#     """
#
#     while True:
#         rule()
#
#         heading("What would you like to see?")
#         options([
#             "Total sales",
#             "Cancelled orders",
#             "Best selling item",
#             "Everything on one page",
#         ])
#
#         choice = input("Your choice: ")
#         print()
#
#         if choice == "1":
#             show_sales()
#         elif choice == "2":
#             show_cancelled()
#         elif choice == "3":
#             show_best_seller()
#         elif choice == "4":
#             show_everything()
#         elif choice == "0":
#             line("Leaving the owner menu.")
#             print()
#             return
#         else:
#             warn("Please choose a number from 0 to 4.")
#             print()
#
#
# def show_sales():
#     """Print the total sales report."""
#     heading("Total sales")
#
#     delivered = orders_with_status("DELIVERED")
#     money = total_sales()
#
#     box("Total sales", [
#         "Orders delivered : " + str(len(delivered)),
#         "Total sales      : " + money(money),
#     ])
#
#     line("Only DELIVERED orders are counted here.")
#     print()
#
#     return money
#
#
# def show_cancelled():
#     """Print the cancelled orders report."""
#     heading("Cancelled orders")
#
#     cancelled = orders_with_status("CANCELLED")
#     lost = money_lost()
#
#     lines = [
#         "Cancelled orders : " + str(len(cancelled)),
#         "Money lost       : " + money(lost),
#     ]
#
#     # show each cancelled order on its own row, so the owner can see
#     # exactly which ones went wrong
#     for order_id in cancelled:
#         order = FULL_DATA["orders"][order_id]
#         customer = FULL_DATA["users"][order["customer"]]["name"]
#         lines.append("")
#         lines.append(columns(order_id + "  -  " + customer,
#                                     money(order["total"]), 32))
#
#     box("Cancellations", lines)
#
#     line("This is kept separate from sales, on purpose.")
#     print()
#
#     return lost
#
#
# def show_best_seller():
#     """Print the best selling item report."""
#     heading("Best selling item")
#
#     result = best_seller()
#
#     if result is None:
#         warn("Nothing has been delivered yet.")
#         line("So there is no best selling item to show.")
#         print()
#         return
#
#     item_id = result[0]
#     count = result[1]
#     money = result[2]
#
#     # the item may have been taken off the menu since it was sold
#     item = FULL_DATA["food"].get(item_id)
#
#     if item is None:
#         name = "(removed from menu)"
#     else:
#         name = item["name"]
#
#     box("Best seller", [
#         "Item        : " + name,
#         "Food ID     : " + item_id,
#         "Sold        : " + str(count) + " time(s)",
#         "Money made  : " + money(money),
#     ])
#
#     print()
#
#     return result
#
#
# def show_everything():
#     """Print all three reports on one page."""
#     heading("All reports")
#     print()
#
#     show_sales()
#     show_cancelled()
#     show_best_seller()
#
#     line("That is every report CraveFlow can produce.")
#     print()
