# Spec: menu

> Module id: `menu` · Build order: 2 of 5
> Implements: `restaurant.py`

---

## Objective

A restaurant can add food items, change their price, hide one when it sells out, and
delete one. A customer can see what is available and what it costs.

The menu is a **dictionary of dictionaries** inside `DATA["food"]`.

---

## The data

```python
DATA["food"] = {
    "F101": {"name": "Margherita Pizza", "price": 250.00,
             "restaurant": "dominoes", "available": True},
    "F102": {"name": "Garlic Bread", "price": 120.00,
             "restaurant": "dominoes", "available": False},
}
```

| Field | Type | Why |
|---|---|---|
| `name` | string | Shown to the customer |
| `price` | float | Money. Rounded to 2 places on display |
| `restaurant` | string | **The owner's username, not the display name.** Which restaurant owns this item |
| `available` | bool | `False` means sold out — hidden from customers, still visible to the owner |

### Why `restaurant` holds the username

`"restaurant": "Domino's"` looks nicer but breaks as soon as a name contains an apostrophe
or a quote. Worse, it means looking up the display name later. Storing the username means
the key used elsewhere in `DATA` is the same key used here.

**Viva answer:** *"Each food item is a dictionary. I store the restaurant's username in it,
so when a restaurant logs in I can find all the items that belong to them."*

---

## Behaviours

### Add an item

Asks name, price, then saves. The ID is generated — never typed by hand.

```python
item_id = "F" + str(len(DATA["food"]) + 101)
```

Length of a dictionary is how many items exist, so this always produces a fresh id. No
counter variable, no import. **Viva answer:** *"I made the ID using the length of the
dictionary plus 101, so it always makes a new one."*

Price validation: reject anything that is not a number, and reject negatives.

```python
price_text = input("Price: ")
if not price_text.replace(".", "", 1).isdigit():
    print("Please enter a number.")
elif float(price_text) < 0:
    print("Price cannot be negative.")
else:
    DATA["food"][item_id] = {...}
```

`.isdigit()` and `.replace()` are both on the taught list.

### Show the menu

Only items where `item["restaurant"] == username` — the owner sees their own food,
including sold-out items, with the unavailable ones marked.

### Change a price

Looks up the item, asks for a new price, validates the same way, saves.

### Toggle availability

`item["available"] = not item["available"]` — the `not` keyword, flipping the flag.

### Delete an item

Removed with `del DATA["food"][item_id]`. If any existing order already references that
id, the order still shows it — the order keeps its own copy of what was ordered, so
history stays truthful. See `SPEC-orders.md`.

---

## Success criteria

- [ ] A restaurant sees only its own items, never another restaurant's
- [ ] Item IDs are generated and never repeat
- [ ] A non-numeric or negative price is rejected with a clear message
- [ ] Toggling availability flips `True` and `False` and back
- [ ] An item added this run survives the next run
- [ ] Sold-out items are hidden from the customer view and shown to the owner

---

## Boundaries

**Never** — let a user type an item ID · store the display name where a username belongs ·
delete an order's history when a menu item is deleted.