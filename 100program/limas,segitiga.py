def limasSegitiga():
    print('==============================')
    print('======= LIMAS SEGITIGA =======')
    print('==============================')

    la = float(input('Masukan luas alas limas : '))
    t = float(input('Masukan tinggi limas : '))
    st = float(input('Masukan luas sisi tegak limas : '))

    lp = lambda la,st : la + st
    v = lambda la,t : 1 / 3 * la * t

    print(f'Volume\t: {v(la,t)}')
    print(f'Luas Permukaan\t: {lp(la,st)}')

limasSegitiga()