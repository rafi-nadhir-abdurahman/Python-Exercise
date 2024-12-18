def kalorEs():
    print('========================================')
    print('============= KALOR JENIS ES ===========')
    print('========================================\n')

    m = int(input('Masukan massa benda : '))
    c = 2100
    l = 336000
    ca = 4200
    suhu1 = int(input('Berapakah suhu pertama : '))
    suhu2 = int(input('Berapakah suhu kedua : '))
    rumus = lambda m,c,suhu1,suhu2 : m * c * (suhu2 - suhu1)
    rumus2 = lambda m,l : m * l

    print('\n================ KALOR JENIS ES =================')
    print(f'Jadi kalor jenis es adalah : {round (rumus(m,c,suhu1,suhu2),2)} J')
    print('\n================ KALOR LEBUR ES =================')
    print(f'Jadi kalor jenis es adalah : {round (rumus2(m,l),2)} J/KG')
    print('\n================ KALOR JENIS AIR ================')
    print(f'Jadi kalor jenis es adalah : {round (rumus2(m,l),2)} KJ\n')

kalorEs()