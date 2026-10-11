# Spec: accounts

> Module id: `accounts` · Build order: 1 of 5
> Implements: `main.py`, `data.py`

---

## Objective

Let someone sign in, and let CraveFlow know **which of the three menus to show them**.

There is no real authentication. Passwords are stored in plain text in `data.py` and
compared directly. This is a deliberate trade-off, not an oversight — see
[B](#why-hardcoded-logins-are-correct-here).

**Viva answer:** *"I stored the demo logins in a dictionary. When someone types their
username, Python looks up that key and gets their role back."*

---

## The data

One dictionary lives in `data.py`. Four top-level keys, nested dictionaries inside.

```python
DATA = {
    "users": {
        "yajat":    {"name": "Yajat Sharma", "role": "customer",   "password": "1234"},
        "dominoes": {"name": "Domino's",      "role": "restaurant", "password": "1234", "fee": 40.00},
        "raj":      {"name": "Raj Kumar",     "role": "rider",      "password": "1234"},
        "owner":    {"name": "Owner",         "role": "owner",      "password": "1234"},
    },

    "food": {},

    "orders": {},

    "riders": {
        "raj": {"name": "Raj Kumar", "status": "FREE", "order": None},
    },
}
```

### Why this shape

- **`users` keyed by username.** A login is then one `in` check and one lookup — no
  searching through a list, which is the part beginners get wrong.
- **`role` as a string, not a number.** `if role == "restaurant"` is readable aloud.
  A `0` or `1` would force him to remember which is which.
- **`riders` is separate from `users`.** A rider has extra state (busy or free, which
  order). Keeping it separate means the rider fields never have to be explained away
  for customers and restaurants, which do not have them.

---

## Behaviour

### Login

```
Username: yajat
Password: ****
→ Signed in as Yajat Sharma (customer)
```

| Situation | Response |
|---|---|
| Username not in `DATA["users"]` | `No account found with that username.` |
| Password wrong | `Wrong password.` |
| Correct | Store the username, show their menu |

Both failures re-prompt. The loop only ends on success or on the literal word `exit`.

The order of these checks matters. We look at the word `exit` **before** asking for a
password, because someone who has decided to leave should never be stopped by a
question they have no reason to answer. Ask the cheap question that can end the loop
first, then pay for the one that cannot.

```python
def login():
    while True:
        username = input("Username: ")
        if username == "exit":
            return None
        if username not in DATA["users"]:
            print("No account found with that username.")
            continue
        if input("Password: ") != DATA["users"][username]["password"]:
            print("Wrong password.")
            continue
        return username
```

`if/elif/else`, `while`, `in`, `!=`, `continue` — every one of these is on the taught list.

### Routing

`main.py` reads the role once, then runs the matching menu loop.

```python
role = DATA["users"][username]["role"]

if role == "customer":
    customer_menu(username)
elif role == "restaurant":
    restaurant_menu(username)
elif role == "rider":
    rider_menu(username)
else:
    owner_menu(username)
```

### Sign out

Returns to the login loop. **Saves the data first** — otherwise everything typed since
the last save is lost, which is the single most annoying bug a demo can have.

---

## Persistence

| Direction | Call | When |
|---|---|---|
| Load | `json.load(f)` | Once, at program start |
| Save | `json.dump(DATA, f)` | On every change, and always on sign-out |

Save on every change rather than only at exit, so a crash mid-demo cannot lose an order
that was already taken.

**Viva answer:** *"I used the `json` module — `json.dump` writes my dictionary to a file
and `json.load` reads it back when the program starts again."*

---

## Why hardcoded logins are correct here

A real login means storing a password, comparing it in a way that is not trivially
guessable, and deciding what happens after too many wrong attempts. That is three
separate concepts stacked on a `while` loop, and each one becomes its own viva question.

A dictionary of demo accounts is **one structure, one lookup, one sentence**. The
multi-role structure survives intact — customers, restaurants, riders and the owner all
still exist and all still get different menus — while the hardest part is avoided.

---

## Success criteria

- [ ] Four demo accounts load from `data.json`, and three when the file does not exist
- [ ] Wrong username and wrong password each give their own message, then re-prompt
- [ ] Typing `exit` at the username prompt returns to the shell without a traceback
- [ ] Correct login routes to the menu for that role
- [ ] Signing out saves the file
- [ ] An item added in one run is still there in the next

---

## Boundaries

**Always** — save after every change · name every variable something a person would say ·
use `snake_case` for functions and variables.

**Ask first** — adding a module or a dependency · renaming a module id · changing the
data shape.

**Never** — use classes, decorators, type hints, `try`/`except`, or `import` beyond
`json` · add a `tests/` folder · add a file whose purpose needs the word "architecture"
to explain.