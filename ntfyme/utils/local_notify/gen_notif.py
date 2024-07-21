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
