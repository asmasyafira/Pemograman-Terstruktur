buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}

while True:
    namaBuah = str(input("Nama buah yang ingin dibeli :"))
    if namaBuah in buah:
        jumlahBerat = float(input("Berapa Kg  :"))
        price = buah.get(namaBuah, 0)
        totalHarga = jumlahBerat * price
        lagi = str(input('Beli buah yang lain(y/n)? '))
        if lagi == 'y':
            continue
        elif lagi == 'n':
            print("-" * 25)
            print('Total harga =', totalHarga)
            break
        else:
            print('Pilihan tidak tersedia')
    else:
        print("Buah tidak tersedia")
