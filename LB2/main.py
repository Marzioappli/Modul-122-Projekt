from http import server
from xhtml2pdf import pisa
import requests
import json
import smtplib

import os
from email.message import EmailMessage

url = "https://api.chucknorris.io/jokes/random"
response = requests.request("GET", url)


Witz = json.loads(response.content)["value"]
print(Witz)


html= f'''
<html>
<body>
<h1>Chuck Norris API</h1>
<p>{Witz}</p>
'''

pdf_file = open("Chuck Norris.pdf", "w+b")
pisa.CreatePDF(html, dest=pdf_file)
pdf_file.close()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('lb2.chucknorris@gmail.com', 'kvwjfstqoczbehso')
server.sendmail('lb2.chucknorris@gmail.com', 'marzio@hispeed.ch', 'Mail automatisiert versendet')
print('Mail wurde erfolgreich versendet')

