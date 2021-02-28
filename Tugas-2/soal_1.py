def daftar_menu() :
    print("Selamat datang!")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

daftar_kontak = []

def print_daftar_kontak () :
    for kontak in daftar_kontak :
        print("nama : {}".format(kontak["nama"]))
        print("nomor HP: {}".format(kontak["nomor"]))

def tambah_daftar_kontak (nama, nomor) :
    kontak_baru = {"nama" : nama, "nomor": nomor}
    daftar_kontak.append(kontak_baru)

daftar_menu()
pilihan = int(input("Pilih menu: "))

while True :
    if pilihan == 1 :
        print_daftar_kontak ()
        daftar_menu()
        pilihan = int(input("Pilih menu: "))
    elif pilihan == 2 :
        nama = input('nama :')
        nomor = input('nomor :')
        tambah_daftar_kontak(nama, nomor)
        print("Kontak berhasil")
        daftar_menu()
        pilihan = int(input("Pilih menu: "))
    elif pilihan == 3 :
        print("program selesai, sampai jumpa!")
        break
    else :
        print("menu tidak tersedia")
        daftar_menu()
        pilihan = int(input("Pilih menu: "))
