from datetime import *
from datetime import date


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


def searchData(kode):
    file = open("dataPerpus.txt", "r")
    myFile = file.read().splitlines()
    for i in myFile:
        data = i.split("|")
        if kode == data[0]:
            print("Data Peminjaman Buku")
            print("Kode Member".ljust(25), ":", data[0])
            print("Nama Member".ljust(25), ":", data[1])
            print("Judul Buku".ljust(25), ":", data[2])
            print("Tanggal Mulai Pinjaman".ljust(25), ":", data[3])
            print("Tanggal Maks Pinjaman".ljust(25), ":", data[4])
            print("Tanggal Maks Pinjaman".ljust(25), ":", datetime.date(datetime.now()))

            keterlambatan = diffDate(data[4])
            if keterlambatan < 0:
                back = keterlambatan * (-1)
                print('Terlambat'.ljust(25), ": {} hari".format(back))
                denda = 2000 * abs(back)
                print('Denda'.ljust(25), ": Rp {} ".format(denda))
            elif keterlambatan > 0:
                print("Terlambat".ljust(25), ": Tidak Terlambat")


kodePinjaman = input("Masukan Kode Member   :".ljust(25))
searchData(kodePinjaman)


