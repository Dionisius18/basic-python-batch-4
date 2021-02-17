ujian_teori = int(input('Nilai ujian teori :'))
ujian_praktik = int(input('Nilai ujian praktik :'))
if ujian_teori >= 70 and ujian_praktik >= 70 :
    print('Selamat, Anda Lulus')
elif ujian_teori >= 70 and ujian_praktik <= 70 :
    print('Anda harus mengulang ujian praktik')
elif ujian_teori <= 70 and ujian_praktik >= 70 :
    print('Anda harus mengulang ujian teori')
else :
    print('Anda harus mengulangi ujian teori dan praktik')