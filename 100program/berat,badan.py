print('='*30)
print('Menentukan berat badan ideal')
print('='*30)

tinggi_badan = float(input('Masukan tinggi badan dengan satuan cm : '))
berat_badan = float(input('Masukan berat badan dengan satuan cm : '))

operasi1 = tinggi_badan - 100
berat_ideal = operasi1 - 0.1

print('Berat badan ideal anda adalah : ', round(berat_ideal, 1), 'kg')

if (berat_ideal-2) <= berat_badan <= (berat_ideal+2) :
    print('Berat badan ideal')
else :
    print('Berat badan tidak ideal')