print('='*30)
print('Menentukan segitiga')
print('='*30)

a1 = int(input('Masukan sudut alas 1 : '))
a2 = int(input('Masukan sudut alas 2   : '))
t = int(input('Masukan sudut tiggi    : '))

if a1 == a2 == t:
    print('Segitiga sama sisi')
elif a1 == a2 > t :
    print('Segitiga sama kaki')
elif a1 == 90 or a2 == 90:
    print('Segitiga siku-siku')
elif a1 > 90 or a2 > 90 or t > 90:
    print('Segitiga tumpul')
elif a2 == a1 > t :
    print('Segitiga sama kaki')
elif a2 == 90 or a1 == 90:
    print('Segitiga siku-siku')
elif a2 > 90 or a1 > 90 or t > 90:
    print('Segitiga tumpul')
else :
    print('Segitiga sembarang')