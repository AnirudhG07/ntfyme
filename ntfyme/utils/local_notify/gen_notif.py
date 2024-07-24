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
    print("\nntfyme :: Diagnostics")
    print(f"PID: {result['pid']}")
    print(f"Command run: {result['command']}")
    print(f"Time taken: {result['time_taken']} seconds")
    print(f"Error:\n{result['error']}")

    return 0
