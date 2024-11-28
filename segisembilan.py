def segiSembilan():
    print('================================')
    print('==== KELILING SEGI SEMBILAN ====')
    print('================================')

    s = int(input('Masukan panjang sisi nya : '))
    l = lambda s : 9 * s

    print(f'keliling : {l(s)}')

segiSembilan(