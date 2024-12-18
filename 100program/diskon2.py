print(30*"=")
print("MENENTUKAN DISKON BELANJA")
print(30*"=")

print("anda akan mendapatkan diskon 25% jika total belanja anda\nlebih dari 100 ribu")

input_user = float(input("masukan total belanja anda = "))
diskon = input_user * 25 / 100
total_harga_diskon = input_user - diskon
if input_user >= 100:
    print(f"selamat anda mendapat diskon sebesar = 25%")
    print(f"diskon anda adalah = {diskon}")
    print(f"ini adalah total harga yang harus anda bayar = {total_harga_diskon}")
elif input_user < 100:
    print(f"maaf karena total belanja anda adalah = {input_user}\nmaka anda tidak mendapat diskon")
print("terima kasih")