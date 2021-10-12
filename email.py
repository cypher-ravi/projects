import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'ronnil oreo'
email['to'] = 'benjaminravi2@gmail.com'
email['subject'] = 'you won 1,00,00000 million dollar'

email.set_content('You have been hacked')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('ronniloreo@gmail.com', 'ronniloreo@123')
    server.send_message(email)
    print('all good boss!!')

