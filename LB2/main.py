from http import server
from turtle import color, width
from xhtml2pdf import pisa
from dotenv import dotenv_values
from email.message import EmailMessage
import requests
import json
import smtplib
import yagmail
import os



url = "https://api.chucknorris.io/jokes/random"
response = requests.request("GET", url)


Witz = json.loads(response.content)["value"]


html= f'''
<html>
<head>
<style>
</style> </head>
<body>
<h1>Chuck Norris API</h1>
<p><b>{Witz}</b></p>
<div class="Cloud-img">
    <img src="https://i.ds.at/gHYq0A/rs:fill:750:0/plain/2020/03/09/chuckBreiteKLEINER1200pix.jpg" width="720" height="347"></a>
</div>
'''


pdf_file = open("Chuck Norris.pdf", "w+b")
pisa.CreatePDF(html, dest=pdf_file)
pdf_file.close()


dotenv = dotenv_values(".env")

user = dotenv.get("Email_Sendfrom")
passcodeGmail = dotenv.get("Email_Passcode")
to = "marzio@hispeed.ch"


with yagmail.SMTP(user, passcodeGmail) as yag:
    yag.send(to, "Chuck Norris", "Here's a joke:", "Chuck Norris.pdf")

