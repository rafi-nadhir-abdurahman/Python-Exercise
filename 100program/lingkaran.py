def lingkaran():
    print('=============================')
    print('===== PROGRAM LINGKARAN =====')
    print('=============================\n')


    r = float(input('Masukan jari-jari : '))
    luas = lambda r : 3.14 * r * r
    keliling = lambda r : 2 * 3.14 * r

    print(f'luas : {luas(r)} cm2')
    print(f'Keliling : {keliling(r)} cm2\n')

lingkaran()