import time
import datetime

nama = input("Hallo... nama saya Mr. Kompie, nama Anda siapa? ")

print("Oh.. nama Anda", nama, ", nama yang bagus sekali.")

time.sleep(3)

thnLahir = int(input("BTW... " + nama + " kamu lahir tahun berapa? "))

time.sleep(3)

skrg = datetime.datetime.now()
usia = skrg.year - thnLahir

print("Hmmm...", nama,"kamu sudah", usia,"tahun ya..")

time.sleep(3)

if (usia > 50):
    print("Anda sudah cukup tua ya?")
    print("Jaga kesehatan ya!!")
elif (usia > 20):
    print("Ternyata Anda masih cukup muda belia")
    print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
    print("Hihihi... Anda ternyata masih ABG")
    print("Mulai berpikirlah secara dewasa ya!!")
else:
    print("Oalah.. Anda masih anak-anak toh?")
    print("Jangan suka merengek-rengek minta jajan ya!!")

time.sleep(3)

print("OK.. see you later", nama, ".. senang berkenalan denganmu")
