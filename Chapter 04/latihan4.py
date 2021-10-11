print("_______Waktu Pak Amir Tiba_______")
kotaAB = int(input("Jarak kota A ke kota B :"))
kotaBC = int(input("Jarak kota B ke kota C :"))
kecepatanAB = int(input("Kecepatan rata\" dari kota A ke kota B :"))
kecepatanBC = int(input("Kecepatan rata\" dari kota B ke kota C :"))

jamBerangkat = int(input("Jam:"))
menitBerangkat = int(input("Menit:"))
jamWaktuAB = kotaAB//kecepatanAB
menitWaktuAB = round((kotaAB/kecepatanAB - kotaAB//kecepatanAB)*60)
print('Lama Waktu tiba di kota B :',jamWaktuAB,'jam',menitWaktuAB,'menit')

jamIstirahat = int(input("Lama jam istirahat di kota B :"))
menitIstirahat = int(input("Lama menit istirahat di kota B :"))

jamWaktuBC = kotaBC//kecepatanBC
menitWaktuBC = round((kotaBC/kecepatanBC - kotaBC//kecepatanBC)*60)
print("Lama Waktu tiba di kota C :", jamWaktuBC,'jam',menitWaktuBC,'menit')

totalJamWaktu = (jamBerangkat + jamWaktuAB +  jamWaktuBC +  jamIstirahat)
totalMenitWaktu = (menitBerangkat + menitWaktuAB +  menitWaktuBC +  menitIstirahat)
if(totalMenitWaktu > 59):
    print("Jam", totalJamWaktu + 1, "lewat", totalMenitWaktu - 60, "menit")


