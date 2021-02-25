#name = input("Nama anda : ")
#age = int(input("Umur anda : "))
#costumer = [name, age]
#for i in costumer :
#    print(i)

count = int(input("Berapa data :"))

nama_pelanggan = []
umur_pelanggan = []

for i in range(count):
    print("Data ke {}".format(i+1))
    nama = input("nama anda :")
    umur = int(input("umur anda :"))

    nama_pelanggan.append(nama)
    umur_pelanggan.append(umur)

