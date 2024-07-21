import platform
import subprocess

from .utils.local_notify.linux import notify_linux
from .utils.local_notify.macos import notify_macos
from .utils.mail.gmail import send_gmail
from .utils.mail.telegram import send_telegram


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
    except Exception as e:
        print("Error occurred in notification as", e)


#    try:
#        send_telegram(results)
#    except Exception as e:
#        print(f"Error in telegram message as {e}")
#
#
#    try:
#        send_gmail(results)
#    except Exception as e:
#        print("Error in gmail as {e}")
#
