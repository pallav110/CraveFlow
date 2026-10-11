
# ============================================================
# CraveFlow | Terminal User Interface
# Food Delivery Management System
# ============================================================

# IDLE COMPATIBLE - colours switched off because IDLE Shell
# cannot show ANSI colours, it prints them as [38;5;215m junk.
# Same file, just blank colours so output is clean in IDLE
# and still clean in normal terminal.
AMBER = ""
WHITE = ""
GREY = ""
RED = ""
GREEN = ""
END = ""

WIDTH = 76

# The logo is drawn with a 5 x 5 letter pattern, which keeps it compact.
# Each letter is just five ordinary strings, five characters wide.
#
# Every letter is built out of one character, the block character.
# The block character is the solid square that looks like this: (█)
# It is not a normal letter, which is exactly why it makes a logo look
# like a logo and not like a sentence.
#
# A # would also draw a letter, but a row of hashes reads as a
# separator, not as a word. The block character reads as a solid shape.
FONT = {
    "C": [" ███ ", "█   █", "█    ", "█   █", " ███ "],
    "R": ["████ ", "█   █", "████ ", "█  █ ", "█   █"],
    "A": [" ███ ", "█   █", "█████", "█   █", "█   █"],
    "V": ["█   █", "█   █", "█   █", " █ █ ", "  █  "],
    "E": ["█████", "█    ", "████ ", "█    ", "█████"],
    "F": ["█████", "█    ", "████ ", "█    ", "█    "],
    "L": ["█    ", "█    ", "█    ", "█    ", "█████"],
    "O": [" ███ ", "█   █", "█   █", "█   █", " ███ "],
    "W": ["█   █", "█   █", "█ █ █", "██ ██", "█   █"],
}


def make_logo(word="CRAVEFLOW"):
    """Build the wordmark using the letter patterns."""
    rows = []

    for row_number in range(5):
        row = " ".join(FONT[letter][row_number] for letter in word)
        rows.append(row)

    return rows


LOGO_ROWS = make_logo()
TAGLINE = "From craving to delivery, seamlessly."


def clear_screen():
    """Clear the terminal - does nothing in IDLE so Shell stays clean."""
    # Original was print("\033[2J\033[H", end="") which IDLE shows as junk.
    # In IDLE Shell we just print blank lines, in real terminal same effect.
    print("\n" * 2)


def center_text(text, width):
    """Center text inside a fixed width."""
    text = str(text)[:width]
    return text.center(width)


def pad_right(text, width):
    """Align text to the left."""
    return str(text)[:width].ljust(width)


def pad_left(text, width):
    """Align text to the right."""
    return str(text)[:width].rjust(width)


def cut(text, length):
    """Shorten text without exceeding the available space."""
    text = str(text)

    if len(text) <= length:
        return text

    if length <= 3:
        return text[:length]

    return text[:length - 3] + "..."


def banner():
    """Display the CraveFlow logo and tagline.

    IDLE version - plain left-aligned text because IDLE Shell
    uses a proportional font, so any centered box with | borders
    looks crooked even when the code is 100% correct.
    Same function name, so main.py needs zero changes.
    """
    print()
    print("C R A V E F L O W")
    print(TAGLINE)
    print("-" * 40)
    print()


def rule():
    """Draw a thin divider between two screens - IDLE plain version."""
    print()
    print("-" * 40)


def heading(text):
    """Print a section heading - IDLE plain version."""
    print()
    print(str(text))
    print("-" * 40)
    print()


def line(text=""):
    """Print secondary information."""
    print(GREY + str(text) + END)


def ok(text):
    """Print a successful operation."""
    print(GREEN + "[OK] " + str(text) + END)


def warn(text):
    """Print an error or warning."""
    print(RED + "[!] " + str(text) + END)


def columns(left, right, left_width, gap=2):
    """Print two aligned columns - IDLE plain version, simple gap."""
    return str(left) + "  " + str(right)


def box(title, lines):
    """Draw a bordered panel - IDLE plain version, no padding tricks."""
    print()
    print(str(title))
    print("-" * 40)

    for text in lines:
        print("  " + str(text))

    print("-" * 40)


def options(items):
    """Display numbered menu choices - IDLE plain version."""
    print()

    for number, item in enumerate(items, start=1):
        print("   " + str(number) + ".  " + str(item))

    print("   0. Go back")
    print()


def money(amount):
    """Format a numeric amount as Indian rupees."""
    return "Rs. " + format(round(float(amount), 2), ".2f")
