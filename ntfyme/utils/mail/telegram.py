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
    message = f"*PID:* {result['pid']}\n*Command run:* {result['command']}\n*Time taken:* {result['time_taken']} seconds\n*Output*:\n{result['output']}\n*Error:* {result['error']}"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=data)
#     requests.get(url).json()




# message = f"This is a message with *_bold_* and _italic_ text."

# # Send the message using the Telegram Bot API endpoint
# url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
# data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
# response = requests.post(url, json=data)
