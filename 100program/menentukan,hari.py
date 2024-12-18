rint(30*"=")
print("PROGRAM MENENTUKAN HARI")
print(30*"=")

menu_bulan = {
    "januari"  : 31,
    "februari" : 29,
    "maret"    : 31,
    "april"    : 30,
    "mei"      : 31,
    "juni"     : 30,
    "juli"     : 31,
    "agustus"  : 31,
    "september": 30,
    "oktober"  : 31,
    "november" : 30,
    "desember" : 31
}
for bulan,hari in menu_bulan.items():
    print(f"bulan = {bulan}, jumlah hari = {hari}")

input_user = str(input("masukan nama bulan = "))

print(f"{bulan} yang anda pilih punya = {hari} hari")