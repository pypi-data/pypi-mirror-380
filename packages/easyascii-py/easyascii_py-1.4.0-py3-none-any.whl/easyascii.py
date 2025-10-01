"""
Easy ASCII - A Comprehensive ASCII Art and Console UI Library

A single-file, zero-dependency Python library for creating beautiful and
functional text-based user interfaces and ASCII art.

Author: Matttz
Version: 1.4.0
License: MIT
"""

# --- IMPORTS ---
import shutil
import sys
import time
import threading
import itertools
from typing import List, Dict, Any, Optional, Union, Tuple, Iterable
import random
import os
from datetime import datetime
import math
import calendar as cal_module

# --- METADATA ---
__version__ = "1.4.0"
__author__ = "Matttz"
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
    "dots": ['.', '..', '...', '....'],
    "arrow": ['->', '-->', '--->', '---->'],
    "moon": ['(    )', '( .  )', '( .. )', '( ... )', '( .... )', '(  ...)', '(  .. )', '(  . )'],
    "bounce": ['[    ]', '[=   ]', '[==  ]', '[=== ]', '[====]', '[ ===]', '[  ==]', '[   =]'],
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

def alert(
    text: Any,
    title: Optional[str] = None,
    alert_type: str = "info",
    **kwargs
) -> str:
    """
    Creates a pre-styled alert box for different message types.
    This is a specialized wrapper around the box() function.

    Args:
        text (Any): The alert message content.
        title (Optional[str]): The title of the alert. Defaults to the alert type.
        alert_type (str): Type of alert ('info', 'success', 'warning', 'error').
        **kwargs: Other arguments to pass directly to the box() function
                  (e.g., width, padding, align).

    Returns:
        str: The formatted alert box string.
    """
    alert_styles = {
        "info":    {"prefix": "[i]", "style": "light", "default_title": "INFO"},
        "success": {"prefix": "[V]", "style": "rounded", "default_title": "SUCCESS"},
        "warning": {"prefix": "[!]", "style": "heavy", "default_title": "WARNING"},
        "error":   {"prefix": "[x]", "style": "double", "default_title": "ERROR"},
    }
    
    config = alert_styles.get(alert_type.lower())
    if not config:
        raise ValueError(f"Unknown alert_type: '{alert_type}'. Use one of {list(alert_styles.keys())}")

    # Use provided title, or the default for the type, or None
    final_title = title if title is not None else config["default_title"]
    
    # Prepend the prefix to the text
    content = f"{config['prefix']} {_clean_text(text)}"
    
    # Set default style but allow override via kwargs
    if 'style' not in kwargs:
        kwargs['style'] = config['style']
        
    return box(content, title=final_title, **kwargs)

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
        # I used font.get() for safety in case a character is missing
        char_lines = font.get(char, font.get(' ', ['     '] * len(output_lines)))
        for i in range(len(output_lines)):
            output_lines[i] += char_lines[i] + " "

    return "\n".join(output_lines)
    
def gauge(
    value: float,
    total: float = 100.0,
    label: str = "",
    length: int = 30,
    fill: str = '█',
    background: str = '░'
) -> str:
    """
    Creates a static gauge or meter bar.

    Args:
        value (float): The current value to display.
        total (float): The total or maximum value.
        label (str): A label to display next to the gauge.
        length (int): The character length of the bar itself.
        fill (str): The character for the filled part of the gauge.
        background (str): The character for the empty part of the gauge.

    Returns:
        str: The formatted gauge string.
    """
    if total <= 0:
        raise ValueError("Total must be positive.")
    
    # Clamp value to be within [0, total]
    value = max(0, min(value, total))
    
    percent = value / total
    filled_length = int(length * percent)
    
    bar = fill * filled_length + background * (length - filled_length)
    percent_str = f" {percent:.1%}" # e.g., " 75.0%"
    
    if label:
        return f"{label}: |{bar}|{percent_str}"
    else:
        return f"|{bar}|{percent_str}"
        
        
from typing import List, Union, Optional

from typing import List, Union

