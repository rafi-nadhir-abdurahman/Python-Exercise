print('='*40)
print('KONVERSI PECAHAN KE DESIMAL')
print('='*40)

pembilang = int(input("Masukkan pembilang : "))
penyebut = int(input("Masukkan penyebut : "))

if penyebut == 0:
    print("Tidak dapat membagi dengan nol")
else:
    rumus =  pembilang / penyebut

print(f"Hasil konversi : {rumus}")