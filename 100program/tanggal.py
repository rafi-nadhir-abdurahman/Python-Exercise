print('='*20)
print('PROGRAM TANGGAL')
print('='*20)

bulan = int(input('masukan nomor bulan : '))

if bulan == 1:
    print('JANUARI')
    print('ada 30 hari')
elif bulan == 2:
    print('FEBUARI')
    print('ada 28 atau 29 hari')
elif bulan == 3:
    print('MARET')
    print('ada 31 hari')
elif bulan == 4:
    print('APRIL')
    print('ada 30 hari')
elif bulan == 5:
    print('MEI')
    print('ada 31 hari')
elif bulan == 6:
    print('JUNI')
    print('ada 30 hari')
elif bulan == 7:
    print('JULI')
    print('ada 31 hari')
elif bulan == 8:
    print('AGUSTUS')
    print('ada 31 hari')
elif bulan == 9:
    print('SEPTEMBER')
    print('ada 30 hari')
elif bulan == 10:
    print('OKTOBER')
    print('ada 31 hari')
elif bulan == 11:
    print('NOVEMBER')
    print('ada 30 hari')
elif bulan == 12:
    print('DESEMBER')
    print('ada 31 hari')
else:
    print('bulan tidak valid')