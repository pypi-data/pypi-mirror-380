import pyfiglet
from colorama import init, Fore, Style
import shutil

init(autoreset=True)

COLOR_MAP = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "yellow": Fore.YELLOW,
    "white": Fore.WHITE
}

def Text_Heading(
    text, 
    font="slant", 
    color="cyan", 
    width=100, 
    height=1.0,  # float: <1 smaller, >1 taller
    border=False, 
    underline=False,
    center=True
):
    """
    Prints a customizable ASCII heading in the console.
    """
    if isinstance(text, str):
        lines_to_print = [text]
    else:
        lines_to_print = text

    color_code = COLOR_MAP.get(color.lower(), Fore.CYAN)
    ascii_lines = []

    # Generate ASCII art
    for line in lines_to_print:
        ascii_text = pyfiglet.figlet_format(line, font=font, width=width)
        original_lines = ascii_text.splitlines()

        # Scale vertically
        scaled_lines = []
        if height >= 1:
            for l in original_lines:
                scaled_lines.extend([l] * int(height))
        else:
            step = int(1 / height)
            if step < 1: step = 1
            scaled_lines = original_lines[::step]

        ascii_lines.extend(scaled_lines)

    # Centering based on console width
    if center:
        term_width = shutil.get_terminal_size((width, 20)).columns
        ascii_lines = [l.center(term_width) for l in ascii_lines]

    # Add border
    if border:
        max_len = max(len(l) for l in ascii_lines)
        top_bottom = "*" * (max_len + 4)
        ascii_lines = [top_bottom] + [f"* {l} *" for l in ascii_lines] + [top_bottom]

    # Add underline
    if underline:
        underline_line = "-" * len(ascii_lines[-1])
        ascii_lines.append(underline_line)

    # Print final heading
    print(color_code + Style.BRIGHT + "\n".join(ascii_lines))

