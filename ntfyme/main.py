import os
import platform
import subprocess
import toml
from argparse import ArgumentParser

from .cmd.cmd_direct import direct_exec
from .cmd.cmd_pipe import pipe_exec
from .manager.encrypt import encrypt
from .manager.setup_interaction import setup
from .notification import notify
from .utils.log.log import log_add


def term_print(result):
    print(f"PID: {result['pid']}")
    print(f"Command run: {result['command']}")
    print(f"Time taken: {result['time_taken']} seconds")
    error_status = "Success" if result["error"] == "none" else "Failed"
    print(f"Output:\n{result['output']}")
    print(f"Error: {result['error']}")

    return 0

def main():
    """
    -> Handles the flags and errors
    -> calls functions based on the flags

    Arguments:
        None: Assumes the user wants to run the main command through pipe
        --cmd or -c : Input the command to cli as 'ntfyme --cmd <command>'
        --enc or -e : Encrypt password with your key for safety
        --log : The command log of ntfyme
        --config: The configuration file of ntfyme

        --help or -h : Shows the help message
        --version or -v : Shows the version of the program
    """

    parser = ArgumentParser(description="ntfyme")
    parser.add_argument("--cmd", "-c", help="Run the command through direct execution")
    parser.add_argument(
        "--log", "-l", action="store_true", help="The command log of ntfyme"
    )
    parser.add_argument(
        "--config", action="store_true", help="The configuration file of ntfyme"
    )
    parser.add_argument(
        "--enc",
        "-e",
        action="store_true",
        help="Encrypting password through ntfyme_key",
    )
    parser.add_argument(
        "--interactive-setup",
        "-i",
        action="store_true",
        help="Interactively setup your notification configuration",
    )

    args = parser.parse_args()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.toml")
    with open (config_path, "r") as file:
        config = toml.load(file)

    log_pager = config["ntfyme"]["log_pager"]
    terminal_print = config["ntfyme"]["terminal_print"]

    # Handling log and config arguments
    if args.log:
        log_path = os.path.join(script_dir, "utils", "log", "ntfyme.log")
        try:
            subprocess.run([log_pager, log_path])
        except Exception as e:
            print(f"Error occurred in opening log file. Error: {e}")
        return 0

    if args.config:
        config_path = os.path.join(script_dir, "config.toml")
        editor = os.getenv("EDITOR", "nano")  # Default to nano if EDITOR is not set
        # Open the config.toml file in the editor
        if platform.system() != "Windows":
            print(
                "For security reasons, please provide your sudo password to edit the config file."
            )
            subprocess.run(["sudo", editor, config_path])
            return 0
        else:
            subprocess.run([editor, config_path])
            return 0

    if args.enc:
        print(
            "Please provide your ntfyme_key for encrypting your password. This key is same throughout ntfyme. Whataver output you get will be based on the same key, please be mindful of the usage."
        )
        key = input("Enter your ntfyme_key: ")
        password = input("Enter your password: ")
        encrypted_password = encrypt(password, key)
        print(f"Encrypted password: {encrypted_password}")
        return 0

    if args.interactive_setup:
        setup()
        return 0

    if args.cmd:
        result = direct_exec(args.cmd)
        log_add(result)
        if terminal_print == "on":
            term_print(result)

    else:
        result = pipe_exec()
        log_add(result)
        if terminal_print == "on":
            term_print(result)

    notify(result)
    return 0


if __name__ == "__main__":
    main()
