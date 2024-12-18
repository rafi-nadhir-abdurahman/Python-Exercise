def bola():
    print('==============================')
    print('============ BOLA ============')
    print('==============================')

    PHI = 3.14
    r = int(input('Masukan jari jari bola\t: '))
    l = lambda PHI,r : 4 * PHI * r**2
    v = lambda PHI,r : (4 / 3) * PHI * r**3

    print(f'Luas\t: {l(PHI,r)}')
    print(f'Volume\t: {round(v(PHI,r),2)}')

bola()