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

