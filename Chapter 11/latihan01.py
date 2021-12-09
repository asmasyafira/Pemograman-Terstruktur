from datetime import *


def diffDate(x):
    skrg = datetime.date(datetime.now())
    print('Tanggal saat ini yaitu', skrg)

    dateSplit = x.split('-')
    diff = date(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
    print('Tanggal yang diinginkan yaitu', diff)

    print('=' * 50)
    selisihDate = (diff - skrg).days
    print('Selisih hari dari tanggal hari ini yaitu', selisihDate)
    return selisihDate


try:
    tanggal = input('Input Tanggal yang Diinginkan (YYYY-MM-DD) :')
    diffDate(tanggal)
except IndexError:
    print('Masukan Tanggal Sesuai Format Kalender')
except ValueError:
    print('Masukan Tanggal Sesuai Format Kalender')
