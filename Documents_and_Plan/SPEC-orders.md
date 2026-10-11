# Spec: orders

> Module id: `orders` · Build order: 3 of 5
> Implements: `customer.py`, and the accept/reject half of `restaurant.py`

---

## Objective

A customer places an order from the menu. A restaurant accepts or rejects it. Either can
cancel. The order's status is always current and never set from two places at once.

This is the keystone module. `menu` and `delivery` both depend on it.

---

## The data

```python
DATA["orders"] = {
    "O1001": {
        "customer": "yajat",
        "items": ["F101", "F102"],       # item ids, in a list
        "quantities": {"F101": 2, "F102": 1},
        "restaurant": "dominoes",
        "total": 620.00,                  # stored once, never recomputed
        "status": "PLACED",
        "rider": None,                    # set by a rider in `delivery`
    },
}
```

### Why the total is stored, not recomputed

`250.00 * 2 + 120.00` is fine. But computing it fresh every time it is displayed means
rounding can drift between two views of the same order. **Compute once, at creation,
then read it forever.**

```python
fee = DATA["users"][restaurant]["fee"]
total = round(food_subtotal + fee, 2)
```

Each restaurant carries its own `fee`, read from the restaurant's own record. This is
why `fee` lives on the restaurant's entry and not as one global constant — it also makes
a better answer when asked why the fee differs between restaurants.

### Why quantities are a dictionary next to the item list

The items list says *what*. The quantities dictionary says *how many of each*. Splitting
them means an order can hold two of one item and one of another without inventing a
`"F101 x2"` string that would need splitting back apart later.

---

## The status flow

```
                    ┌── restaurant rejects ───┐
                    │        (any status before PICKED_UP)
                    ▼                        │
PLACED ──restaurant accepts──▶ ACCEPTED ──rider claims──▶ PICKED_UP ──rider delivers──▶ DELIVERED
   │                              │
   │ customer cancels             │
   ▼                              ▼
CANCELLED ◀───────────────────────┘
```

| From | To | Who | Allowed? |
|---|---|---|---|
| PLACED | ACCEPTED | restaurant | yes |
| PLACED | CANCELLED | customer | yes |
| ACCEPTED | PICKED_UP | rider | via `delivery` |
| PICKED_UP | DELIVERED | rider | yes |
| any pre-delivery | CANCELLED | customer or restaurant | yes |
| DELIVERED | anything | — | **no. ever.** |

### The one rule that matters

**A delivered order is final.** Nothing changes it. This is the single most important
business rule in the project, and the reason `reports` can trust its numbers.

---

## Validation before an order is created

An order is only created if **all** of these hold:

- [ ] The customer has at least one available item selected
- [ ] Every selected item belongs to **one** restaurant — an order cannot span two
      kitchens, because a single rider carries one order
- [ ] Every selected item is `available`
- [ ] The customer has not already got an order in status `PLACED`, `ACCEPTED`, or
      `PICKED_UP`

The last rule is a design decision, not a law of nature. An alternative is to allow many
concurrent orders. **This is flagged as an assumption below** — it is the kind of choice
worth arguing about out loud in a viva.

---

## Success criteria

- [ ] An order cannot be created spanning two restaurants
- [ ] An unavailable item cannot be ordered
- [ ] The total is stored once and reads identically everywhere afterwards
- [ ] The total is rounded to 2 decimal places on every display
- [ ] A delivered order rejects every further status change
- [ ] A cancelled order keeps its items and total, for the report
- [ ] Order IDs are generated and never repeat, even after cancellations

---

## Resolved decisions

1. **One active order per customer — yes.** Confirmed. A customer holds at most one
   order in `PLACED`, `ACCEPTED`, or `PICKED_UP` at a time. Keeps the demo legible and
   the rule easy to state.
2. **Delivery fee — per restaurant.** Each restaurant stores its own `fee`. An order
   reads the fee from the restaurant it belongs to.
3. **Cancelling after `ACCEPTED` — both roles, plus the rider.** A customer or restaurant
   may cancel before pickup; a rider may cancel an order they hold. All three release the
   rider's lock.

---

## Boundaries

**Always** — store the total once at creation · round to 2 places on display · keep a
cancelled order's data intact.

**Never** — recompute a total from scratch when displaying · let a status change skip a
step · modify a `DELIVERED` order · let an order span two restaurants.

---

## Resolved by implementation (2026-10-11)

**The restaurant cannot cancel a `PICKED_UP` order.** `cancel_order()` offers only
`PLACED` and `ACCEPTED`. Once a rider is physically carrying the food, the order leaves
that state through the rider's own cancel, or it does not leave at all.

The spec's table says "any pre-delivery — customer or restaurant — yes". This narrowed
one row of it, on purpose: cancelling from `PICKED_UP` would leave the rider marked `BUSY`
holding an order that no longer exists. The narrower rule has no stranded state.

Note that a restaurant cancelling an `ACCEPTED` order *does* free the rider, because at
that point a rider can already have claimed it. That case is handled and verified.