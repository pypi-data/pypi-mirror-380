# easyascii.py

"""
Easy ASCII - A Comprehensive ASCII Art and Console UI Library

A single-file, zero-dependency Python library for creating beautiful and
functional text-based user interfaces and ASCII art.

Author: Your Name
Version: 1.0.0
License: MIT

Features:
- Advanced Boxes with multiple border styles, titles, and text alignment.
- Data Tables with automatic column sizing, headers, and text wrapping.
- FIGlet-style Banners for large text display.
- Progress Bars for tracking long-running tasks.
- Loading Spinners for indicating activity.
- Horizontal Rules for separating content.
- Ordered and Unordered Lists.
- Multi-column Text Layouts.
- Tree structure visualization.
- Full type hinting and extensive docstrings.
- No external dependencies.

Installation:
-------------
To make this library installable via pip, create the following two files
in your project folder:

1. `setup.py`:
   -------------------------------------------------------------------
   from setuptools import setup

   setup(
       name='easyascii',
       version='1.0.0',
       description='A comprehensive ASCII art and console UI library.',
       long_description=open('README.md').read(),
       long_description_content_type='text/markdown',
       author='Your Name',
       author_email='your.email@example.com',
       py_modules=['easyascii'],
       classifiers=[
           'Programming Language :: Python :: 3',
           'License :: OSI Approved :: MIT License',
           'Operating System :: OS Independent',
           'Topic :: Text Processing',
           'Topic :: Terminals',
       ],
       python_requires='>=3.6',
   )
   -------------------------------------------------------------------

2. `README.md`:
   A file containing a description of your library.

Then, you can install it locally by running:
   pip install .

Or upload it to PyPI to make it publicly available.
"""

# --- IMPORTS ---
import shutil
import sys
import time
import threading
import itertools
from typing import List, Dict, Any, Optional, Union, Tuple, Iterable

# --- METADATA ---
__version__ = "1.0.0"
__author__ = "Your Name"
__license__ = "MIT"

# --- CONSTANTS AND STYLES ---

BORDER_STYLES = {
    "light":      {"tl": "┌", "t": "─", "tr": "┐", "l": "│", "r": "│", "bl": "└", "b": "─", "br": "┘", "j_t": "┬", "j_b": "┴", "j_l": "├", "j_r": "┤", "j_c": "┼"},
    "heavy":      {"tl": "┏", "t": "━", "tr": "┓", "l": "┃", "r": "┃", "bl": "┗", "b": "━", "br": "┛", "j_t": "┳", "j_b": "┻", "j_l": "┣", "j_r": "┫", "j_c": "╋"},
    "double":     {"tl": "╔", "t": "═", "tr": "╗", "l": "║", "r": "║", "bl": "╚", "b": "═", "br": "╝", "j_t": "╦", "j_b": "╩", "j_l": "╠", "j_r": "╣", "j_c": "╬"},
    "rounded":    {"tl": "╭", "t": "─", "tr": "╮", "l": "│", "r": "│", "bl": "╰", "b": "─", "br": "╯", "j_t": "┬", "j_b": "┴", "j_l": "├", "j_r": "┤", "j_c": "┼"},
    "star":       {"tl": "*", "t": "*", "tr": "*", "l": "*", "r": "*", "bl": "*", "b": "*", "br": "*", "j_t": "*", "j_b": "*", "j_l": "*", "j_r": "*", "j_c": "*"},
    "hash":       {"tl": "#", "t": "#", "tr": "#", "l": "#", "r": "#", "bl": "#", "b": "#", "br": "#", "j_t": "#", "j_b": "#", "j_l": "#", "j_r": "#", "j_c": "#"},
    "plus":       {"tl": "+", "t": "-", "tr": "+", "l": "|", "r": "|", "bl": "+", "b": "-", "br": "+", "j_t": "+", "j_b": "+", "j_l": "+", "j_r": "+", "j_c": "+"},
    "dots":       {"tl": ".", "t": ".", "tr": ".", "l": ":", "r": ":", "bl": "'", "b": ".", "br": "'", "j_t": ".", "j_b": ".", "j_l": ":", "j_r": ":", "j_c": ":"},
}

