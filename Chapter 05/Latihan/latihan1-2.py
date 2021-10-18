print("________Syarat Nilai Kelulusan_________")
bIndo = int(input("Masukan nilai Bhs Indonesia :"))
ipa = int(input("Masukan nilai IPA :"))
mtk = int(input("Masukan nilai Matematika :"))

if(bIndo >= 0 and bIndo <=100) and (mtk >= 0 and mtk <=100) and (ipa >= 0 and ipa <=100):
     if (bIndo >= 60) and (ipa >= 60) and (mtk >= 70):
         print("Status Kelulusan : LULUS")
     else:
         print("Status Kelulusan : TIDAK LULUS")
else:
    print("Maaf input ada yang tidak valid")
