import smtplib
import time
from email.message import EmailMessage
import ssl

# Email account credentials and details
# It's recommended to use environment variables for security
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password" # Use the app password, not regular password
RECEIVER_EMAIL = "recipient_email@example.com"
SUBJECT = "Test Email in Infinite Loop"
BODY = "This is an automated email sent from a Python script in an infinite loop."

# SMTP server details for Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587 # Port 587 for TLS

def send_automated_email():
    """Sends a single email using SMTP."""
    # Create the email message
    msg = EmailMessage()
    msg.set_content(BODY)
    msg['Subject'] = SUBJECT   
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context) # Secure the connection with TLS
            server.login(SENDER_EMAIL, SENDER_PASSWORD) # Log in
            server.send_message(msg)
            print(f"Email sent successfully at {time.ctime()}!")
    except Exception as e:
        print(f"Error sending email: {e}")

print("Starting infinite email loop...")

# The infinite loop
while True:
    send_automated_email()
    # Wait for 60 seconds before sending the next email
    time.sleep(60)