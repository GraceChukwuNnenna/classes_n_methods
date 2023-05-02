#  Create an application that sends a bulk email. This application will run as an executable file. When you run the application, it should open a command prompt immediately.



import smtplib

from email.message import EmailMessage

import ssl  # for faster bulk-mail delivery

# COLLECT USER INFO
Name = input('Name: ')

sender = input('Sender email: ')

recipient = input('Recipient emails : ').split(',')

mypassword = ''

subject = input('Subject: ')

body = input('email body content: ')

# CREATE THE OBJECT OF THE EMAIL CLASS EMAILMESSAGE ;
email_me = EmailMessage()

email_me['Subject'] = subject
email_me['From'] = sender
email_me['To'] = ','.join(recipient)
email_me.set_content(body)

context = ssl.create_default_context()

# OPENNING THE CONNECTION TO GMAIL SERVER AND SEND MESSAGE
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mailme: 
    mailme.login(sender, mypassword)
    mailme.sendmail(sender, recipient, email_me.as_string())
    # mailme.send_message(email_me)

    print('emails sent successfully!')
