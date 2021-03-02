#https://www.kite.com/python/answers/how-to-convert-each-line-in-a-text-file-into-a-list-in-python

r_file = open("email.txt", "r")
list_email = []
for line in r_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_email.append(line_list)
r_file.close()

EMAIL_ADDRESS = "dnisius64@gmail.com"
PASSWORD ="Nisius12."
EMAIL_REC = list_email