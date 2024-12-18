def persegi():
    print('=============================')
    print('====== PROGRAM PERSEGI ======')
    print('=============================\n')


    s = int(input('Masukan sisi : '))
    luas = lambda s : s * s
    keliling = lambda s : 4 * s

    print(f'luas : {luas(s)} cm2')
    print(f'Keliling : {keliling(s)} cm2\n')

persegi()