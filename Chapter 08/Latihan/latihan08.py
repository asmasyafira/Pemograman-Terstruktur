def average(a):
    nilai = tuple(a.values())
    jumlahData = sum(nilai)
    jumlahBil = len(nilai)
    ratarata = jumlahData / jumlahBil
    return ratarata


buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
print("Rata-rata harga satuan buahnya adalah", average(buah))
