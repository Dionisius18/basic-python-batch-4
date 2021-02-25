nama_buah = []

def tambah_nama_buah(nama) :
    nama_buah.append(nama)
    print_nama_buah()

def print_nama_buah () :
    for buah in nama_buah :
        print(buah)
    print('------')

tambah_nama_buah("Jeruk")
tambah_nama_buah("apel")
tambah_nama_buah("durian")
