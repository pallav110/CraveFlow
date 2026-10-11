# Capability Map: CraveFlow

> Approved 2026-10-11 · Food Delivery Management System Using Python
> Tagline: *From craving to delivery, seamlessly.*

This map is the index. Each module below has its own spec file, named by module id.
Module ids are stable — never renamed mid-project.

---

## Modules

| Module id | Responsibility | Actor | Depends on | Spec |
|---|---|---|---|---|
| `accounts` | Who is signed in, what role they have, demo logins | — | — | `SPEC-accounts.md` |
| `menu` | Food items — name, price, availability | restaurant | `accounts` | `SPEC-menu.md` |
| `orders` | Placing an order, its status, cancellation | customer, restaurant | `accounts`, `menu` | `SPEC-orders.md` |
| `delivery` | Rider claims work, picks up, delivers | rider | `orders` | `SPEC-delivery.md` |
| `reports` | Sales total, cancelled count, best-selling item | all | `orders` | `SPEC-reports.md` |

## Build order

```
accounts ──▶ menu ──▶ orders ──▶ delivery ──▶ reports
                                        ▲          │
                                        └──────────┘
                              (reports reads orders;
                               orders does NOT read reports)
```

Nothing flows backwards. If two modules ever need each other, they are one module.

---

## The file layout

**Capability modules are not the same thing as files.** Modules describe *what the
system does*; files describe *who is acting*. Files are organised by person, because
"everything a customer can do" is a sentence a 16-year-old can say in a viva without
using the word "architecture".

| File | Implements | Why this file exists |
|---|---|---|
| `main.py` | `accounts` | Starts the program, login loop, sends you to the right menu |
| `data.py` | `accounts` | The one dictionary, plus save and load |
| `customer.py` | `orders` | Everything a customer can do |
| `restaurant.py` | `menu` + part of `orders` | Everything a restaurant can do |
| `rider.py` | `delivery` | Everything a rider can do |
| `reports.py` | `reports` | Everything the owner can look at |

No `src/`. No `tests/`. No `__init__.py`. No `requirements.txt` — nothing to install.

---

## Cross-cutting decisions

| Decision | Choice | Why |
|---|---|---|
| Persistence | `json.dump()` / `json.load()` | Two function calls; survives a viva |
| Login | Hardcoded demo accounts in `DATA` | Avoids password storage entirely |
| Money type | `float`, rounded to 2 places | `round()` is already taught |
| Order IDs | `"O" + str(len(orders) + 1001)` | No import, no counter variable |
| Item IDs | `"F" + str(len(food) + 101)` | Same pattern |
| Rider assignment | Rider claims their own work | Realistic flow; needs the FREE/BUSY lock |
| Cancelled orders | Counted in a separate report line | Never folded into sales |

---

## Resolved decisions

| Question | Decision |
|---|---|
| Delivery fee | **Per restaurant.** Each restaurant stores its own `fee`; an order reads the fee from the restaurant it belongs to |
| Multiple items per order | **Yes.** A list of item ids, with a parallel `quantities` dictionary |
| One active order per customer | **Yes.** At most one order in `PLACED` / `ACCEPTED` / `PICKED_UP` |
| Best-seller counting | **By quantity.** Read the `quantities` dictionary rather than re-counting occurrences |
| Per-restaurant sales breakdown | **Cut.** One combined total is enough; a breakdown is YAGNI for now |