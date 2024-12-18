# Looping 4

print('*'*30)
print('\tPROGRAM LOOPING')
print('*'*30)

jumlah = int(input("\nMasukkan jumlah perkalian: "))

for a in range(1, jumlah+1):
  for b in range(1, 4):
    hasil = a * b
    print(f"{b} x {a} = {hasil}", end="\t")
  print()