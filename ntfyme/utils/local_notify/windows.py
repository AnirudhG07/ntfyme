import os
import toml

from .gen_notif import generate_notif

def windows_config():
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    config_path = os.path.join(package_root, "config.toml")

    with open(config_path, "r") as f:
        conf = toml.load(f)
    enabled = conf["local_windows"]["enabled"]
    success_sub = conf["local_windows"]["success_subject"]
    error_sub = conf["local_windows"]["error_subject"]

    return {
        "enabled": enabled,
        "success_sub": success_sub,
        "error_sub": error_sub,
    }


def notify_windows(results):
    """
    windows uses notify-send as default tool. This will be used for linux local notifications
    """
    configs = windows_config()

    if not configs["enabled"] == "on":
        return 0

    success_sub = configs["success_sub"]
    error_sub = configs["error_sub"]
    pid = results["pid"]
    error = results["error"]
    print(error)
    title, message = "", ""
    if error == "none":
        title = f"ntfyme :: {success_sub}"
        message = f"Process {pid} has ended successfully."
    else:
        title = f"ntfyme :: {error_sub}"
        message = f"Process {pid} ended with a failure."

    err_code = generate_notif(title, message)
    return err_code