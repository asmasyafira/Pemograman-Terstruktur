from datetime import *

myFile = open("dataPerpus.txt", "a")


def libraryMember(kode, nama, judul):
    file = open("dataPerpus.txt", "a")
    tglPinjam = datetime.date(datetime.now())
    tglKembali = tglPinjam + timedelta(days=7)
    data = [kode, nama, judul, str(tglPinjam), str(tglKembali)]
    file.write('|'.join(data) + "\n")
    file.close()


while True:
    kodeMember = str(input("Masukan Kode Member : "))
    namaMember = str(input("Masukan Nama Member : "))
    judulBuku = str(input("Masukan Judul Buku : "))
    libraryMember(kodeMember, namaMember, judulBuku)
    ulangLagi = str(input("\nUlangi lagi (y/n) : "))
    if ulangLagi == "y":
        continue
    elif ulangLagi == "n":
        break
    else:
        print("Input Data tidak Valid")
        break


