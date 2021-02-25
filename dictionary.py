pelanggan = { "nama" : "Astuti", "umur" : 20}
#print(type(pelanggan))

pelanggan_2 = {"nama" : "joko", "umur" : 23}
print("nama : {}".format(pelanggan["nama"]))
print("umur : {}".format(pelanggan["umur"]))

#change value of dictionary
pelanggan["umur"] = 25

print(pelanggan)

#loop through dict
for x in pelanggan:
    print(x)
    print(pelanggan[x])
    print(pelanggan_2[x])

daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

print(daftar_pelanggan)

for pelanggan in daftar_pelanggan :
    print("nama : {}".format(pelanggan["nama"]))
    print("umur : {}".format(pelanggan["umur"]))
