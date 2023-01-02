import yagmail
import os
import pandas

sender = os.getenv('email') #Emails.my_email

subject = 'Proof of payment'

yag = yagmail.SMTP(user=sender, password=os.getenv('password'))

df = pandas.read_csv('6_AutomatingEmails/emails/payments.csv')

for index, row in df.iterrows():
  name_attach = row['filepath'].split('.')[0].split('-')[0]
  name_upper = name_attach[0:1].upper() + name_attach[1:]

  contents = [f"""
    Hey, {row['name']} you have to pay {row['amount']}
    {name_upper} is attached!
  """, f"6_AutomatingEmails/Attachments/{row['filepath']}"]

  yag.send(to=row['email'], subject=subject, contents=contents)
  print('Email Sent!!')