def daftar_menu() :
    print("Selamat datang!")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def pilih_menu() :
    daftar_menu()
    pilihan = int(input("Pilih menu: "))

daftar_kontak = []

def print_daftar_kontak () :
    for kontak in daftar_kontak :
        print(kontak)

def tambah_daftar_kontak() :
    nama = input('nama :')
    nomor = input('nomor :')
    daftar_kontak.append(nama)
    daftar_kontak.append(nomor)

while pilih_menu(pilihan) <= 3 :
    if pilihan == 1 :
        print_daftar_kontak ()
        pilih_menu()
    elif pilihan == 2 :
        tambah_daftar_kontak()
        pilih_menu()
    elif pilihan == 3 :
        print("program selesai, sampai jumpa!")
        pilih_menu()
    else :
        print("menu tidak tersedia")
        pilih_menu()

