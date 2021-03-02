import smtplib
import config

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

subject = "Praktek"
msg = "Hallo"

send_email(subject, msg)

https://www.youtube.com/watch?v=mP_Ln-Z9-XY