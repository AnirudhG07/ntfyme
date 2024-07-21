import os
import subprocess

import toml


def macos_config():
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    config_path = os.path.join(package_root, "config.toml")

    with open(config_path, "r") as f:
        conf = toml.load(f)

    enabled = conf["local_macos"]["enabled"]
    success_sub = conf["local_macos"]["success_subject"]
    error_sub = conf["local_macos"]["error_subject"]
    success_sound = conf["local_macos"]["success_sound"]
    error_sound = conf["local_macos"]["error_sound"]

    return {
        "enabled": enabled,
        "success_sub": success_sub,
        "error_sub": error_sub,
        "success_sound": success_sound,
        "error_sound": error_sound,
    }


def notify_macos(results):
    """
    macos uses osascript for notifications. This command will be used for the notifications.
    """
    configs = macos_config()

    if not configs["enabled"] == "on":
        return 0

    success_sub = configs["success_sub"]
    error_sub = configs["error_sub"]
    success_sound = configs["success_sound"]
    error_sound = configs["error_sound"]
    pid = results["pid"]
    error = results["error"]

    title, message, sound = "", "", ""
    if error != "none":
        title = f"ntfyme :: {error_sub}"
        message = f"Process {pid} ended with failure."
        sound = error_sound
    else:
        title = f"ntfyme :: {success_sub}"
        message = f"Process {pid} ended successfully."
        sound = success_sound
    # AppleScript for notification
    script = f"""
    osascript -e 'display notification "{message}" with title "{title}" sound name "{sound}"'
    """

    try:
        subprocess.run(script, shell=True, check=True)
    except Exception as e:
        print(e)
        return 1
