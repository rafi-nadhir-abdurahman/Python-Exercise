# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 05/11/2024
# program tahun kabisat

print(30*"=")
print("PROGRAM MENGHITUNG TAHUN KABISAT")
print(30*"=")

def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

tahun_input = int(input("Masukkan tahun: "))

tahun_sekarang = 2024

jumlah_kabisat = 0
for tahun in range(tahun_input, tahun_sekarang + 1):
    if is_kabisat(tahun):
        jumlah_kabisat += 1

print(f"Dari tahun {tahun_input} hingga {tahun_sekarang}, terdapat {jumlah_kabisat} tahun kabisat.")