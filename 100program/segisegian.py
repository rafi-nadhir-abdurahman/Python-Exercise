import os

def segiTiga():
    s = int(input('Masukan alas : '))
    keliling = lambda s : s * s * s

    print(f'Keliling : {keliling(s)} cm2\n')

def segiEmpat():
    s = int(input('Masukan sisi : '))
    keliling = lambda s : 4 * s

    print(f'Keliling : {keliling(s)} cm2\n')

def segiLima():
    s = int(input('Masukan panjang sisi : '))
    keliling = lambda s : 5 * s

    print(f'keliling : {keliling(s)}')

def segiEnam():
    s = int(input('Masukan panjang sisi : '))
    keliling = lambda s : 6 * s

    print(f'keliling : {keliling(s)}')

def segiTujuh():
    s = int(input('Masukan panjang sisi : '))
    keliling = lambda s : 7 * s

    print(f'keliling : {keliling(s)}')

def segiDelapan():
    s = int(input('Masukan panjang sisi : '))
    keliling = lambda s : 8 * s

    print(f'keliling : {keliling(s)}')

def segiSembilan():
    s = int(input('Masukan panjang sisi : '))
    keliling = lambda s : 9 * s

    print(f'keliling : {keliling(s)}')

def segiSepuluh():
    s = int(input('Masukan panjang sisi : '))
    keliling = lambda s : 10 * s

    print(f'keliling : {keliling(s)}')

while True:
    print('================================')
    print('===== KELILING SEGI SEGIAN =====')
    print('================================')

    userinput = int(input("Pilih segi yang akan di pakai: \n\n1.segitiga \n2.segiempat \n3.segilima\n4.segienam\n5.segitujuh\n6.segidelapan\n7.segisembilan\n8.segisepuluh\n0.Keluar program\n\nPilih nomer berapa: "))
    os.system('cls')
    if(userinput == 1):
        segiTiga()
    elif(userinput == 2):
        segiEmpat()
    elif(userinput == 3):
        segiLima()
    elif(userinput == 4):
        segiEnam()
    elif(userinput == 5):
        segiTujuh()
    elif(userinput == 6):
        segiDelapan()
    elif(userinput == 7):
        segiSembilan()
    elif(userinput == 8):
        segiSepuluh()