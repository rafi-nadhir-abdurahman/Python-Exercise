print('===========================')
print('====== RESTOK BARANG ======')
print('===========================')

jumlahBarang = int(input('masukan jumlah barang: '))

if int(jumlahBarang) >= 50:
    print('barang boleh di jual belikan')
elif int(jumlahBarang) <= 10:
    print('barang harus di restok')
else:
    print('barang tidak boleh di perjual belikan')