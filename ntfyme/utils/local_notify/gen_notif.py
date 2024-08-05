import os

import toml
from plyer import notification
from rich.console import Console
from rich.table import Table
from rich.text import Text


def generate_notif(title, message, timeout):
    """
    General notifier.
    """
    try:
        notification.notify(title=title, message=message, app_icon="", timeout=timeout)
        return 0

    except Exception as e:
        print(f"Error in General Notification as {e}")
        return 1


def rich_print(results):
    """
    This function is called only when the terminal_print is set to on in the config file.
    Thus the output will already be printed in the terminal.
    """
    console = Console()

    # Create a table to display results
    table = Table(title="ntfyme :: Diagnostics", title_style="bold green")
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="cyan")

    table.add_row("PID", str(results["pid"]))
    table.add_row("Command run", results["command"])
    table.add_row("Time taken", f"{results['time_taken']} seconds")
    table.add_row("Return Code", str(results["return_code"]))
    table.add_row("Remarks", results["remarks"])

    # Add the error as a separate section with a different style
    if results.get("error"):
        console.print(table)
        console.print(Text("Error:", style="bold red"), style="bold red")
        console.print(results["error"], style="red")
    else:
        console.print(table)

    return 0


def col_print(results):
    """
    This function is called only when the terminal_print is set to on in the config file.
    Thus the output will already be printed in the terminal.
    """
    print("\033[92m\nntfyme :: Diagnostics\033[0m")
    print("\033[93mPID:\033[0m", results["pid"])
    print("\033[93mCommand run:\033[0m", results["command"])
    print("\033[93mReturn Code:\033[0m", results["return_code"])
    print("\033[93mRemarks:\033[0m", results["remarks"])
    print("\033[93mTime taken:\033[0m", results["time_taken"], "seconds")
    print("\033[91mError:\n\033[0m" + results["error"])

    return 0


def term_print(results):
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    config_file = os.path.join(package_root, "config.toml")

    with open(config_file, "r") as file:
        config = toml.load(file)

    try:
        if config["ntfyme"]["richer"] == "on":
            rich_print(results)
        else:
            col_print(results)
        return 0

    except:
        print("Error in printing ntfyme diagnostics to Terminal.")
        return 1
