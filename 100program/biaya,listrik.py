TARIF = 1500

print(30 *"=")  
print("PROGRAM MENENTUKAN BIAYA LISTRIK") 
print(30 * "=")

try:
    bulan_pemakaian = float(input("berapa bulan yang anda inginkan = "))
    daya_listrik = float(input("masukan besar daya (w/watt) = "))
    waktu = float(input("berapa total jam pemakaian per bulan = "))
    biaya_listrik = (daya_listrik / 1000) * waktu * TARIF * 30 * bulan_pemakaian
    print(f"biaya listrik rumah anda selama {bulan_pemakaian} bulan = {biaya_listrik:.2f} ")
        

except ValueError:
    print("inputan anda tidak valid")
    print("masukan bilangan bulat / float")