# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 31/07/2024
# program game tebak angka

import random

angka = random.randint(1,5)


while True:
    print("----------------------")
    print("---GAME TEBAK ANGKA---")
    print("---------------------- \n")
    userinput = int(input("masukan angka: "))
    if(userinput == angka):
        print ("KAMU MENANG!!\n")
    elif(userinput != angka):
        print("KAMU KALAH!!\n")
    else:
        break