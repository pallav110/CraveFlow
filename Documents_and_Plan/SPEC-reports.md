# Spec: reports

> Module id: `reports` · Build order: 5 of 5
> Implements: `reports.py`

---

## Objective

Show what the business earned, how much it lost to cancellations, and what sells best.

Reports only ever **read** the data. They never change an order's status — a mistake in
here must not be able to damage the thing being reported on.

---

## The three reports

### 1. Total sales

Counts every order whose status is `DELIVERED`.

```python
for order_id in DATA["orders"]:
    if DATA["orders"][order_id]["status"] == "DELIVERED":
        total_sales += DATA["orders"][order_id]["total"]
```

Cancelled and in-flight orders are excluded. A total that quietly includes cancelled
orders is a number nobody trusts.

### 2. Cancelled orders

Shown as a **separate line**, never folded into sales.

```
Cancelled orders : 2
Money lost       : 490.00
```

Including this is the point. Too many cancellations is a real signal — it usually means
food quality, pricing, or a restaurant taking orders it cannot handle. Hiding it would
hide the problem.

### 3. Best-selling item

Counts every occurrence across all `DELIVERED` orders, then takes the highest.

```python
item_count = {}
for order_id in DATA["orders"]:
    if DATA["orders"][order_id]["status"] == "DELIVERED":
        for item_id in DATA["orders"][order_id]["items"]:
            item_count[item_id] = item_count.get(item_id, 0) + 1
```

`item_count.get(item_id, 0)` is the pattern worth understanding: "if this item is not in
the counting dictionary yet, start it at zero, otherwise use what it has." It is also
`.get()` from the taught list.

The quantity dictionary in `SPEC-orders.md` already holds the exact count — a customer who
orders two pizzas is recorded as `{"F101": 2}`. So the report **reads that dictionary**
rather than re-counting occurrences. Re-counting would give the same answer for simple
orders and a wrong one the moment a quantity above one appears.

---

## Formatting money

Every amount prints with exactly two decimal places: `round(amount, 2)`.

A float like `260.49000000000001` on screen looks like a bug, and it will be. Rounding
on **display only** — the stored number is untouched.

---

## Success criteria

- [ ] Total sales counts only `DELIVERED` orders
- [ ] Cancelled orders are counted and shown on their own line
- [ ] Cancelled orders never appear in total sales
- [ ] Best-selling item handles an item with no delivered orders
- [ ] An empty system shows zeroes, not a crash
- [ ] Every money value prints with exactly 2 decimal places
- [ ] No report function modifies any order

---

## Open questions

1. **Quantities vs. occurrences.** The order stores both `items` and `quantities`.
   Counting *occurrences* means "ordered 2 pizzas" counts as 2. Counting *distinct item
   ids* would count it as 1 line. Occurrences is the correct reading, but the `quantities`
   dictionary already holds it exactly — worth deciding which the report uses.
2. **Per-restaurant breakdown.** Currently one combined total. Splitting by restaurant
   means grouping orders by their `restaurant` field.

---

## Boundaries

**Always** — round on display · handle the empty case explicitly · keep cancelled money
on its own line.

**Never** — modify an order while reporting on it · round a stored total · fold
cancellations into sales.