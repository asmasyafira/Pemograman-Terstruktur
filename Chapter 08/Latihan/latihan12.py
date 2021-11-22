buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}

for a, b in buah.items():
    print('-', a, '=', b)
print('Menu:\n'
      'A. Tambah Bata Buah\n',
      'B. Hapus data Buah\n',
      'C. Beli Buah\n',
      'D. Tutup Program\n')

while True:
    choice = input('Masukkan Pilihan Anda(A/B/C) = ')
    if choice == 'A' or choice == 'a':
        while True:
            add = str(input('Masukkan nama buah yang ingin di data = '))
            if add in buah:
                print('Nama buah sudah ada')
                continue
            else:
                addHarga = int(input('Masukkan harga buah ='))
                buah.update({add: addHarga})
                addAgain = str(input('Mau menambahkan lagi(y/n)?'))
                if addAgain == 'y':
                    continue
                elif addAgain == 'n':
                    print('Data Buah')
                    for a, b in buah.items():
                        print('-', a, '=', b)
                    break
        continue
    elif choice == 'B' or choice == 'b':
        delete = input('Masukkan data buah yang ingin dihapus = ')
        if delete in buah:
            buah.pop(delete)
            print('Data Buah')
            n = 0
            for a, b in buah.items():
                n += 1
                print(n, '.', a, '=', b)
            continue
        else:
            print('Nama Buah Tidak Ditemukan')
            continue
    elif choice == 'C' or choice == 'c':
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
                    print('Total harga =Rp.', totalHarga)
                    print('-' * 15,
                          '\nTerima Kasih\n')
                    break
            else:
                print('Buah tidak tersedia')
                continue
    elif choice == 'D' or choice == 'd':
        print('-' * 15,
              '\nTerima Kasih\n',)
    break
