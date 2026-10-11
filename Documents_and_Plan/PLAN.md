# Implementation Plan: CraveFlow

> Approved spec set · 2026-10-11
> Read `CAPABILITY-MAP.md` and the five `SPEC-*.md` files first.

---

## Build strategy: vertical slices, not layers

We do **not** build all the data functions first, then all the menus. Each task below
produces something you can actually run and click through. After Task 3 the program
already logs in; after Task 4 a restaurant can manage food.

The reason is specific to this project: **a demo that crashes in front of a panel is
worse than a demo that is 60% complete but works.** Every task ends in a runnable state.

---

## One addition to the file layout

`design.py` — colours and box-drawing.

Without it, the border and colour functions get copy-pasted into four files, and then
someone changes a colour in one place and forgets the others. One file, one answer:

> *"I made `design.py` so the colours and the boxes are written once. Otherwise I would
> have to repeat them in every file."*

That is a better viva answer than duplication would be.

---

## Tasks

Build order is dependency order. Each is one focused session.

### Task 1 — `data.py`: the dictionary and saving
- [x] **Task:** Write `DATA` with the four top-level keys and the four demo accounts, each restaurant carrying its own `fee`. Add `save_data()` and `load_data()`.
  - **Acceptance:** Running it once creates `data.json`; running again loads it without wiping. A fresh run with no file builds the demo accounts instead of crashing.
  - **Verify:** Delete `data.json`, run `python main.py` (it will fail on no `main.py` yet — call the functions from the Python prompt instead), check the file appears.
  - **Files:** `data.py`

### Task 2 — `design.py`: colours and boxes
- [x] **Task:** ANSI colour constants (amber `#E08830`, white, grey, red, green) and three helpers: `banner()`, `heading()`, `box()`. Draw the logo as block characters, using a `FONT` dictionary of 5 x 5 letter patterns that `make_logo()` assembles into rows.
  - **Acceptance:** A box prints with even left/right edges. The banner shows the word CRAVEFLOW and the tagline.
  - **Verify:** Run it, look at it. Check the box lines up.
  - **Files:** `design.py`

### Task 3 — `main.py`: login and routing
- [x] **Task:** The `login()` loop and the role router, wired to placeholder menu functions.
  - **Acceptance:** Wrong username and wrong password each give their own message then re-prompt. `exit` quits cleanly. Correct login shows the right role's menu and says "Signed in as ...".
  - **Verify:** Try a bad username, a bad password, then log in as each of the four roles in turn.
  - **Files:** `main.py`

### Task 4 — `restaurant.py`: the menu
- [x] **Task:** Add, show, change price, toggle availability, delete an item.
  - **Acceptance:** Only the logged-in restaurant's items are ever shown. Prices reject letters and negatives. Item IDs are generated, never typed. A deleted item leaves past orders untouched.
  - **Verify:** Add two items, sell out one, delete the other, close, reopen — both changes survived.
  - **Files:** `restaurant.py`

### Task 5 — `customer.py`: browsing
- [x] **Task:** List every restaurant with its available items and prices.
  - **Acceptance:** Sold-out items never appear. Prices show two decimals. An empty menu reads "No food available yet", not a crash.
  - **Verify:** Compare against what the restaurant added.
  - **Files:** `customer.py`

### Task 6 — `customer.py`: placing an order
- [x] **Task:** Select items and quantities, validate, create the order.
  - **Note:** Written by Claude during Task 5, because the four refusals sit inside the item-picking loop and could not be lifted out without restructuring code that was already verified. See the contribution note below for the plan to hand Yajat a real piece of it instead.
  - **Acceptance:** Refuses to mix two restaurants. Refuses unavailable items. Refuses if the customer already has an order in flight. Total = food subtotal + that restaurant's `fee`, rounded once and stored.
  - **Verify:** Try all four refusals, then a valid order, and check the stored total. **All four refusals verified 2026-10-11.**
  - **Files:** `customer.py`

### Task 7 — `restaurant.py`: accept, reject, cancel
- [x] **Task:** The restaurant's three order actions.
  - **Acceptance:** `PLACED` → `ACCEPTED` or `CANCELLED` only. A `DELIVERED` order is refused every action. Only the restaurant's own orders are visible.
  - **Verify:** All 12 status/action combinations checked 2026-10-11; a `DELIVERED` order is refused by all three, and each kitchen's order list is disjoint.
  - **Files:** `restaurant.py`

