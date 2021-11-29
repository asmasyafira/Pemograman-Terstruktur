mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('=' * 60)
print('NIM'.ljust(5), 'NAMA MAHASISWA'.ljust(20), 'TGL LAHIR'.ljust(15), 'TEMPAT LAHIR')
print('-' * 60)
for data in mhs:
    listData = data.split(":")
    date = listData[2].split('-')
    birthDate = date[2] + '/' + date[1] + '/' + date[0]
    print(listData[0].ljust(5),
          listData[1].ljust(20),
          birthDate.ljust(15),
          listData[3])
print('-' * 60)
