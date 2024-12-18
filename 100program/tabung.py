def tabung():
    print('=============================')
    print('====== GEOMETRI TABUNG ======')
    print('=============================\n')

    j2 = float(input('masukan jari jari : '))
    t = float(input('masukan tinggi : '))
    volume = lambda j2,t : 2 * 3.14 * j2 * t
    luas = lambda j2,t : 3.14 * j2 * j2 + 2 * 3.14 * j2 * t

    print(f'volume : {round (volume(j2,t), 2)} cm3')
    print(f'luas : {round (luas(j2,t), 2)} cm2')

tabung()