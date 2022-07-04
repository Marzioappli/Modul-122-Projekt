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

server = smtplib.SMTP('smtp.outlook.com', 587)
server.starttls()
server.login('LB2.ChuckNorris@outlook.com', 'Gczürich*10')
server.sendmail('LB2.ChuckNorris@outlook.com', 'marzio.cassese@edu.tbz.ch', 'Mail automatisiert versendet')
print('Mail wurde erfolgreich versendet')

