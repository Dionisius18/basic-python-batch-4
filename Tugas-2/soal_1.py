def daftar_menu() :
    print("Selamat datang!")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

daftar_kontak = []

def print_daftar_kontak () :
    for kontak in daftar_kontak :
        print(kontak)

def tambah_daftar_kontak() :
    nama = input('nama :')
    nomor = input('nomor :')
    daftar_kontak.append(nama)
    daftar_kontak.append(nomor)
daftar_menu()
pilihan = int(input("Pilih menu: "))
while pilihan <= 3 :
    if pilihan == 1 :
        print_daftar_kontak ()
        daftar_menu()
        pilihan = int(input("Pilih menu: "))
    elif pilihan == 2 :
        tambah_daftar_kontak()
        daftar_menu()
        pilihan = int(input("Pilih menu: "))
    elif pilihan == 3 :
        print("program selesai, sampai jumpa!")
        break
    else :
        print("menu tidak tersedia")
        daftar_menu()
        pilihan = int(input("Pilih menu: "))
