# Spec: delivery

> Module id: `delivery` · Build order: 4 of 5
> Implements: `rider.py`

---

## Objective

A rider sees the orders waiting for someone to collect them, claims one, marks it picked
up, then marks it delivered. A rider holds **at most one order at a time**.

The rider finds work themselves. Nobody assigns it to them.

---

## The data

```python
DATA["riders"] = {
    "raj": {"name": "Raj Kumar", "status": "FREE", "order": None},
}
```

| Field | Values | Meaning |
|---|---|---|
| `status` | `FREE` / `BUSY` | The lock. A busy rider cannot claim again |
| `order` | `"O1001"` or `None` | Which order they hold |

The lock is the whole module. Two riders claiming the same order, or one rider claiming
two orders, are both one missing check.

**Viva answer:** *"I gave each rider a status. It is FREE or BUSY. A rider can only pick
up a new order if their status is FREE, and it becomes BUSY when they take one."*

---

## Behaviours

### See available orders

Every order with status `ACCEPTED` and `rider` set to `None`. Shows the order id, the
restaurant, the items, and the total.

### Claim an order

```
1. Look up the order id.
2. If it does not exist            → "No order found with that ID."
3. If its status is not ACCEPTED   → "That order is not available."
4. If this rider is not FREE       → "You are already delivering an order."
5. Otherwise: set order["rider"], set rider["order"], set rider["status"] = "BUSY"
```

Steps 2–4 are the whole race-condition guard. Order matters: **check availability before
checking your own lock**, so a rider who is busy sees the real reason rather than a
confusing one.

### Mark picked up

Only if the rider holds that order and it is `ACCEPTED`. Sets status to `PICKED_UP`.
The rider stays `BUSY`.

### Mark delivered

Only if the rider holds that order and it is `PICKED_UP`. Sets status to `DELIVERED`,
then sets `rider["order"] = None` and `rider["status"] = "FREE"`.

The order **must** pass through `PICKED_UP`. Letting a rider jump straight from claiming
to delivered would skip the only state that proves the food physically moved.

### Cancellation, from the rider's side

A rider may cancel an order they hold, if it is not yet `DELIVERED`. Their lock is
released and the order goes to `CANCELLED`.

---

## Success criteria

- [ ] A rider sees exactly the `ACCEPTED` orders with no rider assigned
- [ ] A busy rider is told they are already delivering, and is not offered a second
- [ ] Claiming sets the rider to `BUSY` and stamps the order with their username
- [ ] Delivering releases the rider back to `FREE`
- [ ] An order cannot skip `PICKED_UP`
- [ ] A cancelled order releases the rider's lock
- [ ] Claiming the same order twice from one rider is refused

---

## Boundaries

**Never** — let a rider claim while `BUSY` · skip `PICKED_UP` · leave a rider `BUSY`
after a cancellation · overwrite an order that already has a rider.