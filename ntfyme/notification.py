import platform
import subprocess

from .utils.local_notify.linux import notify_linux
from .utils.local_notify.macos import notify_macos
from .utils.local_notify.windows import notify_windows
from .utils.mail.gmail import send_gmail
from .utils.mail.telegram import send_telegram


def notify_runner(notify_function, name, results):
    try:
        notify_function(results)
        return 1
    except Exception as e:
        print(f"Error occurred in {name} notifier. Error: {e}")
        return 0


def notify(results):
    """
    notify_macos   General notification function, which controls the calling of all the notification types
    Local - Linux, Macos
    Remote - mail, telegram
    """
    os = platform.system()
    os = os.lower()
    if os not in ["windows", "linux"]:
        os = "macos"

    try:
        if os == "linux":
            notify_linux(results)
        if os == "macos":
            notify_macos(results)
        else:
            notify_windows(results)

    except Exception as e:
        print("Error occurred in notification as", e)


#    gmail_output = notify_runner(send_gmail, "gmail", results)
#    telegram_output = notify_runner(send_telegram, "telegram", results)
#
#    return gmail_output, telegram_output