def sparkline(data: List[Union[int, float]], height: int = 5, block: str = '#') -> str:
    """
    Generates a truly blocky multi-line ASCII sparkline.
    """
    if not data:
        return ""

    min_v, max_v = min(data), max(data)
    # Handle the case where all data points are the same
    if min_v == max_v:
        # Create a flat line at mid-height
        rows = [' ' * len(data) for _ in range(height)]
        mid_row = height // 2
        rows[mid_row] = block * len(data)
        return '\n'.join(rows)

    value_range = max_v - min_v
    rows = ['' for _ in range(height)]
    
    for n in data:
        # Determine how many rows this value fills, ensuring at least one block for the min value
        level = 1 + int(((n - min_v) / value_range) * (height - 1))
        for i in range(height):
            # Fill from the bottom up
            rows[height - 1 - i] += block if i < level else ' '

    return '\n'.join(rows)

    
    value_range = max_v - min_v
    if value_range == 0:
        return ticks[0] * len(data)  # Return flat line if all values are the same

    line = ""
    for n in data:
        # Normalize to 0-1, then scale to number of ticks
        level = (n - min_v) / value_range
        tick_index = int(round(level * (len(ticks) - 1)))
        line += ticks[tick_index]
        
    return line

       
def bar_chart(
    data: Dict[str, Union[int, float]],
    max_bar_length: int = 40,
    fill: str = '█',
    title: str = ""
) -> str:
    """
    Creates a simple horizontal ASCII bar chart from a dictionary.

    Args:
        data (Dict[str, Union[int, float]]): Dictionary of labels to values.
        max_bar_length (int): The maximum length of the longest bar.
        fill (str): The character to use for the bars.
        title (str): An optional title for the chart.

    Returns:
        str: The formatted bar chart string.
    """
    if not data:
        return ""

    # Find the longest label for alignment
    max_label_len = max(len(label) for label in data.keys())
    
    # Find the maximum value for scaling
    max_value = max(data.values())
    if max_value == 0:
        scale = 0
    else:
        scale = max_bar_length / max_value

    output = []
    if title:
        output.append(title)
        output.append("-" * len(title))

    for label, value in data.items():
        bar_len = int(value * scale)
        bar = fill * bar_len
        # Right-align the label and add the bar and value
        line = f"{label.rjust(max_label_len)} | {bar} {value}"
        output.append(line)

    return "\n".join(output)
    
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

def checklist(
    items: Iterable[Tuple[str, bool]],
    indent: int = 2
) -> str:
    """
    Formats an iterable of (label, status) tuples into a checklist.

    Args:
        items (Iterable[Tuple[str, bool]]): An iterable of tuples where each
            tuple contains the item text (str) and its status (bool: True for checked).
        indent (int): Number of spaces to indent the list.

    Returns:
        str: The formatted checklist string.
    """
    lines = []
    prefix = " " * indent
    
    for item_text, is_checked in items:
        bullet = "[x]" if is_checked else "[ ]"
        lines.append(f"{prefix}{bullet} {_clean_text(item_text)}")
        
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

# --- ASCII ART & SHAPES ---

