print("______Total Pengisian Bensin Selama Perjalanan______")
jarakKota = int(input("Jarak kota A ke kota C :"))
jarakLiter = int(input("Jarak yang ditempuh per liter :"))
totalKapTangki = int(input("Total kapasitas isi bensin :"))

totalLiter = jarakKota/jarakLiter
print("Banyaknya bensin yang diperlukan:",totalLiter,"liter")

jumlahNgisi = totalLiter//totalKapTangki
print("Total minimal pengisian:",jumlahNgisi, "kali")
