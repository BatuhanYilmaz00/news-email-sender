
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
url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-10-18&sortBy=publishedAt&apiKey={api_key}&language=en"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
#print(content["articles"])
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body =("Subject: Today's news" + "\n" +
               body + article["title"] + "\n" +
               article["description"] + "\n"+
               article["url"]  + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)
