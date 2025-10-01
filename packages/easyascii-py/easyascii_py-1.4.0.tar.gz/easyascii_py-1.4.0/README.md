# Easy ASCII
## A comprehensive, single-file, zero-dependency Python library for creating beautiful and functional text-based user interfaces and ASCII art.

[![PyPI version] (https://pypi.org/project/easyascii-py/1.0.2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Easy ASCII is designed to be incredibly simple to use while providing a powerful set of tools for command-line applications. Whether you need to display data in a clean table, create an eye-catching banner, or show progress for a long-running task, this library has you covered.

## ✨ Key Features

*   **📦 Advanced Boxes**: Create boxes with multiple border styles, titles, and text alignment.

*   **📊 Data Tables**: Generate perfectly formatted tables from lists of dictionaries with text wrapping.

*   **🅰️ FIGlet Banners**: Render large ASCII text banners with a built-in font.

*   **⏳ Progress Bars & Spinners**: Provide user feedback for long-running tasks.

*   **🌳 Tree Structures**: Visualize hierarchical data like file systems.

*   **🏛️ Multi-Column Layouts**: Arrange text into clean, evenly spaced columns.

*   **📝 Lists & Rules**: Create ordered/unordered lists and customizable horizontal rules.

*   **🐍 Pure Python**: Single file with zero external dependencies.

*   **💡 Developer Friendly**: Fully type-hinted with extensive docstrings and a flexible API.


## 📦 Installation

Install `easyascii` directly from PyPI:

`pip install easyascii-py==1.0.2`


### 🚀 Quick Start
Creating a rich console output is simple. Just import the functions you need and call them.


import easyascii

# 1. Create a banner for your application
easyascii.print_banner("My App")

# 2. Create a styled box for a welcome message
easyascii.print_box(
    "Welcome to my awesome application!\nHere is some important information.",
    title="Info",
    style="rounded"
)

# 3. Display data in a table
user_data = [

    {"ID": 1, "Username": "alex", "Status": "Active"},
    
    {"ID": 2, "Username": "brian_the_dev", "Status": "Active"},
    
    {"ID": 3, "Username": "casey", "Status": "Inactive"},
    
]

easyascii.print_table(user_data, style="double", align={"ID": "center"})


Output:

`#   # #   #        ###  ####  ####`

`## ##  # #        #   # #   # #   #`

`# # #   #         ##### ####  ####`

`#   #   #         #   # #     #`

`#   #   #         #   # #     #`


``╭──────────────── Info ─────────────────╮``

``│ Welcome to my awesome application!    │``

``│ Here is some important information.   │``

``╰───────────────────────────────────────╯``

``╔════╦═══════════════╦══════════╗``

``║ ID ║ Username      ║ Status   ║``

``╠════╬═══════════════╬══════════╣``

``║  1 ║ alex          ║ Active   ║``

``║  2 ║ brian_the_dev ║ Active   ║``

``║  3 ║ casey         ║ Inactive ║``

``╚════╩═══════════════╩══════════╝``

📚 API Reference
Convenience print_* Wrappers

### Display Functions

box()

table()

banner()

hr()

listing()

columns()

tree()

### Dynamic UI Functions

progress_bar()


### Spinner

Convenience print_

For every function that returns a string (like box, table, etc.), there is a corresponding "print_" version (e.g., print_box) that prints the result directly to the console. The "print_" versions accept the exact same arguments.


## Display Functions


box()


Creates a string of text inside an ASCII box.

Signature:


``def box(``
    ``text: Any,``
	
    style: str = "light",
	
    width: Optional[int] = None,
	
    title: str = "",
	
    align: str = "left",
	
    padding: Union[int, Tuple[int, int]] = 1
	
``) -> str``


**Parameters:**

text (Any): The text content to display. Can be multi-line.

style (str): The border style. Available: "light", "heavy", "double", "rounded", "star", "hash", "plus".

width (Optional[int]): Total width of the box. Auto-calculated if None.

title (str): An optional title to display on the top border.

align (str): Text alignment ("left", "center", "right").

padding (Union[int, Tuple[int, int]]): Horizontal and vertical padding. E.g., 1 or (2, 1).


Example:


``message = "This box is centered and has a heavy border style with custom padding."``
``print(easyascii.box(message, style="heavy", title="Attention", align="center", padding=(4, 1), width=70))``

Output:


``┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Attention ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓``

``┃                                                                    ┃``

``┃        This box is centered and has a heavy border style           ┃``

``┃                       with custom padding.                         ┃``

``┃                                                                    ┃``

``┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛``



table()


Creates a formatted ASCII table from a list of dictionaries.
Signature:


``def table(``
    ``data: List[Dict[str, Any]],``
	
    headers: Optional[List[str]] = None,
	
    style: str = "light",
	
    align: Union[str, Dict[str, str]] = "left",
	
    max_col_width: Optional[int] = None
	
``) -> str``


**Parameters:**

data (List[Dict]): A list of dictionaries, where each dict is a row.

headers (Optional[List[str]]): A list of header keys. If None, uses keys from the first row.

style (str): The border style (see box() for options).

align (Union[str, Dict]): Default alignment, or a dictionary mapping header keys to alignments.

max_col_width (Optional[int]): Maximum width for any single column (enables text wrapping).

Example:


``data = [``
    ``{"File": "main.py", "Size (KB)": 12.5, "Last Modified": "2023-10-27"},``
	
    {"File": "utils/helpers.py", "Size (KB)": 34.1, "Last Modified": "2023-10-26"},
	
    {"File": "README.md", "Size (KB)": 2.8, "Last Modified": "2023-10-27"},
	
``]``
``print(easyascii.table(data, style="light", align={"Size (KB)": "right"}))``


Output:


``┌──────────────────┬─────────────┬───────────────┐``

``│ File             │ Size (KB)   │ Last Modified │``

``├──────────────────┼─────────────┼───────────────┤``

``│ main.py          │        12.5 │ 2023-10-27    │``

``│ utils/helpers.py │        34.1 │ 2023-10-26    │``

``│ README.md        │         2.8 │ 2023-10-27    │``

``└──────────────────┴─────────────┴───────────────┘``




banner()


Renders large ASCII text.

Signature:

``def banner(text: str) -> str``

Example:

``print(easyascii.banner("Ready!"))``


Output:

``####  #####  ###  ####  #   #   #``

``#   # #     #   # #   #  # #    #``

``####  ###   ##### #   #   #     #``

``# #   #     #   # #   #   #``

``#  #  ##### #   # ####    #     #``



hr()

Creates a horizontal rule (a line separator).

Signature:


``def hr(width: Optional[int] = None, char: str = "-", title: str = "") -> str``

Example:

``print(easyascii.hr(width=50, char="=", title="Section Break"))``

Output:


``================= Section Break ==================``


listing()


Formats an iterable into an ordered or unordered list.

Signature:


``def listing(items: Iterable[Any], ordered: bool = False, indent: int = 2) -> str``


Example:


``tasks = ["Design UI", "Implement backend", "Write tests"]``

``print("Todo List:")``

``print(easyascii.listing(tasks, ordered=True, indent=4))``


Output:


``Todo List:``
``    1. Design UI``
``    2. Implement backend``
``    3. Write tests``


columns()


Arranges a list of strings into multiple columns.
Signature:


``def columns(texts: List[str], num_cols: int = 2, spacing: int = 4) -> str``
Example:


``items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]``

``print(easyascii.columns(items, num_cols=3, width=50))``


Output:


``Apple          Elderberry``

``Banana         Fig``

``Cherry         Grape``

``Date``


tree()


Generates an ASCII tree structure from a nested dictionary.

Signature:


``def tree(data: Dict[str, Any]) -> str``


Example:


``file_system = {``

``    "project/": {``

``        "src/": {``

``            "main.py": None,``

``            "utils.py": None``

``        },``

``        "README.md": None``

``    }``

``}``

``print(easyascii.tree(file_system))``


Output:


``└── project/``
``    ├── src/``
``    │   ├── main.py``
``    │   └── utils.py``
``    └── README.md``
	
	
## Dynamic UI Functions


progress_bar()


Prints a dynamic, single-line progress bar. Should be called inside a loop.
Signature:

``def progress_bar(``

``    iteration: int,``

``    total: int,``

``    prefix: str = 'Progress:',``

``    suffix: str = 'Complete',``

``    length: int = 50,``

``    fill: str = '█'``

``)``


Example:


``import time``

``import easyascii``


``total_items = 200``

``for i in range(total_items + 1):``

``    easyascii.progress_bar(i, total_items, prefix='Processing:', suffix='Done')``
    
``    time.sleep(0.01)``
    
``Output (at the end of the loop):``


``Processing: |██████████████████████████████████████████████████| 100.0% Done``


## Spinner
A context manager for displaying a loading spinner for long operations.
Signature:

``class Spinner:``
``    def __init__(self, text: str = "Loading...", style: str = "dots", delay: float = 0.1)``
``style (str): The spinner animation style. Available: "dots", "line", "arrow", "box".``


Example:

``import time``

``import easyascii``

``with easyascii.Spinner("Fetching data from API...", style="arrow"):``

``    time.sleep(3)``

``print("Data fetched successfully!")``

``Output (during execution):``

``Fetching data from API... ↑  (character rotates)``

``Output (after completion):``


``Data fetched successfully!``


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
## 📜 License
This project is licensed under the MIT License.
