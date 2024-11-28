import time
import os

print(10*"=")
print("STOPWATCH")
print(10*"=")

waktu = int(input("Masukkan waktu dalam hitungan detik : "))

for x in range(waktu, 0, -1):
    detik = x % 60
    menit = int(x / 60) % 60
    jam = int(x / 3600)
    os.system('cls')
    print(f"{jam:02}:{menit:02}:{detik:02}")
    time.sleep(1)

print("WAKTUNYA HABIS!")