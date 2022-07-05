from http import server
from turtle import width
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


dotenv = dotenv_values(".env")

user = dotenv.get("Email_Sendfrom")
passcodeGmail = "kvwjfstqoczbehso"
to = "y.kuenzler@icloud.com"


with yagmail.SMTP(user, passcodeGmail) as yag:
    yag.send(to, "Chuck Norris", "Here's a joke:", "Chuck Norris.pdf")

