import os
import requests
import toml

def send_telegram(result):
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    config_path = os.path.join(package_root, "config.toml")

    with open(config_path, "r") as file:
        info = toml.load(file)

    chat_id = info["telegram"]["chat_id"]
    token = info["telegram"]["token"]
    message = f"Output: {result['output']}\nCommand run: {result['command']}\nTime taken: {result['time_taken']} seconds\nPID: {result['pid']}\nError: {result['error']}"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
