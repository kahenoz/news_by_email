import smtplib, ssl
import os

host = "smtp.gmail.com"
port = 465

username = "kahenozturk@gmail.com"
password = os.getenv("APP_PASSWORD")

receiver = "kahenozturk@gmail.com"
context = ssl.create_default_context()

message = """
Hi!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)