# A simple block font for the banner feature
SIMPLE_FONT = {
    ' ': ['     ', '     ', '     ', '     ', '     '],
    'A': [' ### ', '#   #', '#####', '#   #', '#   #'], 'B': ['#### ', '#   #', '#### ', '#   #', '#### '],
    'C': [' ####', '#    ', '#    ', '#    ', ' ####'], 'D': ['#### ', '#   #', '#   #', '#   #', '#### '],
    'E': ['#####', '#    ', '###  ', '#    ', '#####'], 'F': ['#####', '#    ', '###  ', '#    ', '#    '],
    'G': [' ####', '#    ', '# ###', '#   #', ' ####'], 'H': ['#   #', '#   #', '#####', '#   #', '#   #'],
    'I': ['#####', '  #  ', '  #  ', '  #  ', '#####'], 'J': ['#####', '    #', '    #', '#   #', ' ### '],
    'K': ['#  # ', '# #  ', '##   ', '# #  ', '#  # '], 'L': ['#    ', '#    ', '#    ', '#    ', '#####'],
    'M': ['#   #', '## ##', '# # #', '#   #', '#   #'], 'N': ['#   #', '##  #', '# # #', '#  ##', '#   #'],
    'O': [' ### ', '#   #', '#   #', '#   #', ' ### '], 'P': ['#### ', '#   #', '#### ', '#    ', '#    '],
    'Q': [' ### ', '#   #', '# # #', '#  # ', ' ### #'], 'R': ['#### ', '#   #', '#### ', '# #  ', '#  # '],
    'S': [' ####', '#    ', ' ### ', '    #', '#### '], 'T': ['#####', '  #  ', '  #  ', '  #  ', '  #  '],
    'U': ['#   #', '#   #', '#   #', '#   #', ' ### '], 'V': ['#   #', '#   #', '#   #', ' # # ', '  #  '],
    'W': ['#   #', '#   #', '# # #', '## ##', '#   #'], 'X': ['#   #', ' # # ', '  #  ', ' # # ', '#   #'],
    'Y': ['#   #', ' # # ', '  #  ', '  #  ', '  #  '], 'Z': ['#####', '   # ', '  #  ', ' #   ', '#####'],
    '0': [' ### ', '# # #', '# # #', '# # #', ' ### '], '1': ['  #  ', ' ##  ', '  #  ', '  #  ', ' ### '],
    '2': [' ### ', '#   #', '  ## ', ' #   ', '#####'], '3': [' ### ', '#   #', '  ## ', '#   #', ' ### '],
    '4': ['#  # ', '#  # ', '#####', '   # ', '   # '], '5': ['#####', '#    ', '#### ', '    #', '#### '],
    '6': [' ####', '#    ', '#### ', '#   #', ' ####'], '7': ['#####', '   # ', '  #  ', ' #   ', '#    '],
    '8': [' ### ', '#   #', ' ### ', '#   #', ' ### '], '9': [' ####', '#   #', ' ####', '    #', '#### '],
    '!': ['  #  ', '  #  ', '  #  ', '     ', '  #  '], '?': [' ### ', '#   #', '  ## ', '     ', '  #  '],
    '.': ['     ', '     ', '     ', '     ', '  #  '], ',': ['     ', '     ', '     ', '  #  ', ' #   '],
    '-': ['     ', '     ', '#####', '     ', '     '], '+': ['     ', '  #  ', '#####', '  #  ', '     '],
    '=': ['     ', '#####', '     ', '#####', '     '], '/': ['    #', '   # ', '  #  ', ' #   ', '#    '],
    '\\':['#    ', ' #   ', '  #  ', '   # ', '    #'], '_': ['     ', '     ', '     ', '     ', '#####'],
}

SPINNER_STYLES = {
    "line": ['-', '\\', '|', '/'],
    "dots": ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
    "arrow": ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
    "box": ['▖', '▘', '▝', '▗'],
}


# --- INTERNAL HELPER FUNCTIONS ---

def _get_terminal_width(default: int = 80) -> int:
    """Gets the current terminal width, with a fallback."""
    try:
        return shutil.get_terminal_size((default, 20)).columns
    except OSError:
        return default

def _clean_text(text: Any) -> str:
    """Converts input to a string and removes problematic characters."""
    return str(text).replace('\t', '    ')

def _align_text(text: str, width: int, align: str) -> str:
    """Aligns a single line of text within a given width."""
    text_len = len(text)
    if text_len >= width:
        return text[:width]
    
    if align == 'left':
        return text.ljust(width)
    elif align == 'right':
        return text.rjust(width)
    elif align == 'center':
        padding = (width - text_len)
        left_pad = padding // 2
        right_pad = padding - left_pad
        return ' ' * left_pad + text + ' ' * right_pad
    else:
        raise ValueError(f"Unknown alignment: '{align}'. Use 'left', 'right', or 'center'.")

