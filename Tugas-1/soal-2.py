r = int(input("jari-jari lingkaran :"))
pi = 22/7
luas_lingkaran = pi * (r**2)
float_luas = '{:05.2f}'.format(luas_lingkaran)
print("Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2".format(r,float_luas))