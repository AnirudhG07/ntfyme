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


def term_print(results):
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
    print("\033[91mError:\n\033[0m"+results["error"])

    return 0
