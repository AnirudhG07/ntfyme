import os
import platform
import subprocess

import rich_click as click
import toml

from ntfyme.cmd.cmd_direct import direct_exec
from ntfyme.cmd.cmd_pipe import pipe_exec
from ntfyme.manager.encrypt import encrypt
from ntfyme.manager.setup_interaction import setup as notification_setup
from ntfyme.notification import notify
from ntfyme.utils.log.log import log_add


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option("ntfyme v0.0.1", "--version", "-v")
def main():
    """
    ntfyme is a simple notification tool to notify yourself when a long running process ends with local ping, gmail, telegram, etc.
    For more information on each of commands, you can run - ntfyme OPTION --help or -h.
    For setup guidelines or if you are facing any issue, checkout the official github repository at: https://github.com/AnirudhG07/ntfyme.
    """
    pass


@main.command()
@click.option("--cmd", "-c", help="Run the command through direct execution")
@click.option(
    "--enc", "-e", is_flag=True, help="Encrypt password with your key for safety"
)
@click.option(
    "--track-process",
    "-t",
    is_flag=True,
    help="Track the process for suspensions and terminate if stalled for a long time",
)
def exec(cmd, enc, track_process):
    """
    Run main commands and options for ntfyme.
    To directly run a command, use - ntfyme exec -c "your_command"
    To pipe your command & run, use -  echo "your_command" | ntfyme exec
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.toml")
    with open(config_path, "r") as file:
        config = toml.load(file)

    terminal_print = config["ntfyme"]["terminal_print"]

    if enc:
        click.echo(
            "Please provide your ntfyme_key for encrypting your password. This key is the same throughout ntfyme. Whatever output you get will be based on the same key, please be mindful of the usage."
        )
        key = click.prompt("Enter your ntfyme_key")
        password = click.prompt("Enter your password", hide_input=True)
        encrypted_password = encrypt(password, key)
        click.echo(f"Encrypted password: {encrypted_password}")
        return

    results, key = None, None
    log_info = {"key": 0}

    if config["mail"]["enabled"] == "on":
        key = click.prompt("Enter your ntfyme_key", default="", show_default=False)
        if not key:
            log_info["key"] = 1

    if track_process:
        track_process = "on"
        log_info["track_process"] = 0
    else:
        track_process = "off"
        log_info["track_process"] = 1

    if cmd:
        try:
            results = direct_exec(cmd, terminal_print, track_process)
            log_info["execution"] = "Direct :: 0"
        except Exception as e:
            click.echo(f"Error occurred in direct execution. Error: {e}")
            log_info["execution"] = "Direct :: 1"
    else:
        try:
            results = pipe_exec(terminal_print, track_process)
            log_info["execution"] = "Pipe :: 0"

        except Exception as e:
            click.echo(f"Error occurred in piped execution. Error: {e}")
            log_info["error"] = "Pipe: 1"

    try:
        notify(results, key)
        log_info["notify"] = 0
    except Exception as e:
        click.echo(f"Error occurred in notification. Error: {e}")
        log_info["notify"] = 1

    log_add(results, log_info)


@main.command()
@click.option(
    "--recent",
    "-r",
    is_flag=True,
    help="Display the log entry for the latest command run.",
)
def log(recent):
    """The command log of ntfyme. For any debugging, it is advised to check the log along with any Errors printed."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, "utils", "log", "ntfyme.log")
    config_path = os.path.join(script_dir, "config.toml")
    with open(config_path, "r") as file:
        config = toml.load(file)

    log_pager = config["ntfyme"]["log_pager"]
    log_path = os.path.join(script_dir, "utils", "log", "ntfyme.log")

    try:
        if recent:
            subprocess.run(["tail", "-n", "7", log_path])  # Display the last 10 lines
        else:
            subprocess.run([log_pager, log_path])
    except Exception as e:
        print(f"Error occurred in opening log file. Error: {e}")


@main.command()
def config():
    """The configuration file of ntfyme. You will be prompted to provide password to access it for safety."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.toml")
    editor = os.getenv("EDITOR", "nano")  # Default to nano if EDITOR is not set
    # Open the config.toml file in the editor
    if platform.system() != "Windows":
        click.echo(
            "For security reasons, please provide your sudo password to edit the config file."
        )
        subprocess.run(["sudo", editor, config_path])
    else:
        import ctypes

        if ctypes.windll.shell32.IsUserAnAdmin() != 0:
            subprocess.run([editor, config_path])
        else:
            print("Please run this command as admin. Thank you!")
    return 0


@main.command()
def setup():
    """Interactively setup Gmail, Telegram, etc. for ntfyme."""
    notification_setup()
    return 0


if __name__ == "__main__":
    main()
