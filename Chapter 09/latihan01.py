# cara biasa
def ubahHuruf(teks, a, b):
    listText = list(teks)
    result = []
    for huruf in listText:
        if huruf == a:
            huruf = b
        result.append(huruf)
    print(''.join(result))


# cara alternatif
def ubahHuruf2(teks, a, b):
    print(teks.replace(a, b))


ubahHuruf('MATEMATIKA', 'T', 'S')
ubahHuruf2('MATEMATIKA', 'T', 'S')