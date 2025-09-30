from colorama import Fore, Style, init

# Initialize colorama (for Windows too)
init(autoreset=True)

def Success(msg: str):
    print(f"{Fore.GREEN}{Style.BRIGHT}✔ SUCCESS: {Style.RESET_ALL}{msg}")

def Error(msg: str):
    print(f"{Fore.RED}{Style.BRIGHT}✖ ERROR: {Style.RESET_ALL}{msg}")

def Warn(msg: str):
    print(f"{Fore.YELLOW}{Style.BRIGHT}⚠ WARNING: {Style.RESET_ALL}{msg}")

def Info(msg: str):
    print(f"{Fore.CYAN}{Style.BRIGHT}ℹ INFO: {Style.RESET_ALL}{msg}")

def Question(msg: str):
    print(f"{Fore.MAGENTA}{Style.BRIGHT}? QUESTION: {Style.RESET_ALL}{msg}")
