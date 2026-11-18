from email.mime.multipart import MIMEMultipart

import requests
#requests library used for API

import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    sender_email = "user@gmail.com"
    sender_email_password = "your_gmail_app_password"

    receiver_email = "user@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, sender_email_password)
        server.sendmail(sender_email, receiver_email, message)



api_key = "......"
url = "......"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
#print(content["articles"])
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
