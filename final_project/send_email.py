import smtplib

fromaddr = "dnisius64@gmail.com"
toaddr = "dionisius.w98@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "JUDUL PESAN"
 
body = "ISI PESAN"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Nisius12.")
print("login sukses")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("email terkirim")
server.quit()