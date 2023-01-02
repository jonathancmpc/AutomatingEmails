import yagmail
import os
import pandas

sender = os.getenv('email') #Emails.my_email

subject = 'Ultilizando CSV'

#dataframe
df = pandas.read_csv('6_AutomatingEmails/emails/contacts.csv', delimiter=";")

yag = yagmail.SMTP(user=sender, password=os.getenv('password'))

for index, row in df.iterrows():
  contents = f"""
    <p>Esse é o conteúdo do e-mail.</p>
    <b>Olá {row['name']}, como você está? </b>
  """
  yag.send(to=row['email'], subject=subject, contents=contents)
  print('Email Sent!!')