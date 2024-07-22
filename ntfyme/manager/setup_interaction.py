import importlib.util
import os

import tomlkit

config_path = os.path.join(os.path.dirname(__file__), "..", "config.toml")


def loop_on_off(choice):
    """
    Loop to check if the input is on or off.
    """
    while choice.lower() not in ["on", "off"]:
        print("Invalid choice. Please enter choice among on/off.")
        choice = input("Enter your choice: ")
    return choice


def telegram_setup():
    """
    Setup for telegram bot.
    """
    print(
        "Welcome to the telegram setup. Before starting this setup, please make sure to have read the guidelines on setting up the telegram bot for ntfyme. You will be required to enter your telegram chat_id and token."
    )
    print("Note: This will not be stored with encryption. ")
    chat_id = input("Enter your telegram chat_id: ")
    token = input("Enter your telegram token: ")

    enabled = input("Do you want to enable telegram notifications? (on/off): ")
    enabled = loop_on_off(enabled)

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

    print("Telegram setup complete.")
    return 0


def gmail_setup():
    """
    Setup for gmail.
    """
    print(
        "Welcome to the gmail setup. Before starting this setup, please make sure to have read the guidelines on setting up your gmail for security purposes. You will be required to enter your gmail id, password and ntfyme_key."
    )
    print("Note: This will be stored with encryption for security purposes.")
    mail_id = input("Enter your gmail email: ")
    password = input("Enter your gmail password: ")
    key = input("Enter your ntfyme_key: ")
    enabled = input(
        "Do you want to enable gmail notification? Enabling this will ask for your ntfyme_key everytime you run ntfyme. (on/off): "
    )
    enabled = loop_on_off(enabled)

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

    print("Gmail setup complete.")
    return 0


def setup():
    """
    Main interaction function for inputting keys and password and writing to config.toml
    """
    print(
        "Welcome to the ntfyme setup. This setup will help you configure your notification settings. Note: If this is not your first time configuring ntfyme, the previous settings will be overwritten.\n"
    )
    print("[1] Gmail setup")
    print("[2] Telegram setup")
    print("[3] Exit\n")
    choice = input("Enter your choice: ")
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter a valid choice.")
        choice = input("Enter your choice: ")

    if choice == "1":
        gmail_setup()
    elif choice == "2":
        telegram_setup()
    elif choice == "3":
        return 0
