def dataStat(x):
    r = []
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    r.extend([a, b, c])
    return a, b, c


jumlahBilangan = int(input("Jumlah bilangan yang ingin dimasukkan ="))
a = []
i = 0
for i in range(jumlahBilangan):
    angka = int(input("Masukkan bilangan :"))
    a.append(angka)
print(dataStat(a))