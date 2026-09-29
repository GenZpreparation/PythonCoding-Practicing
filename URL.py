import urllib.request
import re
from html.parser import HTMLParser


def _fetch_html(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8", errors="replace")


class _TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.current_row = None
        self.current_cell = None
        self.inside_cell = False

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.current_row = []
        elif tag in ("td", "th"):
            self.inside_cell = True
            self.current_cell = []

    def handle_endtag(self, tag):
        if tag == "tr":
            if self.current_row is not None:
                self.rows.append(self.current_row)
            self.current_row = None

        elif tag in ("td", "th"):
            if self.inside_cell and self.current_row is not None:
                self.current_row.append("".join(self.current_cell).strip())

            self.inside_cell = False
            self.current_cell = None

    def handle_data(self, data):
        if self.inside_cell:
            self.current_cell.append(data)


def _parse_grid_data(html):
    parser = _TableParser()
    parser.feed(html)

    entries = []

    for row in parser.rows:
        if len(row) < 3:
            continue

        x_value = row[0].strip()
        character = row[1].strip()
        y_value = row[2].strip()

        # Skip the header row and any invalid rows.
        if not re.fullmatch(r"-?\d+", x_value):
            continue

        if not re.fullmatch(r"-?\d+", y_value):
            continue

        if not character:
            continue

        entries.append(
            (int(x_value), character[0], int(y_value))
        )

    return entries


def print_secret_message(doc_url):
    """
    Fetch the published Google Doc and print the characters
    according to their x and y coordinates.
    """

    html = _fetch_html(doc_url)
    entries = _parse_grid_data(html)

    if not entries:
        print("No grid data found.")
        return

    max_x = max(x for x, _, _ in entries)
    max_y = max(y for _, _, y in entries)

    # Create an empty grid first.
    grid = [
        [" "] * (max_x + 1)
        for _ in range(max_y + 1)
    ]

    # Place every character at its given coordinate.
    for x, character, y in entries:
        grid[y][x] = character

    # Print the grid from top to bottom.
    for row in grid:
        print("".join(row))