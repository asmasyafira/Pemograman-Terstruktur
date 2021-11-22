dataSayur = ['Bayam', 'Kangkung', 'Wortel', 'Selada']
print("Menu :\n"
      "A. Tambah data sayur\n"
      "B. Hapus data sayur\n"
      "C. Tampilkan data sayur\n")

while True:
    choice = input("Pilihan Anda :")
    if choice == 'A' or choice == 'a':
        addSayur = input("Masukkan nama sayur yang ingin ditambahkan :")
        dataSayur.append(addSayur)
        print("Data Sayur Sekarang :\n", dataSayur)
    elif choice == 'B' or choice == 'b':
        deleteSayur = input("Hapus nama sayur yang sudah ada :")
        if deleteSayur in dataSayur:
            dataSayur.remove(deleteSayur)
            print("Data Sayur Sekarang :", dataSayur)
        else:
            print("Data Sayur yang dimaksud tidak ditemukan")
    elif choice == 'C' or choice == 'c':
        print("Data Sayur Sekarang :", dataSayur)
    else:
        print("Tidak ada pilihan menu")
    repeat = input("Apakah anda ingin mengolah data sayur lagi (y/n)?")
    if repeat == 'y':
        continue
    elif repeat == 'n':
        print("Terima Kasih")
        break
    else:
        print("Tidak terdapat pada pilihan")


