import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


mailserver = smtplib.SMTP('smtp.gmail.com', 25)  #creating a mailserver

mailserver.ehlo() # start the process

with open('pw.txt', 'r') as fl :          #read the password from the file
    password = fl.read()

mailserver.login('spam@fake.com', password)  # create a fake mail account which will be used for sending spam mails

message = MIMEMultipart()
message['From'] = 'spam.fake@sender.com'   #sender mail id from where the spams will be send
message['To'] = 'spam.received@receiver.com'  # you can use list of targeted email-ids
message['Subject'] = 'win exciting prizes'

with open('message.txt', 'r') as f :   #message body
    msg = f.read()

message.attach(MIMEText(msg, 'plain'))

filename = 'Winner.jpg'
attachment = open(filename, 'rb')    #open the image file as bytes

payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attachment.read())           

encoders.encode_base64(payload)
payload.add_header('Content-Disposition', f'attachment; filename={filename}')
message.attach(payload)


textmessage = message.as_string()                      # convert the message into string before sending
mailserver.sendmail('spam.fake@sender.com', 'spam.received@receiver.com', textmessage )

