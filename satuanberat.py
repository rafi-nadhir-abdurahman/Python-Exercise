print('='*30)
print('KONVERSI SATUAN BERAT')
print('='*30)

berat = float(input('Masukan berat badan anda : '))
satuan = input('kilogram atau pound (k atau p) : ').lower()

if satuan == 'k':
    berat = berat * 2.205
    satuan = 'kg'
    print(f'berat kamu adalah : {berat} {satuan}.')
elif satuan == 'p':
    berat = berat / 2.205
    satuan = 'lbs'
    print(f'berat kamu adalah : {berat} {satuan}.')
else:
    print(f'{satuan} tidak valid'