import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
PORT = 587

my_email = "avanepali@gmail.com"
password = "Anepali1!"
BUY_PRICE = 35

PRODUCT_URL = "https://www.amazon.com/Regalo-39-Inch-6-Inch-Extension-Pressure/dp/B001OC5UMQ/ref=sr_1_2?dchild=1&keywords=safety+gates&qid=1615150570&s=home-garden&sr=1-2"
header ={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
         "accept-language": "en-US,en;q=0.9"
         }

response = requests.get(PRODUCT_URL, headers=header)
result = response.content

soup = BeautifulSoup(result, "lxml")
price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Amazon Price Alert!\n\n The amazon product {PRODUCT_URL} you view is below the {BUY_PRICE}. Buy now. "
        )
