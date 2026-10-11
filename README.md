# CraveFlow

**Food Delivery Management System Using Python**
*From craving to delivery, seamlessly.*

A terminal-based food delivery system where customers order, restaurants manage their
menu, riders deliver, and the owner sees the numbers.

---

## Run it

```
python main.py
```

Nothing to install. No `pip install`, no `requirements.txt` — Python's standard library
is all it uses.

---

## Demo logins

| Username | Password | Role |
|---|---|---|
| `yajat` | `1234` | Customer |
| `dominoes` | `1234` | Restaurant (Domino's Pizza) |
| `tandoor` | `1234` | Restaurant (Tandoor House) |
| `raj` | `1234` | Rider |
| `meera` | `1234` | Rider |
| `owner` | `1234` | Owner |

Type `exit` at the username prompt to quit.

Every account uses the password `1234`. Sign in as different people to see the
different menus — a restaurant can only see its own food, and a customer can
only see their own orders.

**To show the whole flow**, run the four roles in this order, signing out of
each one (`0. Go back`) before signing in as the next:

| Step | Sign in as | Do this |
| --- | --- | --- |
| 1 | `yajat` | **Place a new order** → pick a kind of food, a kitchen, then a dish |
| 2 | `tandoor` (or whichever kitchen took it) | **Accept an order** |
| 3 | `raj` | **Claim an order**, then **Mark picked up**, then **Mark delivered** |
| 4 | `owner` | **Total sales** and **Best selling item** |

**Place a new order** and **See food by type** both ask the same way and end in
the same place — the only difference is the first heading you see. Use **See
food by type** if a teacher asks how the browsing works, and **Place a new
order** if they just want the food moving.

Because saving is switched off, start again from step 1 for a second run — the
demo data resets itself every time.

---

## Files

```text
CraveFlow/
  main.py                  Starts the program
  python_project_modules/  Everything else lives in here
```

| File | What it does |
|---|---|
| `main.py` | Starts the program, asks who you are, opens the right menu |
| `python_project_modules/data.py` | The one dictionary that holds everything |
| `python_project_modules/design.py` | The colours, the logo, and the boxes. Written once so they match everywhere |
| `python_project_modules/customer.py` | Everything a customer can do |
| `python_project_modules/restaurant.py` | Everything a restaurant can do |
| `python_project_modules/rider.py` | Everything a rider can do |
| `python_project_modules/reports.py` | Sales, cancellations, and best-selling item |

Files are named after the *person* who uses them, not after what happens
inside them. `customer.py` is "everything a customer can do" — it needs no
vocabulary to explain.

Everything except `main.py` sits in one folder called `python_project_modules`,
because all six are the same kind of thing — supporting files. `main.py` stays
on its own because it is the one file you actually run.

### Saving your changes

Saving is switched off. The data lives only while the program is open, so it
always starts from exactly the same demo data every time — which makes a demo
much easier to follow, because the person watching sees the same flow the same
way on every run.

Nothing had to change elsewhere: `save_data()` is still called everywhere it
always was, it just has nothing to do yet. Putting saving back is a job of
writing the body of that one function.

### The logo

A terminal cannot show a picture file — it can only print characters. So the
logo is drawn out of one character, the block character `█`, arranged as five
rows per letter in `design.py`.

We did not use a picture-to-text conversion, because that would need an extra
library. Instead, each of the nine letters is five ordinary strings in the
`FONT` dictionary, and `make_logo()` puts them side by side.

The block character is not a normal letter, which is exactly why it makes a
logo look like a logo instead of a sentence. A Windows terminal prints with
UTF-8, so it displays correctly. If the letters ever came out as `?` or empty
boxes, the terminal was not UTF-8, and the fix would be to replace every `█`
with `#` in `FONT`.

---

## Documentation

- [`CAPABILITY-MAP.md`](Documents_and_Plan/CAPABILITY-MAP.md) — what the system is built from, and in what order
- [`SPEC-accounts.md`](Documents_and_Plan/SPEC-accounts.md) — sign in, roles, saving and loading
- [`SPEC-menu.md`](Documents_and_Plan/SPEC-menu.md) — food items and prices
- [`SPEC-orders.md`](Documents_and_Plan/SPEC-orders.md) — placing orders and the status flow
- [`SPEC-delivery.md`](Documents_and_Plan/SPEC-delivery.md) — riders claiming work
- [`SPEC-reports.md`](Documents_and_Plan/SPEC-reports.md) — sales and cancellations

---

**Submitted by:** Yajat Sharma · Class 11-A · Somerville School, Noida Sector 22