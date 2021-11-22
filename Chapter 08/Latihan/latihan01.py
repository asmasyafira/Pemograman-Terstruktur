jumlahAngka = int(input("Berapa angka yang ingin dimasukkan?"))
x = []
i = 0
for i in range(jumlahAngka):
    angka = int(input("Masukkan bilangan :"))
    x.append(angka)
x.sort()
x.reverse()
print("List =", x)
