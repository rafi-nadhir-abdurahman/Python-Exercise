def balok():
    print('===============================')
    print('============ BALOK ============')
    print('===============================')

    p = int(input('Masukan panjang balok : '))
    l = int(input('Masukan lebar balok : '))
    t = int(input('Masukan tinggi balok : '))

    lp = lambda p,l,t : 2 * ((p * l) + (p * t) + (l * t))
    v = lambda p,l,t : p * l * t
    k = lambda p,l,t : 4 * (p + l + t)

    print(f'Luas Permukaan\t: {lp(p,l,t)}')
    print(f'Volume\t\t: {v(p,l,t)}')
    print(f'Keliling\t: {k(p,l,t)}')

balok()