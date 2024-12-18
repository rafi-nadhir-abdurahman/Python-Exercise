print(30*"=")
print("MENENTUKAN DISKON BELANJA")
print(30*"=")

br1 = input('\033[33mMasukan harga barang 1: Rp. ')
br2 = input('\033[33mMasukan harga barang 2: Rp. ')
br3 = input('\033[33mMasukan harga barang 3: Rp. ')
br4 = input('\033[33mMasukan harga barang 4: Rp. ')

diskon = float(7.5)/int(100)

total = int(br1)+int(br2)+int(br3)+int(br4)
diskon = int(total)*diskon
diskon2 = int(total)-int(diskon)

print(f'\n\033[37mTotal Belanja: Rp. {total}')

if total >= 100000:
    print(f'\n\033[0,31mDiskon: Rp. {diskon}')
    print(f'Total Bayar: Rp. {diskon2}')

elif total <= 100000:
    print(f'\033[0,35mTotal Bayar: Rp. {total}')