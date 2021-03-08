#https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975

import smtplib
import config
import imghdr
from email.message import EmailMessage

with open('Gambar1.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)

def send_email(subject, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        print("login succes")
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_REC, message)
        server.quit()
        print("Email sent")
    except:
        print("Email failed to send!")

subject = input(str("Masukan Subject : "))
msg = input(str("Masukan pesan : "))

send_email(subject, msg)

#https://www.youtube.com/watch?v=mP_Ln-Z9-XY