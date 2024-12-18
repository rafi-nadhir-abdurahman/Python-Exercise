print('\n========================================')
print('============= JARAK LENSA ===========')
print('========================================\n')

fob = int(input('Masukan fokus lensa objektif : '))
fok = int(input('Masukan fokus lensa okuler : '))
fp = int(input('Masukan fokus lensa pembalik : '))
rumus = fob + (4*fp) + fok 

print(f'\npanjang teropong : {round (rumus, 2)}\n')