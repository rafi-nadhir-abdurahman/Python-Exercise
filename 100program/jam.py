print('='*30)
print('PROGRAM DETEKSI WAKTU')
print('='*30)

jam = int(input('Sekarang jam berapa : '))

if jam >= 4 and jam <= 10:
    print('-----selamat pagi bosku-----')
elif jam >= 11 and jam <= 14:
    print('-----selamat siang bosku-----')
elif jam >= 15 and jam <= 17:
    print('-----selamat sore bosku-----')
elif jam == 18:
    print('-----magrib bosku-----')
elif jam >= 19 and jam <= 24:
    print('-----selamat malam bosku-----')
elif jam >= 1 and jam <= 3:
    print('-----tidur bosku-----')
else:
    print('-----pesan error-----')