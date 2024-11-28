print('='*20)
print('PERKONDISIAN')
print('='*20)
# 1
kondisi = str(input('masukan kondisi air : '))

if kondisi == 'mendidih':
    print('matikan kompor')
elif kondisi == 'anget':
    print('tunggu sebentar lagi')
elif kondisi == 'dingin':
    print('nyalakan api kompor paling besar')



# 2
suhu = int(input('masukan suhu ruangan dalam bentuk celcius : '))

if suhu >= 50:
    print('nyalakan tanda bahaya')
elif suhu <= 20:
    print('matikan ac')
else:
    print('suhu ruangan nya berapa bang')