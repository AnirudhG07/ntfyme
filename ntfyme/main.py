import os
import platform
import subprocess

import rich_click as click
import toml

from ntfyme.cmd.cmd_direct import direct_exec
from ntfyme.cmd.cmd_pipe import pipe_exec
from ntfyme.manager.encrypt import encrypt
from ntfyme.manager.setup_interaction import setup
from ntfyme.notification import notify
from ntfyme.utils.log.log import log_add


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option("ntfyme v0.0.1", "--version", "-v")
def main():
    """
    ntfyme is a simple notification tool to notify yourself when a long running process ends with local ping, gmail, telegram, etc.
    For setup guidelines or if you are facing any issue, checkout the official github repository at: https://github.com/AnirudhG07/ntfyme.
    """
    pass


@main.command()
@click.option("--cmd", "-c", help="Run the command through direct execution")
@click.option(
    "--enc", "-e", is_flag=True, help="Encrypt password with your key for safety"
)
@click.option(
    "--interactive-setup",
    "-i",
    is_flag=True,
    help="Interactively setup your notification configuration",
)
@click.option(
    "--track-process",
    "-t",
    is_flag=True,
    help="Track the process for suspensions and terminate if stalled for a long time",
)
def run(cmd, enc, interactive_setup, track_process):
    """
    Run various commands and options for ntfyme.
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

    if interactive_setup:
        setup()
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

    try:
        if cmd:
            results = direct_exec(cmd, terminal_print, track_process)
            log_info["execution"] = "Direct :: 0"
        else:
            results = pipe_exec(terminal_print, track_process)
            log_info["execution"] = "Pipe :: 0"

    except Exception as e:
        click.echo(f"Error occurred in command execution. Error: {e}")
        log_info["error"] = "Execution: 1"

    try:
        notify(results, key)
        log_info["notify"] = 0
    except Exception as e:
        click.echo(f"Error occurred in notification. Error: {e}")
        log_info["notify"] = 1

    log_add(results, log_info)


@main.command()
def log():
    """The command log of ntfyme"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, "utils", "log", "ntfyme.log")
    config_path = os.path.join(script_dir, "config.toml")
    with open(config_path, "r") as file:
        config = toml.load(file)

    log_pager = config["ntfyme"]["log_pager"]

    try:
        subprocess.run([log_pager, log_path])
    except Exception as e:
        click.echo(f"Error occurred in opening log file. Error: {e}")


@main.command()
def config():
    """The configuration file of ntfyme"""
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
        subprocess.run([editor, config_path])


if __name__ == "__main__":
    main()
