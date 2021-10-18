print("________Syarat Nilai Kelulusan_________")
bIndo = int(input("Masukan nilai Bhs Indonesia :"))
ipa = int(input("Masukan nilai IPA :"))
mtk = int(input("Masukan nilai Matematika :"))

if(bIndo >= 0 and bIndo <=100) and (mtk >= 0 and mtk <=100) and (ipa >= 0 and ipa <=100):
     if (bIndo >= 60) and (ipa >= 60) and (mtk >= 70):
         print("Status Kelulusan : LULUS")
     else:
         sebab = ""
         if(bIndo < 60):
             sebab += ("- Nilai bahasa indonesia kurang dari 60")
         if(ipa < 60):
             sebab += ("- Nilai IPA kurang dari 60")
         if(mtk < 70):
             sebab += ("- Nilai Matematika kurang dari 70")
         print("Status Kelulusan : TIDAK LULUS")
         print("Sebab : ")
         print(sebab)
else:
    print("Maaf input ada yang tidak valid")
