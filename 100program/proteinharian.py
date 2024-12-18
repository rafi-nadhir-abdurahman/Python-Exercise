print("="*35)
print("PROGRAM MENENTUKAN JUMLAH PROTEIN  HARIAN".center(40))
print("="*35)

kelamin = str(input("masukan jenis kelamin anda (cowok/cewek) = ")).lower()
umur = int(input("masukan umur anda = "))


if kelamin == "cowok":
    if 1 <= umur <= 3:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari adalah 14 gram") 
    elif 4 <= umur <= 8:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari adalah 19 gram") 
    elif 9 <= umur <= 13:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari adalah 34 gram") 
    elif 14 <= umur <= 18:
        print("kamu sudah remaja")
        print("protein yang harus kamu konsumsi perhari adalah 52 gram") 
    elif 19 <= umur <= 50:
        print("kamu sudah dewasa")
        print("protein yang harus kamu konsumsi perhari adalah 56 gram") 
    elif umur < 51:
        print("kamu sudah manula")