def _wrap_text(text: str, width: int) -> List[str]:
    """Wraps a string to a given width, preserving words."""
    if width <= 0:
        return [text]
        
    lines = []
    for line in text.split('\n'):
        words = line.split(' ')
        current_line = ""
        for word in words:
            if len(word) > width: # Handle very long words
                if current_line: lines.append(current_line.strip())
                lines.extend([word[i:i+width] for i in range(0, len(word), width)])
                current_line = ""
                continue

            if not current_line:
                current_line = word
            elif len(current_line) + 1 + len(word) <= width:
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
    return lines


# --- CORE PUBLIC FUNCTIONS ---

def box(
    text: Any,
    style: str = "light",
    width: Optional[int] = None,
    title: str = "",
    align: str = "left",
    padding: Union[int, Tuple[int, int]] = 1
) -> str:
    """
    Creates a string of text inside an ASCII box.

    Args:
        text (Any): The text content to display. Can be multi-line.
        style (str): The border style. Keys from BORDER_STYLES.
        width (Optional[int]): Total width of the box. If None, it's auto-calculated.
        title (str): An optional title to display on the top border.
        align (str): Text alignment ('left', 'center', 'right').
        padding (Union[int, Tuple[int, int]]): Horizontal and vertical padding.
            If int, used for both. If tuple, (horizontal, vertical).

    Returns:
        str: The formatted ASCII box as a single string.
    """
    if style not in BORDER_STYLES:
        raise ValueError(f"Unknown style: '{style}'. Available: {list(BORDER_STYLES.keys())}")
    
    s = BORDER_STYLES[style]
    clean_content = _clean_text(text)
    
    # Process padding
    if isinstance(padding, int):
        pad_h, pad_v = padding, padding
    else:
        pad_h, pad_v = padding

    # Calculate content width
    content_lines = clean_content.split('\n')
    max_line_len = max(len(line) for line in content_lines) if content_lines else 0
    
    if width:
        content_width = width - 2 - (pad_h * 2)
        if content_width <= 0:
            raise ValueError("Specified width is too small for borders and padding.")
    else:
        content_width = max_line_len
        width = content_width + 2 + (pad_h * 2)

    # Wrap text if necessary
    wrapped_lines = []
    for line in content_lines:
        wrapped_lines.extend(_wrap_text(line, content_width))

    # Build the box
    output = []
    
    # Top border with title
    if title:
        title_text = f" {title} "
        title_len = len(title_text)
        if title_len >= width - 2:
            title_text = _align_text(title, width - 2, "center")
            top_border = s['tl'] + title_text + s['tr']
        else:
            bar_len = width - 2 - title_len
            left_bar = bar_len // 2
            right_bar = bar_len - left_bar
            top_border = s['tl'] + s['t'] * left_bar + title_text + s['t'] * right_bar + s['tr']
    else:
        top_border = s['tl'] + s['t'] * (width - 2) + s['tr']
    output.append(top_border)
    
    # Vertical padding (top)
    empty_line = s['l'] + ' ' * (width - 2) + s['r']
    for _ in range(pad_v):
        output.append(empty_line)
    
    # Content
    for line in wrapped_lines:
        padded_line = ' ' * pad_h + _align_text(line, content_width, align) + ' ' * pad_h
        output.append(s['l'] + padded_line + s['r'])

    # Vertical padding (bottom)
    for _ in range(pad_v):
        output.append(empty_line)
        
    # Bottom border
    output.append(s['bl'] + s['b'] * (width - 2) + s['br'])
    
    return "\n".join(output)

