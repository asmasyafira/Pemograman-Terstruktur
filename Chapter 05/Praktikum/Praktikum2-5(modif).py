from random import randint
jumlahPerulangan = 0
while True:
    bil = randint(0, 10)
    print(bil)
    jumlahPerulangan += 1
    if bil == 5:
        break
print('Jumlah Perulangan =', jumlahPerulangan)
