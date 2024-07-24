from plyer import notification


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


def term_print(result):
    """
    This function is called only when the terminal_print is set to on in the config file.
    Thus the output will already be printed in the terminal.
    """
    print("\033[92m\nntfyme :: Diagnostics\033[0m")
    print("\033[93mPID:\033[0m", result["pid"])
    print("\033[93mCommand run:\033[0m", result["command"])
    print("\033[93mTime taken:\033[0m", result["time_taken"], "seconds")
    print("\033[91mError:\033[0m", result["error"])

    return 0
