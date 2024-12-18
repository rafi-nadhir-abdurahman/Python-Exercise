import os

def rumus():
    la = float(input('Masukan luas alas limas : '))
    t = float(input('Masukan tinggi limas : '))
    st = float(input('Masukan luas sisi tegak limas : '))

    lp = lambda la,st : la + st
    v = lambda la,t : 1 / 3 * la * t

    print(f'Luas permukaan : {lp(la,st)}')
    print(f'Volume : {v(la,t)}')


while True:
    print('===========================')
    print('====== LIMAS LIMASAN ======')
    print('===========================')

    userinput = int(input("Pilih segi yang akan di pakai: \n\n1.Limas segitiga\n2.Limas segiempat\n3.Limas segilima\n4.Limas segienam\n5.Limas segitujuh\n6.Limas segidelapan\n7.Limas segisembilan\n8.Limas segisepuluh\n0.Keluar program\n\nPilih nomer berapa: "))
    os.system('cls')
    if(userinput == 1):
        print('RUMUS LIMAS SEGI TIGA READY!!!')
        rumus()
    elif(userinput == 2):
        print('RUMUS LIMAS SEGI TIGA READY!!!')
        rumus()
    elif(userinput == 3):
        print('RUMUS LIMAS SEGI TIGA READY!!!')
        rumus()
    elif(userinput == 4):
        print('RUMUS LIMAS SEGI TIGA READY!!!')
        rumus()
    elif(userinput == 5):
        print('RUMUS LIMAS SEGI TIGA READY!!!')
        rumus()
    elif(userinput == 6):
        print('RUMUS LIMAS SEGI TIGA READY!!!')
        rumus()
    elif(userinput == 7):
        print('RUMUS LIMAS SEGI TIGA READY!!!')
        rumus()
    elif(userinput == 8):
        print('RUMUS LIMAS SEGI TIGA READY!!!')
        rumus()