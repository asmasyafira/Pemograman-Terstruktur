myFile = "dataMhs.txt"
true = "y"


def inputMhs(myFile, nim, nama, alamat):
    data = open(myFile, "a")
    data.write("{}|{}|{}\n".format(nim, nama, alamat))
    data.close()


def viewMhs(myFile):
    hasil = open(myFile, "r")
    for x in hasil:
        print(x)
    hasil.close()


while true == "y":
    nim = input('\nMasukan NIM\t : ')
    nama = input('Masukan Nama Mhs : ')
    alamat = input('Masukan Alamat\t : ')
    inputMhs(myFile, nim, nama, alamat)
    jawab = input('\nUlangi input lagi (y/n) : ')
if true == "n":
    viewMhs(myFile)
