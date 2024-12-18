print('='*20)
print('NILAI XYZ')
print('='*20)

x = int(input('masukan angka x : '))
y = int(input('masukan angka y : '))
z = int(input('masukan angka z : '))

if x > y and z:
    print('nilai x lebih besar dari y dan z')
elif y > x and z:
    print('nilai y lebih besar dari x dan z')
elif z > y and x:
    print('nilai y lebih besar dari y dan x')
else:
    print('nilai tidak konek')