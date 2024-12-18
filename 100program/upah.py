# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 27/10/2024
# program upah kerja

print('===========================')
print('=========== UPAH ==========')
print('===========================')

golongan = input('masukkan golongan (A,B,C,D): ').upper()
jam_kerja = int(input('masukkan jam kerja: '))
jam_lembur = int(input('masukkan jam lembur: '))

if golongan == 'A':
    upah_perjam = 4000
elif golongan == 'B':
    upah_perjam = 5000
elif golongan == 'C':
    upah_perjam = 6000
elif golongan == 'D':
    upah_perjam = 7500
else:
    print('golongan tidak ada')
    upah_perjam = 0

upah_kerja = jam_kerja * upah_perjam
upah_lembur = jam_kerja * (upah_perjam * 1.5)
total_upah = jam_lembur + upah_perjam

print(f'total upah : Rp.{round(total_upah)}')