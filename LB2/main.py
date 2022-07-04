from xhtml2pdf import pisa
import requests
import json
import smtplib

url = "https://api.chucknorris.io/jokes/random"
response = requests.request("GET", url)


joke = json.loads(response.content)["value"]
print(joke)


html= f'''
<html>
<body>
<h1>Chuck Norris API</h1>
<p>{joke}</p>
'''

pdf_file = open("Chuck Norris.pdf", "w+b")
pisa.CreatePDF(html, dest=pdf_file)
pdf_file.close()

schicken = smtplib.SMTP('smtp.outlook.com', 587)