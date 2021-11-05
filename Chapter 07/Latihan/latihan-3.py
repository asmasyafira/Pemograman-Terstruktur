print("-----------------------------")
print("   PROGRAM HITUNG RATA-RATA  ")
print("-----------------------------")

angka = True
jumlah = 0
jumlahBilangan = 0
while(angka == True):
    try:
        inputNumber = int(input("Masukkan bilangan bulat :"))
        jumlah+=inputNumber
        jumlahBilangan+=1
        add = input("Lagi(y/n)?")
        if(add=='y'):
            angka=True
        elif(add=='n'):
            angka=False
        else:
            print("Input yang anda masukkan tidak sesuai")
    except ValueError:
        print("Data yang dimasukkan bukan bilangan bulat")

average = jumlah/jumlahBilangan
print("Rata-ratanya adalah", average)
        
        
        
