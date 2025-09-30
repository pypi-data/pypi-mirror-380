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