### Task 8 — `rider.py`: claim, pick up, deliver
- [x] **Task:** The rider's three actions plus the FREE/BUSY lock.
  - **Acceptance:** A `BUSY` rider is refused a second claim. An order cannot skip `PICKED_UP`. Delivering frees the rider. Cancelling frees the rider.
  - **Verify:** 11 checks run 2026-10-11. Double claim refused with the rider's existing order named; `PICKED_UP` cannot be skipped; a claimed order disappears from the waiting list; both riders hold independent locks.
  - **Files:** `rider.py`

### Task 9 — `reports.py`: the three reports
- [x] **Task:** Total sales, cancelled count and money lost, best-selling item.
  - **Note:** `best_seller()` was scaffolded empty for Yajat, then implemented at his direction — count the `quantities` dictionary, not the `items` list. Reasoning is in the docstring so it survives into the viva.
  - **Acceptance:** Sales counts only `DELIVERED`. Cancellations sit on their own line. Best-seller reads the `quantities` dictionary. All amounts show two decimals. Empty system shows zeroes.
  - **Verify:** 8 checks run 2026-10-11. Quantities proven against occurrences (3 order lines → 6 units); 25 units across four non-delivered orders correctly ignored; money attributed per item (1250, not 1530); `None` and deleted-item cases handled.
  - **Files:** `reports.py`

### Task 10 — Seed data and final polish
- [x] **Task:** A few demo food items so the first run isn't empty. Then re-read every file once.
  - **Acceptance:** A fresh run shows food to order. Every screen has no traceback. No file uses a construct from the forbidden list.
  - **Verify:** AST sweep 2026-10-11 — zero forbidden constructs across all 7 files. `json` and `os` appear only below the extension fence in `data.py` (line 177). Full four-role walkthrough driven through `main.py` as a subprocess: exit code 0, no traceback, every one of the 28 prompts answered.
  - **Bug found and fixed by the walkthrough:** `login()` asked for the password *before* checking for `exit`, so leaving the program demanded a password nobody should have to type. The check moved above the `input("Password: ")` line, which also matches the order the spec already described. Re-verified: `exit` quits with no password asked, and all three login paths still behave.
  - **Files:** `data.py`, `main.py`, all others read-only

---

## Verification checkpoints

There is no automated test suite, by decision. These are the checkpoints instead.

| After | Check |
|---|---|
| Task 3 | Login works for all four roles |
| Task 4 | Menu changes survive a restart |
| Task 6 | Every order refusal is enforced |
| Task 8 | The FREE/BUSY lock holds under a double claim |
| Task 9 | Reports match a hand-check of two known orders |
| Task 10 | Full four-role walkthrough, no crashes |

---

## Risks

| Risk | Mitigation |
|---|---|
| **Status flow is broken** — cancellation reachable from two states, by three roles | Task 7 and 8 both check status *before* acting. A `DELIVERED` order is refused everywhere. Task 6 is written by hand as the owner of that logic |
| **Money shows `260.49000000000001`** | `round(x, 2)` on every display, and the total is stored once, never recomputed |
| **A feature is quietly dropped under viva pressure** | The forbidden-construct list is in every spec's Boundaries. It is checked at Task 10, not hoped for |
| ~~**Demo is run on a machine where `data.json` is corrupt**~~ | **No longer possible — saving is switched off, so there is no file to be corrupt. Every run starts from the same demo data** |
| **Scope creep** — real payments, multiple addresses, ratings | Cut list is below. Not on the build order. If time runs short, cut from the bottom |

---

## Cut list, in order

If time runs short, remove from the bottom. Nothing above a cut line depends on it.

1. Delete an item from the menu (keep add and toggle)
2. Customer cancelling after `ACCEPTED` (keep cancelling while `PLACED`)
3. Rider cancelling (keep customer and restaurant cancelling)
4. Best-selling item report (keep sales and cancellations)

---

## What is deliberately not being built

No payments. No ratings or reviews. No delivery addresses or maps. No multiple
restaurants in one order. No login security. No password hashing. No database.

Each was considered and cut. If a panel asks "why didn't you add X", the answer is that
it was cut on purpose to keep the project explainable — which is a better answer than
having built it badly.