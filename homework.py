# 1. Oson bosqich: "Bozorlik ro'yxati"
# Bu bosqichda asosiy maqsad — ro'yxat yaratish va unga element qo'shishni o'rganish.
# Vazifa: bozorlik deb nomlangan bo'sh ro'yxat yarating. Unga .append() yordamida kamida 4 ta mahsulot qo'shing (masalan: "Olma", "Non", "Sut", "Tuxum").
# Amal: Ro'yxatdagi ikkinchi elementni ("Non") ekranga chiqaring va oxirgi elementni .pop() yordamida o'chirib tashlang.
# Natija: Yakuniy ro'yxatni konsolga chiqaring.



bozorlik_royxati=[]
bozorlik_royxati.append("Olma")
bozorlik_royxati.append("Non")
bozorlik_royxati.append("Sut")
bozorlik_royxati.append("Tuxum")
print( f"Ikinchi maxsulot: {bozorlik_royxati[1]}")
bozorlik_royxati.pop()
print(f"Sotib olinishi kerak bolgan maxsulotlar:{bozorlik_royxati}")








# 2. O'rta bosqich: "Saralash va Filtrlash"
# Bu bosqichda ro'yxat metodlari va sikllar (for loop) bilan ishlash talab etiladi.
# Vazifa: Ixtiyoriy 10 ta sondan iborat sonlar ro'yxatini tuzing (masalan: [12, 5, 20, 8, 15, ...]).
# Amal:
# Ro'yxatni kichigidan kattasiga qarab saralang (.sort()).
# Yangi juft_sonlar degan bo'sh ro'yxat oching.
# for sikli yordamida asosiy ro'yxatdagi faqat juft sonlarni ajratib, yangi ro'yxatga joylang.
# Natija: Ikkala ro'yxatni ham ekranga chiqaring va ularning uzunligini (len) ko'rsating.




sonlar=[10,13,14,18,88,985,2,33,91,1013]
sonlar.sort()
print(f"Sonlarning kichikdan kattayishi : {sonlar}")
juft_sonlar=[]
for i in sonlar:
    if i%2==0:
     juft_sonlar.append(i)
print(f"Xamma kiritilgam sonlar : {sonlar}")
print(f"Kiritilgam juft  sonlar : {juft_sonlar}")
print(f"Xamma kiritilgam sonlarning uzunligi : {len(sonlar)}")
print(f"Kiritilgam juft  sonlarning uzunligi   : {len(juft_sonlar)}")

        







# 1. Oson bosqich: "Ismlar filtri"
# Bu bosqichda siz ro'yxatni qidirish va o'zgartirishni mashq qilasiz.
# Vazifa: 5 ta do'stingiz ismidan iborat dustlar ro'yxatini tuzing.
# Amal:
# Foydalanuvchidan bitta ism so'rang.
# Agar bu ism ro'yxatda bo'lsa, uni o'chirib tashlang (.remove()).
# Agar ro'yxatda bo'lmasa, "Bunday ism topilmadi" deb xabar chiqaring.
# Natija: Yangilangan ro'yxatni alifbo tartibida chiqaring.




ismlar=["Said","Javoxir", "Farux" , "Bexruz", "Arsen"]
ism=input("Qidirmoqchi bolgan ismingizni kiriting : ")
if ism in ismlar:
    ismlar.remove(ism)
elif ism not in ismlar:
    print("Bunday natija topilmadi")
ismlar.sort()
print(ismlar)





# 2. O'rta bosqich: "Unique (Noyob) elementlar"
# Bu bosqichda siz takrorlanishlar bilan ishlashni o'rganasiz.
# Vazifa: Ichida bir xil elementlar bir necha bor qatnashgan ro'yxat yarating. Masalan: mevalar = ["olma", "banan", "olma", "uzum", "banan", "olcha"].
# Amal:
# Yangi bo'sh ro'yxat yarating (toza_ruyxat).
# for sikli yordamida asosiy ro'yxatni aylanib chiqing.
# Agar meva toza_ruyxat ichida yo'q bo'lsa (if item not in...), uni qo'shing.
# Natija: Faqat takrorlanmas mevalardan iborat ro'yxatni konsolga chiqaring.



mevalar=["Olma","Banan", "Olma","Uzum", "Banan","Ananas"]
yangi_royxat=[]
for i in mevalar:
    if i not in yangi_royxat:
        yangi_royxat.append(i)
print(yangi_royxat)






# 1 "red", "green", "blue" qiymatlari bilan colors nomli ro‘yxat yarating.
# 2 Ro‘yxatdagi birinchi elementni ekranga chiqaring.
# 3 Ikkinchi elementni "yellow" ga o‘zgartiring.
# 4 .append() yordamida "purple" ni ro‘yxat oxiriga qo‘shing.
# 5 .remove() yordamida "red" ni ro‘yxatdan o‘chiring.
# 6 Yakuniy ro‘yxatni ekranga chiqaring.

ranglar=["Red", "Green", "Blue"]
print(f" Birinchi rang {ranglar[0]}")
ranglar[1]="Yellow"
ranglar.append("Purple")
ranglar.remove("Red")
print(ranglar)




