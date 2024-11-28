# Fungsi untuk menghitung volume balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# Fungsi untuk menghitung luas permukaan balok
def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Meminta input dari pengguna
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

# Menghitung volume dan luas permukaan
volume = volume_balok(panjang, lebar, tinggi)
luas_permukaan = luas_permukaan_balok(panjang, lebar, tinggi)

# Menampilkan hasil
print(f"Volume balok: {volume}")
print(f"Luas permukaan balok: {luas_permukaan}"