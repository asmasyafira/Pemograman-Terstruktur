jumlahNama = int(input("Berapa nama yang ingin dimasukkan = "))
listNama = []
i = 0

for i in range(jumlahNama):
    nama = input("Masukkan nama :")
    listNama.append(nama)
listNama.sort()
print("---------LIST NAMA-----------")
r = 0
for r in range(len(listNama)):
    print(listNama[r], '(', len(listNama[r]), 'karakter)')
    r += 1
