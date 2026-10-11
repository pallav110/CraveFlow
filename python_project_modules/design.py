
# ============================================================
# CraveFlow | Terminal User Interface
# Food Delivery Management System
# ============================================================

AMBER = "\033[38;5;215m"
WHITE = "\033[38;5;255m"
GREY = "\033[38;5;245m"
RED = "\033[38;5;203m"
GREEN = "\033[38;5;114m"
END = "\033[0m"

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
    """Clear the terminal."""
    print("\033[2J\033[H", end="")


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

    This is called once, at the start of the program. It does not clear
    the screen, so nothing the user has already read gets thrown away.
    """
    logo_width = max(len(row) for row in LOGO_ROWS)
    inside = max(WIDTH, logo_width)
    border = "+" + "-" * (inside + 2) + "+"

    print()
    print(AMBER + border + END)

    for row in LOGO_ROWS:
        print(
            AMBER + "| " + END
            + AMBER + pad_right(row, inside) + END
            + AMBER + " |" + END
        )

    print(
        AMBER + "| " + END
        + GREY + center_text(TAGLINE, inside) + END
        + AMBER + " |" + END
    )

    print(AMBER + border + END)
    print()


def rule():
    """Draw a thin divider between two screens.

    This is what separates one round of a menu from the next. It does
    not clear the screen, so the user can still scroll back and read
    anything that was printed above it.
    """
    print()
    print(GREY + "-" * WIDTH + END)


def heading(text):
    """Print a section heading."""
    text = " " + str(text) + " "
    available = max(0, WIDTH - len(text) - 2)

    print()
    print(
        AMBER + "--" + END
        + WHITE + text + END
        + AMBER + "-" * available + END
    )
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
    """Print two aligned columns.

    The whole row comes out exactly WIDTH characters wide, so it lines
    up with heading() and rule(), and still fits inside box().
    """
    left_width = max(0, min(left_width, WIDTH - gap))
    gap = max(0, min(gap, WIDTH - left_width))
    right_width = WIDTH - left_width - gap

    left_text = pad_right(cut(left, left_width), left_width)
    right_text = pad_left(cut(right, right_width), right_width)

    return left_text + " " * gap + right_text


def box(title, lines):
    """Draw a bordered panel."""
    # A content row is "| " + WIDTH characters + " |", so the row is
    # WIDTH + 4 wide. The top border has to be that same width, and it
    # is built out of: a +, a -, the title, then dashes for the rest.
    # Those first two characters leave WIDTH + 1 of dashes to share
    # between the title and the tail.
    title = " " + cut(title, WIDTH - 6) + " "
    remaining = WIDTH + 1 - len(title)

    top = "+" + "-" + title + "-" * max(0, remaining) + "+"
    bottom = "+" + "-" * (len(top) - 2) + "+"

    print()
    print(AMBER + top + END)

    for text in lines:
        content = pad_right(cut(text, WIDTH), WIDTH)
        print(
            AMBER + "| " + END
            + WHITE + content + END
            + AMBER + " |" + END
        )

    print(AMBER + bottom + END)


def options(items):
    """Display numbered menu choices."""
    print()

    for number, item in enumerate(items, start=1):
        print(
            "   " + AMBER + str(number) + "." + END
            + "  " + WHITE + str(item) + END
        )

    print("   " + GREY + "0. Go back" + END)
    print()


def money(amount):
    """Format a numeric amount as Indian rupees."""
    return "Rs. " + format(round(float(amount), 2), ".2f")
