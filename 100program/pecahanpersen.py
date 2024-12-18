print('='*40)
print('KONVERSI PECAHAN KE PERSEN')
print('='*40)

pembilang = int(input("Masukkan pembilang : "))
penyebut = int(input("Masukkan penyebu t: "))

if penyebut == 0:
    print("Tidak dapat membagi dengan nol")
else:
    rumus = (pembilang / penyebut) * 100

print(f"Hasil konversi : {rumus}%")