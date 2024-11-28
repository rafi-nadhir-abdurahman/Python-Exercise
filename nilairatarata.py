def nilaiRatarata():
      print('===========================')
      print('==== NILAI RATA - RATA ====')
      print('===========================')

      nama = input('Masukan nama : ')
      kelamin = input('masukan gender : ')
      usia = input('masukan umur : ')
      nilai_mtk = int(input('masukan nilai matematika : '))
      nilai_bindo = int(input('''masukan nilai bahasa indonesia : '''))
      nilai_ipas = int(input('masukan nilai ipas : '))
      nilai_binggris = int(input('masukan nilai bahsa inggris : '))
      jumlah =nilai_mtk + nilai_bindo + nilai_ipas + nilai_binggris
      rata_rata = jumlah/4
      print(f'''
      Nama saya adalah {nama},saya berjenis kelamin {kelamin},
      sekarang usia saya adalah {usia}.
      Nilai ujian terakhir saya adalah sebagai berikut
      Matematika  : {nilai_mtk}
      B.Indonesia : {nilai_bindo}
      B.Inggiris  : {nilai_binggris}
      IPAS        : {nilai_ipas}
      jumlah      : {jumlah}
      Rata-rata   : {rata_rata}
      ''')