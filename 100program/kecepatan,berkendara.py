print("="*40)
print("PROGRAM MENGHITUNG KECEPATAN KENDARAAN")
print("="*40)


try:
    jarak = int(input("masukan jarak berkendara (m) = "))
    waktu = int(input("masukan waktu berkendara (s) = "))
    kecepatan = jarak / waktu
    print(f"kecepatan kendaraan anda adalah = {kecepatan:.2f} m/s")

except ValueError:
    print("inputan anda tidak valid")
    print("silahka masukan y/t saja")