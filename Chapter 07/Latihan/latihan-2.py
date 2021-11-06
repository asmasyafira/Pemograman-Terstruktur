nameFile = input("Masukkan nama file: ")

try:
    file = open(nameFile, "a")
    file.write(input("Data yang mau ditambahkan: "))
    tambah = input("Mau lagi (y/n) : ")
    while (tambah == 'y'):
        file.write(input("Data yang mau ditambahkan: "))
        Add = input("Mau lagi (y/n) : ")
        if (Add == 'n'):
            file.close()
except FileNotFoundError:
    print("File Tidak Ada")
except ValueError:
    print('Input tidak valid')
except PermissionError:
    print('Permission tidak valid')
