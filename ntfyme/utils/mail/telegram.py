import os
import requests
import toml

def send_telegram(results):
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    config_path = os.path.join(package_root, "config.toml")

    with open(config_path, "r") as file:
        details = toml.load(file)

    chat_id =   details["telegram"]["chat_id"]
    token = details["telegram"]["token"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    error = results["error"]
    pid = results["pid"]

    message = f"*PID:* {pid}\n*Command run:* {results['command']}\n*Time taken:* {results['time_taken']} seconds\n"
    message_telegram = f"*Output*:\n{results['output']}\n*Error:* {error}"

    filename = f"output{pid}.txt"
    if len(results["output"]) > 1000:
        with open(filename, "w") as file:
            file.write(message_telegram)
        with open(filename, "r") as file:
            files = {'document': (filename, file)}
            data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
            requests.post(url, json=data)
            requests.post(f"https://api.telegram.org/bot{token}/sendDocument", data={"chat_id": chat_id}, files=files)
            
    else:
        message = message + message_telegram
        data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=data)

    if os.path.exists(filename):
        os.remove(filename)