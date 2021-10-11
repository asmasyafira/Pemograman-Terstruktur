print("_______________Tarif Rental Mobil_______________")
biayaSewa1 = int(input("Harga sewa 12 Jam pertama: Rp."))
biayaSewa2 = int(input("Harga sewa setelah 12 jam per jamnya: Rp."))
print("___________________Waktu Peminjaman_______________________")
jamRental1 = float(input("Jam:"))
menitRental1 = float(input("Menit:"))
print("___________________Waktu Pengembalian_______________________")
jamRental2 = float(input("Jam:"))
menitRental2 = float(input("Menit:"))

lamaWaktuRental = int((jamRental2 - jamRental1) + (menitRental2 - menitRental1)/ 60)
print("Total lama waktu rental :",lamaWaktuRental, "jam")
waktuLanjut = lamaWaktuRental - 12
print("Tambahan waktu rental:", waktuLanjut, "jam")

biayaLanjut = biayaSewa2 * waktuLanjut
print("Tambahan harga lanjut rental : Rp.", biayaLanjut)
totalTarifSewa = biayaLanjut + biayaSewa1
print("Total biaya rental : Rp.", totalTarifSewa)
