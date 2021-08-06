import smtplib
from email.message import EmailMessage

with open('database.csv', 'r') as StudentList:
    user = StudentList.read()
    user_list = user.split()
    new_user = user_list[-1]
    formatted_new_user = new_user.split()

email = EmailMessage()

email['from'] = 'ronnil oreo'
email['to'] = 'aprcompany369@gmail.com'
email['subject'] = 'New customer fill up the form'

email.set_content(new_user)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('ronniloreo@gmail.com', 'ronniloreo@123')
    server.send_message(email)
    print('all good boss!!')
