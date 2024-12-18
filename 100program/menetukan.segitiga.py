print('='*20)
print('SEGITIGA')
print('='*20)

a = int(input('masukan sisi pertama : '))
b = int(input('masukan sisi kedua : '))
c = int(input('masukan sisi ketiga : '))

if a**2 + b**2 == c**2:
    print('ini termasuk kedalam segitiga siku siku')
elif a**2 + b**2 > c**2:
    print('ini termasuk kedalam segitiga lancip')
elif a**2 + b**2 < c**2:
    print('ini termasuk kedalam segitiga tumpul')
else:
    print('ini bukan segitiga')