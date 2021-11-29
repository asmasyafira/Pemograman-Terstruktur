nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
         {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
         {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]

print('=' * 50)
print("NIM".ljust(5), "NAMA".ljust(9), "N.MID".ljust(7), "N.UAS".ljust(7),
      "N.AKHIR".ljust(9), "STATUS")
print('-' * 50)
for data in nilai:
    nAkhir = data['mid'] + 2 * data['uas'] / 3
    status = 'LULUS'
    if nAkhir < 60 or nAkhir == 60:
        status = 'TIDAK LULUS'
    print(data['nim'].ljust(6),
          data['nama'].ljust(10),
          str(data['mid']).ljust(8),
          str(data['uas']).ljust(5),
          str(round(nAkhir, 1)).ljust(8),
          status)

print('-' * 50)
