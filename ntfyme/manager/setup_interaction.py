import importlib.util
import os
import re
import time

import requests
import tomlkit
from beaupy import select
from beaupy.spinners import *
from rich.console import Console

console = Console()
config_path = os.path.join(os.path.dirname(__file__), "..", "config.toml")


def valid_telegram_chat_id():
    chat_id = ""
    while True:
        chat_id = input("\033[93m" + "Enter Telegram Chat ID: " + "\033[0m")
        if chat_id.isdigit():  # Ensuring the chat ID is an integer
            return int(chat_id)
        print("\033[91m" + "Invalid Telegram Chat ID: Must be an integer." + "\033[0m")


def valid_telegram_token():
    token = ""
    while True:
        token = input("\033[93m" + "Enter Telegram Bot Token: " + "\033[0m")
        response = requests.get(
            f"https://api.telegram.org/bot{token}/getMe", timeout=10
        )
        spinner = Spinner(DOTS, "Verifying bot token...")
        spinner.start()

        time.sleep(4)

        spinner.stop()
        if response.status_code == 200 and response.json().get("ok"):
            return token
        if response.status_code >= 400:
            print(
                "Unable to authenticate with Telegram API. Please check your internet or input a valid token."
            )
        else:
            print(
                "\033[91m"
                + "Invalid Telegram Bot Token: Must be a valid token."
                + "\033[0m"
            )


def valid_gmail_email():
    gmail_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@gmail\.com$")
    email = ""
    input_msg = "\033[93m" + "Enter Gmail Email ID: " + "\033[0m"
    while True:
        email = input(input_msg)
        if gmail_pattern.match(email):
            return email
        print(
            "\033[91m" + "Invalid Gmail Email ID: Must be a valid Gmail ID." + "\033[0m"
        )


def telegram_setup():
    """
    Setup for telegram bot.
    """
    print(
        "\n\033[92m"
        + "Welcome to the telegram setup. Before starting this setup, please make sure to have read the guidelines on setting up the telegram bot for ntfyme at: https://github.com/AnirudhG07/ntfyme/blob/main/docs/setup_guide/telegram_bot.md. You will be required to enter your telegram chat_id and token."
        + "\033[0m\nNote: This will not be stored with encryption. "
    )

    chat_id = valid_telegram_chat_id()
    token = valid_telegram_token()

    print("\033[93m" + "Do you want to enable telegram notifications?" + "\033[0m")

    choice = select(["on", "off"], cursor=">", cursor_style="cyan")
    enabled = choice

    with open(config_path, "r") as file:
        tele_toml = tomlkit.parse(file.read())
    # Directly modify the document object
    if "telegram" not in tele_toml:
        tele_toml["telegram"] = tomlkit.table()
    tele_toml["telegram"]["chat_id"] = chat_id
    tele_toml["telegram"]["token"] = token
    tele_toml["telegram"]["enabled"] = enabled

    # Write the modified document object back to the file
    with open(config_path, "w") as file:
        file.write(tomlkit.dumps(tele_toml))

    spinner = Spinner(DOTS, "Setting up...")
    spinner.start()

    time.sleep(1)

    spinner.stop()
    print("Telegram setup complete.")
    return 0


def gmail_setup():
    """
    Setup for gmail.
    """
    # color it green
    print(
        "\n\033[92m"
        + "Welcome to the gmail setup. Before starting this setup, please make sure to have read the guidelines on setting up your gmail for security purposes. You will be required to enter your gmail id, password and ntfyme_key."
        + "\033[0m"
    )
    print("Note: This will be stored with encryption for security purposes.")
    mail_id = valid_gmail_email()
    password = input("\033[93m" + "Enter your gmail app password: " + "\033[0m")
    key = input("\033[93m" + "Enter your ntfyme_key: " + "\033[0m")

    print(
        "\033[93m"
        + "Do you want to enable gmail notification? Enabling this will ask for your ntfyme_key everytime you run ntfyme. (on/off): "
        + "\033[0m"
    )

    choice = select(["on", "off"], cursor=">", cursor_style="cyan")
    enabled = choice

    encrypt_path = os.path.join(os.path.dirname(__file__), "encrypt.py")
    spec = importlib.util.spec_from_file_location("encrypt", encrypt_path)
    encrypt_modeule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(encrypt_modeule)
    encrypted_password = encrypt_modeule.encrypt(password, key)

    with open(config_path, "r") as file:
        gmail_toml = tomlkit.parse(file.read())
    # Directly modify the document object
    if "telegram" not in gmail_toml:
        gmail_toml["telegram"] = tomlkit.table()

    gmail_toml["mail"]["mail_id"] = mail_id
    gmail_toml["mail"]["password"] = encrypted_password
    gmail_toml["mail"]["enabled"] = enabled
    # Write the modified document object back to the file
    with open(config_path, "w") as file:
        file.write(tomlkit.dumps(gmail_toml))

    spinner = Spinner(DOTS, "Setting up...")
    spinner.start()

    time.sleep(1)

    spinner.stop()
    print("Gmail setup complete.")
    return 0


def setup():
    """
    Main interaction function for inputting keys and password and writing to config.toml
    """
    print(
        "\033[92m"
        + "Welcome to the ntfyme setup. This setup will help you configure your notification settings.\n"
        + "\033[0m"
        + "\033[95m"
        + "Note: If this is not your first time configuring ntfyme, the previous settings will be overwritten."
        + "\033[0m\n",
    )
    # color option purple and bold and text yello
    options = [
        "\033[91m" + "[1]" + "\033[0m" + "\033[94m" + " Gmail setup" + "\033[0m",
        "\033[91m" + "[2]" + "\033[0m" + "\033[94m" + " Telegram setup" + "\033[0m",
        "\033[91m" + "[3]" + "\033[0m" + "\033[94m" + " Exit" + "\033[0m",
    ]

    choice = select(options, cursor=">", cursor_style="cyan")

    if choice == options[0]:
        gmail_setup()
    elif choice == options[1]:
        telegram_setup()
    else:
        print("Thanks for using ntfyme!")
        return 0
