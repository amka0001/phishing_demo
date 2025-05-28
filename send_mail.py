import smtplib
from email.message import EmailMessage

text_content = f"""
Additional account compromises
"""

with open("templates/produkt.html", "r", encoding="utf-8") as f:
    html_content = f.read()

msg = EmailMessage()
msg['Subject'] = 'Additional account compromises'
msg['From'] = 'Noah Rodriguez - Internal IT-Department | noah.rodriguez@greenanimalsbank.com <noahrodriguezzz@protonmail.com>'
msg['To'] = 'Phillip Price <phillip.price@greenanimalsbank.dk>'

msg.set_content(text_content)
msg.add_alternative(html_content, subtype='html')


SMTP_SERVER = 'sandbox.smtp.mailtrap.io'
SMTP_PORT = 2525
USERNAME = '9fa06f1fa4d7ae'
PASSWORD = 'b8dbb4f59a48df'

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.login(USERNAME, PASSWORD)
    server.send_message(msg)

print("Mail sendt!")
