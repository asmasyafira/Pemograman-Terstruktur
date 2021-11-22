def expensive(price):
    listHarga = list(price.values())
    listHarga.sort()
    listHarga.reverse()
    indexHarga = listHarga[0]
    for x, y in price.items():
        if y == indexHarga:
            return x
    return indexHarga


buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
print("Buah dengan harga satuan termahal adalah", expensive(buah))
