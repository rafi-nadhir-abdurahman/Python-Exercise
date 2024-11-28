import os

def luas_segitiga():
    print ("Hitung luas segitiga ready!")
    a = float(input("Masukan alas: "))
    t = float(input("Masukan tinggi: "))
    luas = lambda t : 0.5 * (a * t)
    print ("luas segitiga: ", luas(t), "\n")

def luas_balok():
    print ("Hitung luas balok ready!")
    p = float(input("Masukan panjang: "))
    l = float(input("Masukan lebar: "))
    t = float(input("Masukan tinggi: "))
    luas = lambda p,l,t : 2 * (p * l + p * t + l * t)
    print ("luas balok: ", luas(p,l,t), "\n")

def luas_bola():
    print ("Hitung luas bola ready!")
    r = float(input("Masukan jari-jari: "))
    luas = lambda r : 4 * 3.14 * (r**2)
    print ("luas bola: ", luas(r), "\n")

while True:
    print('=========================')
    print('==== MENGHITUNG LUAS ====')
    print('=========================')

    userinput = int(input("Pilih rumus yang akan di pakai: \n\n1.Luas segitiga \n2.Luas balok \n3.Luas bola\n0.Keluar program\n\nPilih nomer berapa: "))
    os.system('cls')
    if(userinput == 1):
        luas_segitiga()
    elif(userinput == 2):
        luas_balok()
    elif(userinput == 3):\
        luas_bola()
    else:
        break
    