def table(
    data: List[Dict[str, Any]],
    headers: Optional[List[str]] = None,
    style: str = "light",
    align: Union[str, Dict[str, str]] = "left",
    max_col_width: Optional[int] = None
) -> str:
    """
    Creates a formatted ASCII table from a list of dictionaries.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries, where each dict is a row.
        headers (Optional[List[str]]): A list of header keys. If None, uses keys from the first row.
        style (str): The border style. Keys from BORDER_STYLES.
        align (Union[str, Dict[str, str]]): Default alignment for all columns, or a
            dictionary mapping header keys to alignments ('left', 'center', 'right').
        max_col_width (Optional[int]): Maximum width for any single column.

    Returns:
        str: The formatted ASCII table as a single string.
    """
    if not data:
        return ""
    if style not in BORDER_STYLES:
        raise ValueError(f"Unknown style: '{style}'. Available: {list(BORDER_STYLES.keys())}")
    
    s = BORDER_STYLES[style]
    
    if headers is None:
        headers = list(data[0].keys())

    # --- 1. Prepare data and calculate column widths ---
    clean_data = [[_clean_text(row.get(h, "")) for h in headers] for row in data]
    clean_headers = [_clean_text(h) for h in headers]
    
    col_widths = {h: len(h) for h in clean_headers}
    for row in clean_data:
        for i, cell in enumerate(row):
            header = clean_headers[i]
            col_widths[header] = max(col_widths[header], len(cell))
            
    if max_col_width:
        for h in col_widths:
            col_widths[h] = min(col_widths[h], max_col_width)

    # --- 2. Wrap cell content and determine row heights ---
    wrapped_data = []
    for row in clean_data:
        wrapped_row = []
        max_lines_in_row = 1
        for i, cell in enumerate(row):
            header = clean_headers[i]
            wrapped_cell = _wrap_text(cell, col_widths[header])
            wrapped_row.append(wrapped_cell)
            max_lines_in_row = max(max_lines_in_row, len(wrapped_cell))
        wrapped_data.append((wrapped_row, max_lines_in_row))
    
    # --- 3. Build the table string ---
    def get_align(header: str) -> str:
        if isinstance(align, dict):
            return align.get(header, "left")
        return align

    def build_divider(left: str, middle: str, right: str, joint: str) -> str:
        parts = [left]
        for h in clean_headers:
            parts.append(middle * (col_widths[h] + 2)) # +2 for padding
        return joint.join(parts) + right

    output = []
    
    # Top border
    output.append(build_divider(s['tl'], s['t'], s['tr'], s['j_t']))
    
    # Header row
    header_parts = [s['l']]
    for h in clean_headers:
        header_parts.append(" " + _align_text(h, col_widths[h], get_align(h)) + " ")
    output.append(s['r'].join(header_parts) + s['r'])

    # Header divider
    output.append(build_divider(s['j_l'], s['t'], s['j_r'], s['j_c']))

    # Data rows
    for (wrapped_row, num_lines) in wrapped_data:
        for line_idx in range(num_lines):
            row_parts = [s['l']]
            for i, wrapped_cell in enumerate(wrapped_row):
                header = clean_headers[i]
                line_content = wrapped_cell[line_idx] if line_idx < len(wrapped_cell) else ""
                cell_str = " " + _align_text(line_content, col_widths[header], get_align(header)) + " "
                row_parts.append(cell_str)
            output.append(s['r'].join(row_parts) + s['r'])

    # Bottom border
    output.append(build_divider(s['bl'], s['b'], s['br'], s['j_b']))
    
    return "\n".join(output)

def banner(text: str, font: Dict = SIMPLE_FONT) -> str:
    """
    Renders large ASCII text (like FIGlet).
    """
    text = text.upper()
    output_lines = [''] * len(font.get('A', [''] * 5)) # Use height of a known character

    for char in text:
        # Use font.get() for safety in case a character is missing
        char_lines = font.get(char, font.get(' ', ['     '] * len(output_lines)))
        for i in range(len(output_lines)):
            output_lines[i] += char_lines[i] + " "

    return "\n".join(output_lines)

def hr(
    width: Optional[int] = None,
    char: str = "-",
    title: str = ""
) -> str:
    """
    Creates a horizontal rule (a line separator).

    Args:
        width (Optional[int]): The width of the rule. Defaults to terminal width.
        char (str): The character to use for the line.
        title (str): Optional title to embed in the middle of the rule.

    Returns:
        str: The horizontal rule string.
    """
    width = width or _get_terminal_width()
    char = char[0] if char else '-'

    if title:
        title_text = f" {title} "
        if len(title_text) >= width:
            return _align_text(title, width, 'center')
        
        bar_len = width - len(title_text)
        left_bar = bar_len // 2
        right_bar = bar_len - left_bar
        return char * left_bar + title_text + char * right_bar
    else:
        return char * width

