# ============================================================
# CraveFlow - Food Delivery Management System
# From craving to delivery, seamlessly.
#
# Student : Yajat Sharma
# Class   : 11-A
#
# Run with F5 in IDLE.
# TIP: Options > Configure IDLE > Fonts/Tabs > choose Consolas
#      so that the big block letters line up properly.
# ============================================================

# ---------- 1. DATA (our small database using a nested dictionary) ----------

WIDTH = 70
TAGLINE = "From craving to delivery, seamlessly."

USERS = {
    "yajat": {"name": "Yajat Sharma", "password": "1234", "role": "customer"},
}

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


# ---------- 4. MAIN PROGRAM ----------

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


main()
