import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_="aok-offscreen").get_text()

price_without_sign = price.split("$")[1]

float_price = float(price_without_sign)

title = soup.find(class_="a-size-large product-title-word-break").get_text()

BUY_PRICE = 100

if float_price < BUY_PRICE:
    message = f"{title} is now ${price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )


