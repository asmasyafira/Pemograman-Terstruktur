angka = 0
hitung = 0
hasil = 0
while(angka <= 100):
    if(angka % 2 == 1):
        hitung += 1
        hasil += angka
        print(angka)
    angka += 1
print("Banyaknya bilangan ganjil :",hitung)
print("Jumlah seluruh bilangan :",hasil)
