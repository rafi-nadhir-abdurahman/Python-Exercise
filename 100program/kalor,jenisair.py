print('='*35)
print("KALOR JENIS AIR")
print('='*35)

m = float(input("masukan massa = "))
c = 4.18
suhu_awal = float(input("masukan suhu awal = "))
suhu_akhir = float(input("masukan suhu akhir = "))
t = suhu_awal - suhu_akhir
q3 = m * c * t

print(f"jumlah kalor yang diperlukan adalah = {q3}")