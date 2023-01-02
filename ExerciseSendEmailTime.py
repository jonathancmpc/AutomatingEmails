import yagmail
import os
import time
from datetime import datetime

sender = os.getenv('email') #Emails.my_email
#e-mail temporário criado em https://dropmail.me/pt/
receiver = 'taarztiee@emlpro.com'


subject = 'A cada minuto'

while True:
  now = datetime.now()
  dt_str = now.strftime("%H:%M:%S")
  contents = """
    <p>Esse é o conteúdo do e-mail.</p>
    <b>Olá!! Hello!! Esse e-mail foi enviado as """ + dt_str + "</b>"
  
  yag = yagmail.SMTP(user=sender, password=os.getenv('password'))
  yag.send(to=receiver, subject=subject, contents=contents)
  print('Email Sent!!')
  time.sleep(60)