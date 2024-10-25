print('='*40)
print('PROGRAM TABUNG')
print('='*40)

R = float(input('masukan jari jari: '))
T = float(input('masukan tinggi: '))

PHI = 3.14
volume = PHI * R * R * T
LP = (2 * PHI * R * T) + (2 *(2 * PHI))

print('volume',volume,'cm2')
print('LP:',LP,'cm2')