#merupakan library python untuk mengakses email
import smtplib

sender_mail = "dnisius64@gmail.com"
password = input(str("masukan password anda : "))
rec_mail = "dionisius.w98@gmail.com"
subject = "Pesan"
pesan = "Hello"

#masuk ke dalam server smtp sesuai dengan domain dan portnya
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(sender_mail, password)
print("Login berhasil")
server.sendmail(sender_mail, rec_mail, subject, pesan)
print("email terikirim")