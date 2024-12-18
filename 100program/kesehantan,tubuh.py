print("="*35)
print("PROGRAM MENENTUKAN KESEHATAN TUBUH")
print("="*35)
    
try:            
    berat_badan = float(input("Masukkan berat badan Anda :  "))
    tinggi_badan = float(input("Masukkan tinggi badan Anda : "))
    usia = int(input("Masukkan usia Anda : "))

    bmi = berat_badan  /  (tinggi_badan ** 2)

    if bmi < 18.5:
        kategori = " anda Kekurangan berat badan"
        risiko = "anda beresiko tinggi untuk:\n- Malnutrisi\n- Osteoporosis\n- Sistem imun yang lemah"
    elif 18.5 <= bmi < 24.9:
        kategori = "Berat badan normal"
        risiko = "anda beresiko rendah untuk masalah kesehatan."
    elif 25 <= bmi < 29.9:
        kategori = "Kelebihan berat badan"
        risiko = "anda resiko meningkat untuk:\n- Diabetes tipe 2\n- Penyakit jantung\n- Tekanan darah tinggi"
    else:
        kategori = "Obesitas"
        risiko = "anda beresiko tinggi untuk:\n- Diabetes tipe 2\n- Penyakit jantung\n- Hipertensi\n- Masalah tidur (sleep apnea)\n- Beberapa jenis kanker"

    print(f"\nIndeks Massa Tubuh (BMI) Anda: {bmi:.2f}")
    print(f"Kategori: {kategori}")
    print("Risiko kesehatan:")
    print(risiko)
    
except ValueError:
    print("Anda memasukkan data yang salah.")
    print("Silakan masukkan angka bulat atau float.")