def highGrades(data):
    nilaiTertinggi = 0
    dictionary = {}
    for i in data:
        uas = i.get('uas')
        mid = i.get('mid')
        nilaiAkhir = (mid + 2 * uas) / 3
        if nilaiAkhir > nilaiTertinggi:
            nilaiTertinggi = nilaiAkhir
            dictionary['nim'] = i.get('nim')
            dictionary['nama'] = i.get('nama')
    print('Mahasiswa dengan nilai tertinggi diraih oleh ', dictionary['nama'], 'dengan NIM', dictionary['nim'])


nilaiMhs = [{'nim': 'A01', 'nama': 'Amir', 'mid': 50, 'uas': 80},
            {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
            {'nim': 'A03', 'nama': 'Cici', 'mid': 50, 'uas': 50},
            {'nim': 'A04', 'nama': 'Dedi', 'mid': 20, 'uas': 30},
            {'nim': 'A05', 'nama': 'Fifi', 'mid': 70, 'uas': 40}]

highGrades(nilaiMhs)
