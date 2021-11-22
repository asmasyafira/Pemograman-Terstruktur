buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}

for a, b in buah.items():
    print('-', a, '=', b)

print('Menu:\n'
      'A. Tambah data buah\n'
      'B. Beli Buah\n'
      'C. Selesai')

while True:
    choice = input('Pilihan menu (A/B/C) = ')
    if choice == 'A' or choice == 'a':
        while True:
            add = str(input('Masukkan nama buah = '))
            if add in buah:
                print('Nama buah sudah ada')
                continue
            else:
                hargabaru = int(input('Masukkan harga satuan ='))
                buah.update({add: hargabaru})
                tambahlagi = str(input('Mau menambahkan lagi(y/n)?'))
                if tambahlagi == 'y':
                    continue
                elif tambahlagi == 'n':
                    print('Data Buah')
                    for a, b in buah.items():
                        print('-', a, '(Harga Rp.', b, ')')
                    break
        continue
    elif choice == 'B' or choice == 'b':
        totalHarga = 0
        while True:
            namaBuah = str(input('Nama buah yang akan dibeli = '))
            if namaBuah in buah:
                jumlah = float(input('Berapa Kg = '))
                total = jumlah * buah[namaBuah]
                totalHarga += total
                lagi = str(input('Mau beli buah yang lain(y/n)? '))
                if lagi == 'y':
                    continue
                elif lagi == 'n':
                    print('-'*15)
                    print('Total harga = Rp.', totalHarga)
                    print('-' * 15,
                          '\nTerima Kasih\n')
                    break
            else:
                print('Buah tidak tersedia')
    elif choice == 'C' or choice == 'c':
        print('-'*15,
              '\nTerima Kasih\n')
    else:
        print('Pilihan tidak tersedia')
        continue
    break
