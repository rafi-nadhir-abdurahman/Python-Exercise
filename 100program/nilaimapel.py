mapel= str(input('masukan nama mapel '))
uts = int(input('masukan nilai uts '))
uas= int(input('masukan nilai uas '))
tugas= int(input('masukan nilai tugas '))
rata=uts+uas+tugas/3
if rata >=85:
    print(f"untuk mapel {mapel} kamu dapat grade A")
elif rata >=70:
    print(f"untuk mapel {mapel} kamu dapat grade B")
elif rata >=60:
    print(f"untuk mapel {mapel} kamu dapat grade C")
else:
    print(f"untuk mapel {mapel} kamu dapat grade D")