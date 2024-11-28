def segitiga():
    print('==============================')
    print('====== PROGRAM SEGITIGA ======')
    print('==============================\n')


    t = float(input('Masukan tinggi : '))
    a = float(input('Masukan alas : '))
    luas = lambda a,t : 0.5 * (a * t)
    keliling = lambda a : a * a * a

    print(f'luas : {luas(a,t)} cm2')
    print(f'Keliling : {keliling(a)} cm2\n')

segitiga()