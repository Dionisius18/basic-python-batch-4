import smtplib
import imghdr
from email.message import EmailMessage
import config

EMAIL_ADDRESS = "dnisius64@gmail.com"
EMAIL_PASSWORD = "Nisius12."

r_file = open("email.txt", "r")
list_email = []
for line in r_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_email.append(line_list)
r_file.close()

for name in list_email :
    msg = EmailMessage()
    msg['Subject'] = 'Checck out this'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = name
    msg.set_content('Image attached...')

    with open('Gambar1.jpg', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename= file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Email has been sent")