def bubble(
    text: Any,
    style: str = "rounded"
) -> str:
    """
    Puts a message inside an ASCII speech bubble.

    Args:
        text (Any): The message to display inside the bubble.
        style (str): The border style for the bubble body ('light', 'rounded', etc.).

    Returns:
        str: The ASCII speech bubble as a string.
    """
    clean_content = _clean_text(text)
    box_content = box(clean_content, style=style, padding=(1, 0))
    
    lines = box_content.split('\n')
    width = len(lines[0])
    
    # Add the bubble tail
    lines.append(' ' * (width // 4) + ('\\' if style != 'rounded' else '╰') + '  ' + ('╯' if style != 'rounded' else '/'))
    lines.append(' ' * (width // 4) + ' \\/')
    
    return "\n".join(lines)

def cat() -> str:
    """Returns a simple static ASCII cat."""
    return "\n".join([
        r' /\_/\ ',
        r'( o.o )',
        r' >   < '
    ])
    

# --- GENERATORS ---

def maze(width: int = 21, height: int = 11) -> str:
    """
    Generates a simple ASCII maze using a randomized depth-first search.

    Args:
        width (int): The width of the maze. Should be an odd number.
        height (int): The height of the maze. Should be an odd number.

    Returns:
        str: The generated maze as a string.
    """
    # Ensure dimensions are odd
    w = (width // 2) * 2 + 1
    h = (height // 2) * 2 + 1

    # Initialize grid with walls
    grid = [['█'] * w for _ in range(h)]
    
    def carve_passages(cx, cy):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 < nx < w and 0 < ny < h and grid[ny][nx] == '█':
                grid[ny-dy//2][nx-dx//2] = ' ' # Carve path
                grid[ny][nx] = ' ' # Move to new cell
                carve_passages(nx, ny)

    # Start carving from a random odd-coordinate point
    start_x = random.randrange(1, w, 2)
    start_y = random.randrange(1, h, 2)
    grid[start_y][start_x] = ' '
    carve_passages(start_x, start_y)
    
    # Add entry and exit points
    grid[1][0] = ' '
    grid[h-2][-1] = ' '
    
    return "\n".join("".join(row) for row in grid)


# --- TEXT EFFECTS ---

def mirror(text: str) -> str:
    """
    Creates a side-by-side mirror effect for the given text.

    Args:
        text (str): The input text (can be multi-line).

    Returns:
        str: The text next to its horizontal reflection.
    """
    lines = text.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    
    output = []
    for line in lines:
        padded_line = line.ljust(max_len)
        reversed_line = padded_line[::-1]
        output.append(f"{padded_line} | {reversed_line}")
        
    return "\n".join(output)

def repeat(text: str, n: int, direction: str = "row") -> str:
    """
    Repeats a string multiple times in a row or column.

    Args:
        text (str): The text to repeat.
        n (int): The number of times to repeat.
        direction (str): The direction of repetition ('row' or 'col').

    Returns:
        str: The repeated text string.
    """
    if direction.lower() == 'row':
        return text * n
    elif direction.lower() == 'col':
        return "\n".join([text] * n)
    else:
        raise ValueError("Direction must be 'row' or 'col'.")

def staircase(text: str) -> str:
    """
    Arranges text in a staircase pattern.

    Args:
        text (str): The text to format.

    Returns:
        str: The text arranged as a staircase.
    """
    return "\n".join(text[:i+1] for i in range(len(text)))

def wave(text: str, amplitude: int = 4) -> str:
    """
    Creates a wavy text effect by shifting lines with spaces.

    Args:
        text (str): The text to make wavy (can be multi-line).
        amplitude (int): How far the text should shift left and right.

    Returns:
        str: The wavy text string.
    """
    lines = text.split('\n')
    output = []
    for i, line in enumerate(lines):
        # Use a sine wave for smooth oscillation
        shift = int(amplitude * math.sin(i * math.pi / (amplitude * 2)))
        output.append(" " * shift + line)
    return "\n".join(output)
    
    # --- DATE & TIME UTILITIES ---

def timestamp(message: str, format_str: str = "[%Y-%m-%d %H:%M:%S]") -> str:
    """
    Prepends a formatted timestamp to a message.

    Args:
        message (str): The message to timestamp.
        format_str (str): The format for the timestamp (strftime format).

    Returns:
        str: The timestamped message string.
    """
    now_str = datetime.now().strftime(format_str)
    return f"{now_str} {message}"

def day_banner() -> str:
    """
    Creates a large ASCII banner of the current day of the week.
    This is a wrapper around the banner() function.

    Returns:
        str: A large ASCII art banner of the day's name.
    """
    day_name = datetime.now().strftime("%A").upper()
    return banner(day_name)

def calendar(year: Optional[int] = None, month: Optional[int] = None) -> str:
    """
    Generates a simple ASCII calendar for a given month and year,
     defaulting to the current month.

    Args:
        year (Optional[int]): The year for the calendar. Defaults to current year.
        month (Optional[int]): The month for the calendar (1-12). Defaults to current month.

    Returns:
        str: The formatted calendar string inside a box.
    """
    now = datetime.now()
    cal_year = year if year is not None else now.year
    cal_month = month if month is not None else now.month

    # Use the aliased module name to avoid name collision
    cal_text = cal_module.month(cal_year, cal_month, w=2, l=1)
    
    # Get month name for the title
    month_name = datetime(cal_year, cal_month, 1).strftime('%B')
    title = f"{month_name} {cal_year}"
    
    # Use the box function for a consistent look
    # Using 'plus' style for a classic calendar grid look
    return box(cal_text, title=title, style="plus", align="left", padding=1)
    
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

# easyascii.py, around line 527

class Spinner:
    """
    A context manager for displaying a loading spinner in the console.
    The spinner's text can be updated dynamically while it is running.

    Example:
        with Spinner("Loading data...") as s:
            time.sleep(2)
            s.update_text("Processing files...")
            time.sleep(2)
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
        self._last_line_len = 0

    def _spinner_task(self):
        while self.busy:
            char = next(self.spinner)
            current_line = f"\r{self.text} {char}"
            padding = ' ' * (self._last_line_len - len(current_line))
            
            sys.stdout.write(current_line + padding)
            sys.stdout.flush()
            
            self._last_line_len = len(current_line)
            self.spinner_visible = True
            time.sleep(self.delay)

    def update_text(self, new_text: str):
        """Updates the text displayed next to the spinner."""
        self.text = new_text

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
            sys.stdout.write('\r' + ' ' * self._last_line_len + '\r')
            sys.stdout.flush()

def typewriter(text: str, delay: float = 0.05):
    """
    Prints text to the console with a typewriter effect.

    Args:
        text (str): The text to print.
        delay (float): The delay in seconds between each character.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def timer(seconds: int):
    """
    Displays a countdown timer for a given number of seconds.

    Args:
        seconds (int): The number of seconds to count down from.
    """
    try:
        for i in range(seconds, -1, -1):
            minutes, secs = divmod(i, 60)
            time_str = f"{minutes:02d}:{secs:02d}"
            sys.stdout.write(f"\r Countdown: {time_str} ")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\n Times up!\n")
    except KeyboardInterrupt:
        sys.stdout.write("\nTimer cancelled.\n")
    finally:
        sys.stdout.flush()
        
def clock():
    """
    Displays a live-updating ASCII clock until interrupted (Ctrl+C).
    """
    print("Press Ctrl+C to stop the clock.")
    try:
        while True:
            now = datetime.now()
            time_str = now.strftime("%H:%M:%S")
            # A simple digital-style ASCII clock
            clock_art = banner(time_str)
            
            # Move cursor up to overwrite previous clock drawing
            num_lines = len(clock_art.split('\n'))
            if 'last_lines' in locals() and last_lines > 0:
                 sys.stdout.write(f'\r\033[{last_lines}A')
            
            sys.stdout.write(clock_art + '\n')
            sys.stdout.flush()
            last_lines = num_lines
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")
        sys.stdout.flush()

def scroll(text: str, width: Optional[int] = None, delay: float = 0.1):
    """
    Displays a horizontally scrolling text animation until interrupted.

    Args:
        text (str): The text to scroll.
        width (Optional[int]): The width of the scrolling window. Defaults to terminal width.
        delay (float): The delay between animation frames.
    """
    width = width or _get_terminal_width() // 2 # A sensible default
    
    # Pad the text to create a seamless loop
    padded_text = text + ' ' * width
    
    print("Press Ctrl+C to stop scrolling.")
    try:
        i = 0
        while True:
            # Create the current view
            current_view = (padded_text * 2)[i : i + width]
            sys.stdout.write(f"\r[{current_view}]")
            sys.stdout.flush()
            
            i = (i + 1) % len(padded_text)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nScrolling stopped.")
        sys.stdout.flush()
        
def fireworks(duration: int = 10):
    """
    Displays a simple ASCII fireworks animation for a given duration.
    Note: Uses os.system('clear'/'cls') to clear the screen.

    Args:
        duration (int): The duration of the animation in seconds.
    """
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    frames = [
        [' ', ' ', ' ', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', ' ', ' '],
        [' ', '*', ' ', '*', ' ', '*', ' '],
        ['*', ' ', '.', '*', '.', ' ', '*'],
        [' ', '*', ' ', '.', ' ', '*', ' '],
        [' ', ' ', '*', '.', '*', ' ', ' '],
        [' ', ' ', ' ', '.', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    width = _get_terminal_width()
    height = 20

    print("Fireworks starting! Press Ctrl+C to stop early.")
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            clear_screen()
            x = random.randint(5, width - 5)
            y = random.randint(3, height - 8)
            
            for frame in frames:
                output = [[' '] * width for _ in range(height)]
                for i, char in enumerate(frame):
                    if y + i < height:
                        if x - len(frame)//2 + i >= 0 and x - len(frame)//2 + i < width:
                             output[y+i][x - len(frame)//2 + i] = char
                             output[y+i][x + len(frame)//2 - i] = char
                
                clear_screen()
                print("\n".join("".join(row) for row in output))
                time.sleep(0.08)
            time.sleep(random.uniform(0.5, 2.0))
    except KeyboardInterrupt:
        pass
    finally:
        clear_screen()
        print("Fireworks show finished.")
        
def rain(duration: int = 10, chars: str = "01"):
    """
    Displays a Matrix-style rain animation.
    Note: Uses os.system('clear'/'cls') to clear the screen.

    Args:
        duration (int): The duration of the animation in seconds.
        chars (str): The characters to use for the rain.
    """
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    width = _get_terminal_width()
    height = 24
    
    columns = [random.randint(-height, height) for _ in range(width)]
    
    print("Rain starting! Press Ctrl+C to stop early.")
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            output = [[' '] * width for _ in range(height)]
            for i in range(width):
                if columns[i] < height:
                    if columns[i] >= 0:
                        output[columns[i]][i] = random.choice(chars)
                
                # Move the "drop"
                if random.random() > 0.95:
                    columns[i] = random.randint(-height, 0)
                else:
                    columns[i] += 1
            
            clear_screen()
            print("\n".join("".join(row) for row in output))
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        clear_screen()
        print("Rain stopped.")

# --- CONVENIENCE PRINT WRAPPERS ---

def print_box(*args, **kwargs):
    """Prints the result of box()."""
    print(box(*args, **kwargs))

def print_alert(*args, **kwargs):
    """Prints the result of alert()."""
    print(alert(*args, **kwargs))

def print_table(*args, **kwargs):
    """Prints the result of table()."""
    print(table(*args, **kwargs))

def print_banner(*args, **kwargs):
    """Prints the result of banner()."""
    print(banner(*args, **kwargs))
    
def print_gauge(*args, **kwargs):
    """Prints the result of gauge()."""
    print(gauge(*args, **kwargs))
    
def print_sparkline(*args, **kwargs):
    """Prints the result of sparkline()."""
    print(sparkline(*args, **kwargs))
    
def print_bar_chart(*args, **kwargs):
    """Prints the result of bar_chart()."""
    print(bar_chart(*args, **kwargs))
    
def print_hr(*args, **kwargs):
    """Prints the result of hr()."""
    print(hr(*args, **kwargs))

def print_listing(*args, **kwargs):
    """Prints the result of listing()."""
    print(listing(*args, **kwargs))

def print_checklist(*args, **kwargs):
    """Prints the result of checklist()."""
    print(checklist(*args, **kwargs))

def print_columns(*args, **kwargs):
    """Prints the result of columns()."""
    print(columns(*args, **kwargs))

def print_tree(*args, **kwargs):
    """Prints the result of tree()."""
    print(tree(*args, **kwargs))
    
def print_bubble(*args, **kwargs):
    """Prints the result of bubble()."""
    print(bubble(*args, **kwargs))

def print_cat(*args, **kwargs):
    """Prints the result of cat()."""
    print(cat(*args, **kwargs))
    
def print_maze(*args, **kwargs):
    """Prints the result of maze()."""
    print(maze(*args, **kwargs))
    
def print_mirror(*args, **kwargs):
    """Prints the result of mirror()."""
    print(mirror(*args, **kwargs))
    
def print_repeat(*args, **kwargs):
    """Prints the result of repeat()."""
    print(repeat(*args, **kwargs))
    
def print_staircase(*args, **kwargs):
    """Prints the result of staircase()."""
    print(staircase(*args, **kwargs))

def print_wave(*args, **kwargs):
    """Prints the result of wave()."""
    print(wave(*args, **kwargs))

def print_timestamp(*args, **kwargs):
    """Prints the result of timestamp()."""
    print(timestamp(*args, **kwargs))
    
def print_day_banner(*args, **kwargs):
    """Prints the result of day_banner()."""
    print(day_banner(*args, **kwargs))
    
def print_calendar(*args, **kwargs):
    """Prints the result of calendar()."""
    print(calendar(*args, **kwargs))

# --- DEMONSTRATION / SHOWCASE ---

def showcase():
    """Demonstrates all features of the Easy ASCII library."""
    
    print_banner("EASY ASCII")
    print_hr(title="v" + __version__)
    typewriter("A comprehensive, single-file, zero-dependency Python library.\n")

    # --- Static ASCII Art & Shapes ---
    print_hr(title="ASCII Art & Shapes")
    print_bubble("Hello! I'm a speech bubble.\nYou can put multi-line text in me.", style="light")
    print("\nSome fun shapes:")
    print_columns([cat()], num_cols=3, spacing=4)
    print_hr()
    print_maze(width=41, height=11)

    # --- Text Effects ---
    print_hr(title="Text Effects")
    print_wave("This text is wavy and fun!", amplitude=3)
    print("\nStaircase effect:")
    print_staircase("PYTHON")
    print("\nMirror effect:")
    print_mirror("Hello\nWorld")
    
    # --- Date & Time Utilities ---
    print_hr(title="Date & Time Utilities")
    print_timestamp("Application log entry.")
    print_day_banner()
    print("Here is the calendar for the current month:")
    print_calendar()
    print("And for a specific month (Dec 2024):")
    print_calendar(year=2024, month=12)
    
    # --- Boxes & Alerts ---
    print_hr(title="Boxes & Alerts")
    print_box(
        "This is a 'light' box with left alignment (default).\nIt supports multi-line content and auto-wraps text if the box is given a fixed width.",
        style="light",
        title="Light Style"
    )
    print_alert("Your operation was completed successfully.", alert_type="success", width=60)
    print_alert("A critical error occurred. Please check the logs.", alert_type="error", style="star", width=60)

    # --- Data Display ---
    print_hr(title="Data Display")
    sample_data = [
        {"ID": 1, "Name": "Python", "Type": "Programming Language", "Description": "A versatile and widely-used language."},
        {"ID": 2, "Name": "JavaScript", "Type": "Scripting Language", "Description": "The language of the web."},
        {"ID": 3, "Name": "SQL", "Type": "Query Language", "Description": "Manages and manipulates databases."},
    ]
    print_table(
        sample_data, 
        style="double",
        align={"ID": "center", "Name": "left"},
        max_col_width=30
    )
    
    # --- Lists & Trees ---
    print_hr(title="Lists & Trees")
    project_tasks = [
        ("Initialize project", True), ("Write core logic", True), ("Add unit tests", False)
    ]
    print("Project Status:")
    print_checklist(project_tasks, indent=4)
    
    file_system = {"project": {"src": {"main.py": "Entry"}, "README.md": "Docs"}}
    print("\nFile System:")
    print_tree(file_system)
    
    # --- Charts and Gauges ---
    print_hr(title="Charts & Gauges")
    print_gauge(75.3, 100, label="CPU Usage", length=40)
    server_load = [5, 10, 15, 20, 35, 50, 88, 90, 75, 60, 40, 20, 10]
    print(f"Server Load: {sparkline(server_load)}")
    poll_results = {"Python": 1250, "JavaScript": 980, "Go": 450}
    print_bar_chart(poll_results, title="Programming Language Poll")

    # --- Dynamic & Animated Elements ---
    print_hr(title="Dynamic & Animated Elements")
    
    # Progress Bar
    items = range(100)
    for i, item in enumerate(items):
        progress_bar(i + 1, len(items), prefix='Downloading:', suffix='Complete', length=50)
        time.sleep(0.01)
        
    # Spinner
    print("\nRunning a simulated multi-step task...")
    with Spinner("Initializing...", style="moon") as s:
        time.sleep(1.5)
        s.update_text("Fetching resources...")
        time.sleep(1.5)
    print("Task complete!")

    # Typewriter
    typewriter("This is the typewriter effect...", delay=0.08)

    # Timer
    timer(3)

    # Scroll
    try:
        print("Starting scroll animation for 5 seconds...")
        scroll_thread = threading.Thread(target=scroll, args=("... This is a very long scrolling message for your terminal ...",), daemon=True)
        scroll_thread.start()
        time.sleep(5)
        print("\nScrolling stopped. Press Enter to continue the showcase.")
    except Exception:
        pass

    # Animated Effects
    input("\nPress Enter to see the fireworks animation...")
    fireworks(duration=5)
    
    input("Press Enter to see the rain animation...")
    rain(duration=5, chars="easyascii")

    input("Press Enter to see the live clock (stop with Ctrl+C)...")
    clock()

    print_hr(title="Showcase Complete")

if __name__ == "__main__":
    showcase()