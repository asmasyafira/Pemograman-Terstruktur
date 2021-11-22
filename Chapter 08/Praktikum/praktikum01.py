a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
print("Data awal list A \n", a)
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print("Data awal list B \n", b)
print("")

a.insert(3, 10)
print("Nilai dari list A disisipkan dengan 10 ke indeks 3\n", a)
b.insert(2, 15)
print("Nilai dari list B disisipkan dengan 15 ke indeks 2\n", b)
print("")

a.append(4)
print("Nilai dari list A disisipkan dengan 4 ke indeks terakhir\n", a)
b.append(8)
print("Nilai dari list B disisipkan dengan 8 ke indeks terakhir\n", b)
print("")

a.sort()
print("List A disorting secara ascending\n", a)
b.sort()
print("List B disorting secara ascending\n", b)
print("")

c = a[:8]
print("List C adalah sublist dari a [indeks 0-7]\n", c)
d = b[2:10]
print("List D adalah sublist dari a [indeks 2-9]\n", d)

e = []
for i in range(len(d)):
    e += [c[i] + d[i]]
print("\nHasil list e yang merupakan penjumlahan dari setiap elemen c dan d\n", e)

eTuple = tuple(e)
print("\nList e dijadikan tuple\n", eTuple)

eMin = min(e)
print("\nNilai minimal dari tuple e\n", eMin)
eMax = max(e)
print("\nNilai maksimal dari tuple e\n", eMax)
eSum = sum(e)
print("\nHasil jumlah seluruh elemen dari tuple e\n", eSum)

myString = "python adalah bahasa pemrograman yang menyenangkan"
print("\nIsi dari variable myString\n", myString)

myStringSet = set(myString)
print("\nKarakter huruf yang menyusun myString\n", myStringSet)

myStringSetList = list(myStringSet)
print("\nBentuk list dari variable myString \n", myStringSetList)
myStringSetList.sort()
print("\n List myStringSet setelah di sorting secara ascending \n", myStringSetList)












