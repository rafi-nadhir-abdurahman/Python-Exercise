
def persegiPanjang():
    print('===============================')
    print('======= PERSEGI PANJANG =======')
    print('===============================')

    p = float(input('Masukan panjangnya : '))
    l = float(input('Masukan lebarnya : '))

    rl = lambda p,l : p * l
    rk = lambda p,l : 2 * (p * l)

    print(f'Luas\t\t: {rl(p,l)}')
    print(f'Keliling\t: {rk(p,l)}')

persegiPanjang()