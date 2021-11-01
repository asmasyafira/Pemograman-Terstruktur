def luasSegitiga(a, t):
    luas = a * t / 2
    return luas

alas = 10
tinggi = 20
luasSegitiga0 = luasSegitiga(alas, tinggi)
print('Luas segitiga dg alas ', alas,
      ' dan tinggi ', tinggi, ' adalah ', luasSegitiga0)

alas1 = 15
tinggi1 = 45
luasSegitiga1 = luasSegitiga(alas1, tinggi1)
print('Luas segitiga dg alas ', alas1,
      ' dan tinggi ', tinggi1, ' adalah ', luasSegitiga1)

print('Total luas kedua segitiga adalah', luasSegitiga0 + luasSegitiga1)
