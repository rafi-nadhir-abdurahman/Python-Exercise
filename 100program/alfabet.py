print('*'*30)
print('\tPROGRAM HURUF')
print('*'*30)

huruf = input('masukan huruf alfabet (a-z): ')


if huruf in 'aiueo':
    print('huruf ini termasuk kedalam huruf vokal')
elif huruf.isdigit():
    print('ini bukan huruf')
else:
    print('huruf ini termasuk kedalam huruf konsonan')