buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
namaBuah = str(input("Nama buah yang dibeli :"))
include = namaBuah in buah

if include:
    while True:
        jumlahBerat = float(input("Berapa Kg   :"))
        price = buah.get(namaBuah, 0)
        totalHarga = jumlahBerat * price
        print("-"*25)
        print("Total harga : Rp.", totalHarga)
        break
else:
    print("Buah tidak tersedia")

