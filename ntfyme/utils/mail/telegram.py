import os

import requests
import toml

# USER_NAME = "https://t.me/notify_cli_bot"
TOKEN = "YOUR BOT TOKEN"


def send_telegram(result):
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, ".."))
    config_path = os.path.join(package_root, "config.toml")

    with open(config_path, "r") as file:

        data = toml.load(file)

    chat_id = data["telegram"]["chat_id"]
    message = f"Output: {result['output']}\nCommand run: {result['command']}\nTime taken: {result['time_taken']} seconds\nPID: {result['pid']}\nError: {result['error']}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
