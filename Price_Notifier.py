import requests
import smtplib
from bs4 import BeautifulSoup
import time

URL = 'https://www.amazon.in/Sony-WF-XB700-Wireless-Bluetooth-Headphones/dp/B085VQFZ8Z/ref=sr_1_12?dchild=1&keywords=sony+headphones+original+bluetooth&qid=1596400066&s=electronics&sr=1-12'
#URL should be of the amazon page of the product whose price we want to be notified should it drop
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

def check_price():
    page=requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()

    price=soup.find(id="priceblock_ourprice").get_text()

    con=price[2]+price[4:7]
    actual_price=(int)(con)
    
    #print(actual_price)
    desired_price=5000
    if(actual_price<desired_price):
        notify()


def notify():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('xyz@gmail.com','password')
    

    subject='Price Fell Down'
    body='CHECK https://www.amazon.in/Sony-WF-XB700-Wireless-Bluetooth-Headphones/dp/B085VQFZ8Z/ref=sr_1_12?dchild=1&keywords=sony+headphones+original+bluetooth&qid=1596400066&s=electronics&sr=1-12'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'the_emailid_from_which_we_send_the_mail.com',
        'the_emailid_to_which_we_send_the_mail.com',
        msg
    )

    print("EMAIL'S BEEN SENT")
    server.quit()

while(True):
    check_price()
    time.sleep(60*60*2)
    #Now it would run in the background and check the price every 2 hours
