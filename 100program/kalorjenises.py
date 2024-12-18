print('='*35)
print("KALOR JENIS ES")
print('='*35)

m = float(input("masukan massa es = "))
suhu_awal = float(input("masukan suhu awal = "))
suhu_akhir = float(input("masukan suhu akhir = "))
kalor_jenis_es = 2.1
t = suhu_awal - suhu_akhir
q1 = m * kalor_jenis_es * t
print(f"julmah kalor yang diperlukan adalah {q1}")