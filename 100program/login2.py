print ("-------------------------")
print ("Verifikasi Login Anda")
print ("-------------------------")

username = str(input("Masukkan Username Anda: "))
password = str(input("Masukkan Password Anda: "))

if username == "admin" and password == "nimda123":
    print ('''-------------------------
Verifikasi Berhasil
-------------------------''')

else:
    print ('''-------------------------
Verifikasi Gagal
-------------------------''')