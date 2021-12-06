myFile = open("file.txt", "r")
teks = myFile.readlines()
angkaGenap = 0
angkaGanjil = 0
a = list(teks)
c = []

for i in a:
    b = int(i)
    d = c.append(b)

for data in c:
    if data % 2 == 0:
        angkaGenap += 1
    else:
        angkaGanjil += 1

myFile.close()
print('Banyak bilangan genap: ', angkaGenap)
print('Banyak bilangan ganjil: ', angkaGanjil)
