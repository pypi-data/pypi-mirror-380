# tui_inputs_pro.py
from colorama import init, Fore, Style
from InquirerPy import prompt

# Initialize colorama
init(autoreset=True)

# ------------------------------
# Standard colored input
# ------------------------------
def ColorInput(message: str, color: str = "cyan", style: str = "bright", default: str = None):
    """
    Displays a colored input prompt and returns user input.
    """
    COLOR_MAP = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "yellow": Fore.YELLOW,
        "white": Fore.WHITE
    }
    color_code = COLOR_MAP.get(color.lower(), Fore.CYAN)
    style_code = Style.BRIGHT if style.lower() == "bright" else Style.NORMAL
    prompt_msg = f"{color_code}{style_code}{message} "
    if default:
        prompt_msg += f"[default: {default}] "
    result = input(prompt_msg)
    if result.strip() == "" and default is not None:
        return default
    return result

# ------------------------------
# Interactive single selection
# ------------------------------
def OneSelect(message: str, choices: list, default=None):
    question = [
        {
            "type": "list",
            "name": "selection",
            "message": message,
            "choices": choices,
            "default": default
        }
    ]
    result = prompt(question)
    return result.get("selection")

# ------------------------------
# Interactive multi-select
# ------------------------------
def MultiSelect(message: str, choices: list, default=None):
    question = [
        {
            "type": "checkbox",
            "name": "selection",
            "message": message,
            "choices": choices,
            "default": default
        }
    ]
    result = prompt(question)
    return result.get("selection")

# ------------------------------
# Numeric input with validation
# ------------------------------
def RangeSelect(message: str, default=None, min_val=None, max_val=None):
    while True:
        val = ColorInput(message, default=str(default) if default else None)
        if val.isdigit():
            val = int(val)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Value must be between {min_val} and {max_val}")
            else:
                return val
        else:
            print("Please enter a valid number.")


def ColorText(text, color="cyan", style="bright"):
    COLOR_MAP = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "yellow": Fore.YELLOW,
        "white": Fore.WHITE,
    }
    color_code = COLOR_MAP.get(color.lower(), Fore.CYAN)
    style_code = Style.BRIGHT if style.lower() == "bright" else Style.NORMAL
    print(f"{color_code}{style_code}{text}{Style.RESET_ALL}")

from tabulate import tabulate
import shutil

# --- Configuration (These variables must be defined globally or passed in) ---
# Assuming these are defined at the top of your script:
MIN_NAME_WIDTH = 18 
MIN_ADDRESS_WIDTH = 25 
MIN_SCHOOL_WIDTH = 12
# ----------------------------------------------------------------------------


def display_centered_table(student_data, title="Student Records"):
    """
    Generates, pads, and horizontally centers a table and its title 
    from student dictionary data.
    """
    
    if not student_data or not isinstance(student_data, dict):
        # Print a simple message if data is missing, no need to center
        print(f"\n\n--- {title} ---")
        print("No student data or invalid format to display.")
        print("\n\n")
        return

    # 1. Transform and Pad the Data (No change needed here)
    student_list = []
    for key, record in student_data.items():
        if isinstance(record, dict):
            row = {"Student_Key": key}
            
            # Apply padding to widen columns 
            name = record.get("name", "").ljust(MIN_NAME_WIDTH)
            address = record.get("address", "").ljust(MIN_ADDRESS_WIDTH)
            school = record.get("school", "").ljust(MIN_SCHOOL_WIDTH)

            # Store padded values
            row["name"] = name
            row["address"] = address
            row["school"] = school
            
            # Merge
            temp_row = {}
            temp_row.update(record)
            temp_row.update(row)
            student_list.append(temp_row)
        
    if not student_list:
        print(f"\n\n--- {title} ---")
        print("Error: Transformed data is empty or invalid.")
        print("\n\n")
        return

    # Define the order of columns to display
    display_keys = [
        "Student_Key", "name", "class", "school", 
        "phone", "address", "fees", "dob", "adm"
    ]
    
    # Prepare final data rows, ensuring consistency
    table_data = []
    for row in student_list:
        table_data.append([row.get(k, '') for k in display_keys])

    # 2. Generate the table string
    table_string = tabulate(table_data, headers=display_keys, tablefmt="fancy_grid")

    # 3. Center the table AND the title
    
    try:
        terminal_width = shutil.get_terminal_size().columns
    except OSError:
        terminal_width = 80 # Fallback 
    
    table_lines = table_string.split('\n')
    table_width = max(len(line) for line in table_lines)
    
    # Calculate padding based on the widest table line
    padding = max(0, (terminal_width - table_width) // 2)
    indent = " " * padding

    # --- NEW LOGIC: Center and Print the Title ---
    
    # 3a. Format the title string
    title_text = f"--- {title} ---"
    
    # 3b. Center the title based on the TABLE width, so it aligns with the table
    # We use table_width for the reference, not terminal_width, so the title 
    # sits perfectly above the table borders.
    title_padding = max(0, (table_width - len(title_text)) // 2)
    centered_title = title_text.center(table_width) 

    # Print a couple of newlines first
    print("\n\n") 
    
    # Print the centered title using the table's calculated left indent
    print(indent + centered_title)
    
    # Print a separator line that matches the table width (optional, but looks good)
    separator = "-" * table_width
    print(indent + separator)
    # ---------------------------------------------

    # Print centered table
    for line in table_lines:
        ColorText(indent + line)

    print("\n\n")