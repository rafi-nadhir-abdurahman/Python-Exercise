pin = "nimda123"

print ("-------------------------")
print ("Verifikasi Login Anda")
print ("-------------------------")

username = input ("Masukkan Username Anda: ")
password = input("Masukkan Password Anda: ")

if password == pin:
    print (f'''-------------------------
Login berhasil
-------------------------''')
else:
    print (f'''-------------------------
Maaf, Password Salah
-------------------------''')