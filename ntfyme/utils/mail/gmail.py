import smtplib
import toml
import os

def send_gmail(result):
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, '..'))
    config_path = os.path.join(package_root, 'config.toml')

    with open(config_path, 'r') as file:

        data = toml.load(file)
    
    
    if data['mail']['mail_id'].endswith("@gmail.com"):
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

        EMAIL_USE_TLS = True

        EMAIL_HOST = 'smtp.gmail.com'

        EMAIL_PORT = 587

        EMAIL_HOST_USER = data['mail']['mail_id']

        EMAIL_HOST_PASSWORD = data['mail']['password']
        connection = smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD)
        connection.sendmail(from_addr=  EMAIL_HOST_USER, 
                            to_addrs="anirudhgupta.ani0711@gmail.com",
                            msg=f"Subject:Hello\n\n Output: {result['output']}\nCommand run: {result['command']}\nTime taken: {result['time_taken']} seconds\nPID: {result['pid']}\nError: {result['error']}")    
        connection.close()

