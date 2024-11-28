print('='*20)
print('Inputan Perkalian')
print('='*20)

jumlah_perkalian = int(input("Masukkan jumlah perkalian: "))

for i in range(1, jumlah_perkalian+1):
  for j in range(1, 3):
    hasil = i * j
    print(f"{j} x {i} = {hasil}", end="  ")
  print()