def listing(
    items: Iterable[Any],
    ordered: bool = False,
    indent: int = 2,
    start: int = 1
) -> str:
    """
    Formats an iterable into an ordered or unordered list.

    Args:
        items (Iterable[Any]): The list of items to display.
        ordered (bool): If True, creates a numbered list. Otherwise, uses bullets.
        indent (int): Number of spaces to indent the list.
        start (int): The starting number for an ordered list.

    Returns:
        str: The formatted list string.
    """
    lines = []
    prefix = " " * indent
    
    for i, item in enumerate(items):
        if ordered:
            bullet = f"{i + start}."
        else:
            bullet = "*"
        
        lines.append(f"{prefix}{bullet} {_clean_text(item)}")
    
    return "\n".join(lines)

def columns(
    texts: List[str],
    num_cols: int = 2,
    width: Optional[int] = None,
    spacing: int = 4
) -> str:
    """
    Arranges a list of strings into multiple columns.

    Args:
        texts (List[str]): The strings to arrange.
        num_cols (int): The number of columns.
        width (Optional[int]): Total width for all columns. Defaults to terminal width.
        spacing (int): Number of spaces between columns.

    Returns:
        str: The formatted multi-column string.
    """
    width = width or _get_terminal_width()
    if num_cols <= 0:
        raise ValueError("Number of columns must be positive.")

    col_width = (width - (spacing * (num_cols - 1))) // num_cols
    if col_width <= 0:
        raise ValueError("Not enough width for the specified columns and spacing.")

    wrapped_cols = [_wrap_text(text, col_width) for text in texts]
    
    # Pad columns to have the same number of rows
    max_rows = max(len(col) for col in wrapped_cols) if wrapped_cols else 0
    padded_cols = [col + [''] * (max_rows - len(col)) for col in wrapped_cols]

    output_lines = []
    for i in range(max_rows):
        line_parts = []
        for j in range(num_cols):
            text_to_add = ""
            if j < len(padded_cols):
                text_to_add = padded_cols[j][i]
            line_parts.append(text_to_add.ljust(col_width))
        
        output_lines.append((' ' * spacing).join(line_parts))

    return "\n".join(output_lines)
    
def tree(
    data: Dict[str, Any],
    prefix: str = "",
    is_last: bool = True
) -> str:
    """
    Generates an ASCII tree structure from a nested dictionary.

    Args:
        data (Dict[str, Any]): The hierarchical data. Keys are node names.
            Values can be other dicts (sub-trees) or any other type (leaves).
        prefix (str): For internal recursive use.
        is_last (bool): For internal recursive use.

    Returns:
        str: The ASCII tree string.
    """
    output = []
    items = list(data.items())
    for i, (key, value) in enumerate(items):
        is_current_last = (i == len(items) - 1)
        connector = "└── " if is_current_last else "├── "
        output.append(prefix + connector + str(key))

        new_prefix = prefix + ("    " if is_current_last else "│   ")
        if isinstance(value, dict):
            output.append(tree(value, prefix=new_prefix, is_last=is_current_last))
        elif value is not None:
             # Leaf node
            leaf_connector = "    " if is_current_last else "│   "
            output.append(new_prefix + f"-> {value}")

    # The recursive calls return lists, we need to join them properly
    return "\n".join(line for line in "\n".join(output).split('\n') if line)


# --- DYNAMIC/UI HELPER FUNCTIONS ---

def progress_bar(
    iteration: int,
    total: int,
    prefix: str = 'Progress:',
    suffix: str = 'Complete',
    length: int = 50,
    fill: str = '█',
    print_end: str = "\r"
):
    """
    Prints a dynamic, single-line progress bar. Should be called in a loop.

    Args:
        iteration (int): Current iteration number (0-based).
        total (int): Total number of iterations.
        prefix (str): Text to display before the bar.
        suffix (str): Text to display after the bar.
        length (int): Character length of the bar.
        fill (str): Bar fill character.
        print_end (str): The end character for the print function (use "\r" for single-line update).
    """
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')
        sys.stdout.flush()

class Spinner:
    """
    A context manager for displaying a loading spinner in the console.

    Example:
        with Spinner("Loading data..."):
            time.sleep(3)
    """
    def __init__(self, text: str = "Loading...", style: str = "dots", delay: float = 0.1):
        if style not in SPINNER_STYLES:
            raise ValueError(f"Unknown style: '{style}'. Available: {list(SPINNER_STYLES.keys())}")
        
        self.text = text
        self.delay = delay
        self.spinner = itertools.cycle(SPINNER_STYLES[style])
        self.busy = False
        self.spinner_visible = False
        self.thread = None

    def _spinner_task(self):
        while self.busy:
            char = next(self.spinner)
            sys.stdout.write(f"\r{self.text} {char}")
            sys.stdout.flush()
            self.spinner_visible = True
            time.sleep(self.delay)

    def __enter__(self):
        self.busy = True
        self.thread = threading.Thread(target=self._spinner_task)
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.busy = False
        if self.thread:
            self.thread.join()
        if self.spinner_visible:
            # Clear the line
            sys.stdout.write('\r' + ' ' * (len(self.text) + 2) + '\r')
            sys.stdout.flush()


