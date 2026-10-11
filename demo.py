#!/usr/bin/env python3
"""
Demo script for CraveFlow — runs the full 4-role flow in one terminal.

Usage:
    python demo.py

What it does:
    1. Customer (yajat) places an order
    2. Restaurant (tandoor) accepts it
    3. Rider (raj) claims → picks up → delivers (auto-shows receipt)
    4. Customer (yajat) sees the delivered order

All output is streamed in real-time so you can watch the flow.
"""

import subprocess
import sys
import os
import time


# Force UTF-8 for subprocess
os.environ["PYTHONIOENCODING"] = "utf-8"


# ──────────────────────────────────────────────────────────────
# Keystroke sequences for each role
# ──────────────────────────────────────────────────────────────

# Each entry: (username, password, [list of inputs with delays])
# Delay of 0 means "send immediately after previous output"
# Delay > 0 means "wait N seconds before sending"

FLOW = [
    # ── CUSTOMER: place order ─────────────────────────────────
    {
        "role": "customer",
        "username": "yajat",
        "password": "1234",
        "inputs": [
            ("2", 0.3),   # Place a new order
            ("1", 0.3),   # North Indian
            ("1", 0.3),   # Tandoor House
            ("F201 1", 0.3),  # 1x Butter Chicken
            ("0", 0.5),   # Done adding items
            ("0", 0.3),   # Sign out
        ],
    },

    # ── RESTAURANT: accept order ──────────────────────────────
    {
        "role": "restaurant",
        "username": "tandoor",
        "password": "1234",
        "inputs": [
            ("7", 0.3),   # Accept an order
            ("O1001", 0.3),  # The order ID (will be O1001 since we start fresh)
            ("0", 0.3),   # Sign out
        ],
    },

    # ── RIDER: claim → pick up → deliver ──────────────────────
    {
        "role": "rider",
        "username": "raj",
        "password": "1234",
        "inputs": [
            ("2", 0.3),   # Claim an order
            ("O1001", 0.3),  # Claim the order
            ("3", 0.3),   # Mark picked up
            ("4", 0.5),   # Mark delivered (auto-shows receipt)
            ("0", 0.3),   # Sign out
        ],
    },

    # ── CUSTOMER AGAIN: verify delivered order ────────────────
    {
        "role": "customer (verify)",
        "username": "yajat",
        "password": "1234",
        "inputs": [
            ("3", 0.3),   # My orders
            ("0", 0.3),   # Sign out
            ("exit", 0),  # Exit program
        ],
    },
]


# ──────────────────────────────────────────────────────────────
# Helper: run the program and feed inputs
# ──────────────────────────────────────────────────────────────

def run_flow():
    """Launch main.py and drive it through the full flow."""

    # Build the full input script
    all_inputs = []

    for step in FLOW:
        # Login
        all_inputs.append((step["username"], 0.2))
        all_inputs.append((step["password"], 0.3))

        # Role actions
        for inp, delay in step["inputs"]:
            all_inputs.append((inp, delay))

    # Convert to string with newlines
    input_script = "\n".join(inp for inp, _ in all_inputs) + "\n"

    print("=" * 60)
    print("CRAVEFLOW DEMO — Full 4-Role Flow")
    print("=" * 60)
    print()
    print("Input script that will be sent:")
    print("-" * 40)
    for i, (inp, delay) in enumerate(all_inputs, 1):
        label = "<-" if inp in ("yajat", "tandoor", "raj", "owner", "1234", "exit") else ""
        print(f"  {i:2d}. {inp:<12} (wait {delay}s) {label}")
    print("-" * 40)
    print()
    print("Starting in 2 seconds... (Ctrl+C to cancel)")
    print()
    time.sleep(2)

    # Launch the program with UTF-8 encoding for block characters
    proc = subprocess.Popen(
        [sys.executable, "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,  # line buffered
        cwd="C:\\Users\\pallav\\Desktop\\Python\\CraveFlow",
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )

    # Feed inputs with delays, while streaming output
    try:
        for inp, delay in all_inputs:
            # Write input
            proc.stdin.write(inp + "\n")
            proc.stdin.flush()

            # Small delay for the program to process
            time.sleep(delay)

        # Wait for process to finish and stream remaining output
        proc.stdin.close()
        for line in proc.stdout:
            # Replace block characters (█) with ASCII equivalent for cp1252 terminals
            line = line.replace("█", "#")
            print(line, end="")

        proc.wait()

    except KeyboardInterrupt:
        print("\n\n[Demo interrupted by user]")
        proc.terminate()
        proc.wait()
        return 1

    print()
    print("=" * 60)
    print("Demo complete.")
    print("=" * 60)
    return proc.returncode


if __name__ == "__main__":
    sys.exit(run_flow())