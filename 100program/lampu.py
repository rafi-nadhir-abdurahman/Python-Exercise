def lampu():
    print('======================================')
    print('========== LAMPU LALU LINTAS =========')
    print('======================================')

    warna = input('Masukan warana lampu lalu lintas : ').lower()

    if warna == 'merah':
        print('silahkan berhenti')
    elif warna == 'kuning':
        print('berhati hati')
    elif warna == 'hijau':
        print('silahkan maju')
    else:
        print('ini bukan warna lampu lalu lintas')