print('='*20)
print('HARI KEMARIN')
print('='*20)

hari = input('Masukan nama hari : ')

if hari == 'senin':
    print('Kemarinnya minggu')
elif hari == 'selasa':
    print('Kemarinnya senin')
elif hari == 'rabu':
    print('Kemarinnya selasa')
elif hari == 'kamis':
    print('Kemarinnya rabu')
elif hari == 'jumat':
    print('Kemarinnya kamis')
elif hari == 'sabtu':
    print('Kemarinnya jumat')
elif hari == 'minggu':
    print('Kemarinnya sabtu')
else:
    print('ini bukan nama hari')