# --- CONVENIENCE PRINT WRAPPERS ---

def print_box(*args, **kwargs):
    """Prints the result of box()."""
    print(box(*args, **kwargs))

def print_table(*args, **kwargs):
    """Prints the result of table()."""
    print(table(*args, **kwargs))

def print_banner(*args, **kwargs):
    """Prints the result of banner()."""
    print(banner(*args, **kwargs))

def print_hr(*args, **kwargs):
    """Prints the result of hr()."""
    print(hr(*args, **kwargs))

def print_listing(*args, **kwargs):
    """Prints the result of listing()."""
    print(listing(*args, **kwargs))

def print_columns(*args, **kwargs):
    """Prints the result of columns()."""
    print(columns(*args, **kwargs))

def print_tree(*args, **kwargs):
    """Prints the result of tree()."""
    print(tree(*args, **kwargs))


# --- DEMONSTRATION / SHOWCASE ---

def showcase():
    """Demonstrates all features of the Easy ASCII library."""
    
    print_banner("EASY ASCII")
    print_hr(title="v" + __version__)

    # --- Box Showcase ---
    print_hr(title="Boxes")
    print_box(
        "This is a 'light' box with left alignment (default).\nIt supports multi-line content and auto-wraps text if the box is given a fixed width.",
        style="light",
        title="Light Style"
    )
    print_box(
        "This is a 'heavy' box with center alignment and custom padding.",
        style="heavy",
        title="Heavy Style",
        align="center",
        padding=(4, 1) # 4 horizontal, 1 vertical
    )
    print_box(
        "A rounded box with right alignment.",
        style="rounded",
        title="Right Aligned",
        align="right",
        width=60
    )
    print_box("Double style", style="double", align="center")
    print_box("Star style", style="star", align="center", width=40)

    # --- Table Showcase ---
    print_hr(title="Tables")
    sample_data = [
        {"ID": 1, "Name": "Python", "Type": "Programming Language", "Description": "A versatile and widely-used language known for its readability and extensive libraries."},
        {"ID": 2, "Name": "JavaScript", "Type": "Scripting Language", "Description": "The language of the web, enabling interactive and dynamic content in browsers."},
        {"ID": 3, "Name": "SQL", "Type": "Query Language", "Description": "Standard language for managing and manipulating databases."},
    ]
    print_table(
        sample_data, 
        style="double",
        align={"ID": "center", "Name": "left", "Type": "left", "Description": "left"},
        max_col_width=40
    )

    # --- Lists and Columns Showcase ---
    print_hr(title="Lists & Columns")
    features = ["Boxes", "Tables", "Banners", "Progress Bars", "Spinners", "And more!"]
    print_listing(features, ordered=True, indent=4)

    long_texts = [
        "Column 1: This is the first column. It contains some text that will be arranged neatly.",
        "Column 2: Here is the second column. Easy-ASCII automatically calculates the required width and wraps the text.",
        "Column 3: And finally, a third column to demonstrate the layout capabilities.",
    ]
    print_columns(long_texts, num_cols=3)

    # --- Tree Showcase ---
    print_hr(title="Tree Structure")
    file_system = {
        "project": {
            "src": {
                "main.py": "Entry point",
                "utils.py": "Helper functions"
            },
            "docs": {
                "index.md": None
            },
            "README.md": "Project description"
        }
    }
    print_tree(file_system)

    # --- Dynamic Elements Showcase ---
    print_hr(title="Dynamic Elements")
    
    # Progress Bar
    items = range(100)
    total = len(items)
    for i, item in enumerate(items):
        progress_bar(i + 1, total, prefix='Downloading:', suffix='Complete', length=50)
        time.sleep(0.02)
        
    # Spinner
    print("Running a simulated task with a spinner...")
    with Spinner("Processing files...", style="dots"):
        time.sleep(3)
    print("Task complete!")

    with Spinner("Another task...", style="arrow"):
        time.sleep(3)
    print("Done again.")
    

if __name__ == "__main__":
    showcase()