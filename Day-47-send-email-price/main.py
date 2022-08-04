import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/dp/B09WVZBWWK/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-price-whole").getText()
price_as_float = float(price.split(".")[0])
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200
YOUR_SMTP_ADDRESS = ""
YOUR_EMAIL = ""
YOUR_PASSWORD = ""
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )