import os
import platform

import toml

from .utils.local_notify.gen_notif import term_print
from .utils.local_notify.linux import notify_linux
from .utils.local_notify.macos import notify_macos
from .utils.local_notify.windows import notify_windows
from .utils.mail.gmail import send_gmail
from .utils.mail.telegram import send_telegram


def notify_runner(notify_function, name, results, key):
    try:
        if name == "gmail":
            notify_function(results, key)
        else:
            notify_function(results)
        return 1
    except Exception as e:
        print(f"Error occurred in {name} notifier. Error: {e}")
        return 0


def notify(results, key):
    """
    notify_macos   General notification function, which controls the calling of all the notification types
    Local - Linux, Macos
    Remote - mail, telegram
    """
    system = platform.system()
    system = system.lower()
    if system not in ["windows", "linux"]:
        system = "macos"

    try:
        if system == "linux":
            notify_linux(results)
        if system == "macos":
            notify_macos(results)
        else:
            notify_windows(results)

    except Exception as e:
        print("Error occurred in notification as", e)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.toml")
    with open(config_path, "r") as file:
        config = toml.load(file)

    # Local terminal printing.
    terminal_print = config["ntfyme"]["terminal_print"]
    if terminal_print == "on":
        term_print(results)

    gmail_output, telegram_output = 0, 0
    if config["mail"]["enabled"] == "on":
        gmail_output = notify_runner(send_gmail, "gmail", results, key)
    if config["telegram"]["enabled"] == "on":
        telegram_output = notify_runner(send_telegram, "telegram", results, key)

    return gmail_output, telegram_output
