import yagmail
import os

sender = os.getenv('email') #Emails.my_email
#e-mail temporário criado em https://dropmail.me/pt/
receiver = 'taarztiee@emlpro.com'

subject = 'Esse é o título'

contents = ["""
  <p>Esse é o conteúdo do e-mail.</p>
  <b>Olá!! Hello!! I love You ❤❤❤❤</b>
""", 'image.jpg']

yag = yagmail.SMTP(user=sender, password=os.getenv('password'))
yag.send(to=receiver, subject=subject, contents=contents)
print('Email Sent!!')