import importlib.util
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import toml


def send_gmail(results, key):
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

    config_path = os.path.join(package_root, "config.toml")
    encrypt_path = os.path.join(package_root, "manager", "encrypt.py")

    spec = importlib.util.spec_from_file_location("decrypt", encrypt_path)
    decrypt_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(decrypt_module)

    with open(config_path, "r") as file:
        details = toml.load(file)

    mail_id = details["mail"]["mail_id"]
    encrypted_password = details["mail"]["password"]
    pid = results["pid"]
    error = results["error"]

    password = decrypt_module.decrypt(encrypted_password, key)

    if mail_id.endswith("@gmail.com"):

        message = f"""
                        <html>
                        <body>
                        <p><b>ntfyme :: Diagnostics </b></p>
                        <p><b>Pid:</b> {pid}</p>
                        <p><b>command run:</b> {results['command']}</p>
                        <p><b>Time taken:</b> {results['time_taken']} seconds</p>
                        </body>
                        </html>
                        """
        message1 = f"""
                            <html>
                            <body>
                            <p><b>Output:</b> {results["output"]}</p>
                            <p><b>Error:</b> {results["error"]}</p>
                            </body>
                            </html>
                            """
        filename = f"output{pid}.txt"
        message_mail = f"""
        Output:\n{results["output"]}\n
        Error:\n{results["error"]}
        """
        if len(results["output"]) > 1000:
            with open(filename, "w") as f:
                f.write(message_mail)
            with open(filename) as f:
                attachment = MIMEText(f.read())
                attachment.add_header(
                    "Content-Disposition", "attachment", filename=filename
                )
        else:
            message = message + message1
        # bold_text = "\033[1mThis text is bold!\033[0m"
        msg = MIMEMultipart()
        msg["From"] = msg["To"] = mail_id
        success_sub = details["ntfyme"]["success_subject"]
        error_sub = details["ntfyme"]["error_subject"]
        msg["Subject"] = (
            f"ntfyme :: {success_sub}" if error == "none" else f"ntfyme :: {error_sub}"
        )

        msg.attach(MIMEText(message, "html"))
        if len(results["output"]) > 1000:
            msg.attach(attachment)
        server = smtplib.SMTP("smtp.gmail.com: 587")
        server.starttls()
        server.login(msg["From"], password)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()

        # remove the file after sending the mail
        if os.path.exists(filename):
            os.remove(filename)
