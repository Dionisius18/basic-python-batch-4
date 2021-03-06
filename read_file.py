r = open("hello.txt","r")

print(r.read())

temp2 = r.readlines()

a = []
for li in temp2:
    a.append(li.strip())

print(a)
r.close()