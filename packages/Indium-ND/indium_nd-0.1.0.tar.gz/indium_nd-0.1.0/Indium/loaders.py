import time

# Rich Loader
try:
    from rich.console import Console
    from rich.progress import Progress
    _rich_available = True
except ImportError:
    _rich_available = False

# Alive-progress Loader
try:
    from alive_progress import alive_bar
    _alive_available = True
except ImportError:
    _alive_available = False

# Yaspin Loader
try:
    from yaspin import yaspin
    _yaspin_available = True
except ImportError:
    _yaspin_available = False


def DownloadStyle(total=100, desc="Processing...", speed=0.05):
    """Progress bar with Rich"""
    if not _rich_available:
        raise ImportError("Rich is not installed. Run: pip install rich")
    console = Console()
    with Progress() as progress:
        task = progress.add_task(f"[cyan]{desc}", total=total)
        for _ in range(total):
            time.sleep(speed)
            progress.update(task, advance=1)
    console.log("[green]Done!")


def RetroStyle(total=100, desc="Processing...", speed=0.05):
    """Smooth animated loader with alive-progress"""
    if not _alive_available:
        raise ImportError("alive-progress is not installed. Run: pip install alive-progress")
    with alive_bar(total, title=desc) as bar:
        for _ in range(total):
            time.sleep(speed)
            bar()


def MiniStyle(total=100, desc="Processing...", speed=0.05, color="cyan"):
    """Spinner with yaspin (simulates total steps)"""
    if not _yaspin_available:
        raise ImportError("yaspin is not installed. Run: pip install yaspin")
    with yaspin(text=desc, color=color) as spinner:
        for _ in range(total):
            time.sleep(speed)
        spinner.ok("✔")
