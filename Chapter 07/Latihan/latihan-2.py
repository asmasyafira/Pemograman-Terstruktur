import os

nameFile = input("Masukkan nama file: ")
existence = os.path.exists(nameFile)

try:
    if existence is True:
        file = open(nameFile, "a")
        file.write(input("Data yang mau ditambahkan: "))
        tambah = input("Mau lagi (y/n) : ")
        while tambah == 'y':
            file.write(input("Data yang mau ditambahkan: "))
            Add = input("Mau lagi (y/n) : ")
            if Add == 'n':
                file.close()
                break
        look = input('ingin lihat isi file?(y/n):')
        if look == 'n':
            file.close()
        elif look == 'y':
            file = open(nameFile, "r")
            print(file.read())
            file.close()
        else:
            print('data tidak valid')
    else:
        print('File tidak ada')
except FileNotFoundError:
    print("File Tidak Ada")
except ValueError:
    print('Input tidak valid')
except PermissionError:
    print('Permission tidak valid')
