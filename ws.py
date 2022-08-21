import requests
from bs4 import BeautifulSoup
import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail, To



URL = "https://www.brasiltronic.com.br/camera-fujifilm-x-t3-mirrorless-preto-somente-o-corpo-p1328375"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('h1', class_='col-12 name no-medium').get_text()
print(title)
price = soup.find('strong', class_="sale-price").get_text().strip()

num_price = price[3:9]
num_price = num_price.replace('.', '')
num_price = float(num_price)

print(num_price)

def send_email():
    
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("contato@codifike.com.br")  # Change to your verified sender
    to_email = To("webscrapper244@gmail.com")  # Change to your recipient
    subject = "Preço Camera Fuji BAIXOU!!!!"
    content = Content("text/plain", "Link do produto https://www.brasiltronic.com.br/camera-fujifilm-x-t3-mirrorless-preto-somente-o-corpo-p1328375")
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
   
    print('Email enviado')

if num_price > 12000:
    send_email()


