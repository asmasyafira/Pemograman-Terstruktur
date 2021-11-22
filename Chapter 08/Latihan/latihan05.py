def kuadrat(bil):
    for i in range(len(bil)):
        bil[i] **= 2
    return bil


jumlahBilangan = int(input("Berapa bilangan yang ingin dimasukkan :"))
dataBil = []
for i in range(jumlahBilangan):
    angka = int(input("Masukkan bilangan :"))
    dataBil.append(angka)
print("Kuadrat dari setiap bilangan yang dimasukkan\n", kuadrat(dataBil))
