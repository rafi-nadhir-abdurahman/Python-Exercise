print('='*40)
print("PROGRAM PEGULAGAN KALIMAT / KATA")
print('='*40)

try:
    input_pesan = str(input("masukan pesan yang akan di ulang : "))
    input_no = int(input("berapa kali ingin di ulang : "))
    for i in range(input_no):
        print(f"{i+1}.{input_pesan}")

except ValueError:
    print("inputan anda tidak valid")