from plyer import notification


def generate_notif(title, message):
    """
    General notifier.
    """
    try:
        notification.notify(
            title=title, message=message, app_icon=None, timeout=10, toast=False
        )
        return 0

    except Exception as e:
        print(f"Error in General Notification as {e}")
        return 1
    
def term_print(result):
    print(f"PID: {result['pid']}")
    print(f"Command run: {result['command']}")
    print(f"Time taken: {result['time_taken']} seconds")
    error_status = "Success" if result["error"] == "none" else "Failed"
    print(f"Output:\n{result['output']}")
    print(f"Error: {result['error']}")

    return 0
