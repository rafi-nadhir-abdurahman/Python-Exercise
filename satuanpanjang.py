print(30*"=")
print("PROGRAM MENGHITUNG KONVERSI")
print(30*"=")


try:
    inputan = int(input("masukan satuan meter = "))
    mllimeter = inputan * 1000
    sentimeter = inputan * 100
    dekameter = inputan % 10
    hektometer = inputan % 100
    kilometer = inputan % 1000
    print(f"""hasil konversi meter {inputan}\nmilimeter = {mllimeter}\nsentimeter = {sentimeter}\ndekameter = {dekameter}\nhektometer = {hektometer}\nkilometer = {kilometer}""")
except ValueError:
    print("inputan anda tidak valid")
    print("masukan inputan bertipe integer saja")