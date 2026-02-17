while True:
    print("Sending email...")
import smtplib
import time
from email.mime.text import MIMEText

EMAIL = MaxNuthall@outlook.com
PASSWORD = MaxTigris2010

def send_email():
    msg = MIMEText ("Test message")
    msg["Subject"] = "loopemail"
    msg["From"] = "MaxNuthall@outlook.com"
    msg["To"] = "ispammyfreindalotqwertyq"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

while True:
    send_email()
    print("Email sent!")
    time.sleep(60)  # waits 60 seconds before next email
for i in range(10):  # sends only 10 emails
    send_email(1)
    time.sleep(60)
