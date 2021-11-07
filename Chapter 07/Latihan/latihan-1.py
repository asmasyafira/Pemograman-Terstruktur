nameFile = input("Masukkan nama file:")

try:
    file = open(nameFile, 'r')
    print("Isi file", nameFile, "adalah", file.read())
except FileNotFoundError:
    print("File tidak ada / salah penulisan")

