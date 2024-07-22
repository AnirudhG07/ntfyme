import importlib.util
import os
import smtplib

import toml


def send_gmail(result):
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

    config_path = os.path.join(package_root, "config.toml")
    encrypt_path = os.path.join(package_root, "manager", "encrypt.py")

    spec = importlib.util.spec_from_file_location("decrypt", encrypt_path)
    encrypt_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(encrypt_module)

    with open(config_path, "r") as file:
        details = toml.load(file)

    mail_id = details["mail"]["mail_id"]
    password = details["mail"]["password"]

    if mail_id.endswith("@gmail.com"):
        EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
        EMAIL_USE_TLS = True
        EMAIL_HOST = "smtp.gmail.com"
        EMAIL_PORT = 587

        EMAIL_HOST_USER = RECIEVER_S_MAIL_ID = mail_id
        EMAIL_HOST_PASSWORD = password
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD)

        connection.sendmail(
            from_addr=EMAIL_HOST_USER,
            to_addrs=RECIEVER_S_MAIL_ID,
            msg=f"Subject:Hello\n\n Output: {result['output']}\nCommand run: {result['command']}\nTime taken: {result['time_taken']} seconds\nPID: {result['pid']}\nError: {result['error']}",
        )
        connection.close()
