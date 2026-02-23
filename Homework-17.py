 
 
 
 
 #Easy (Oson - Mantiqni mustahkamlash)
# 1. Sonlarni sakrab o'tish
# 1 dan 15 gacha sanaydigan sikl yozing.
# Agar son 3 ga bo‘linadigan bo‘lsa, uni ekranga chiqarmasdan tashlab o'ting (continue).
# Agar son 13 ga yetsa, siklni butunlay to'xtating (break).

son=0
while son<=15:
     son=son+1
     if son%3==0:
          continue
     elif son==13:
          break
     print(son)












# 2. Faqat musbat sonlar yig'indisi
# Foydalanuvchidan sonlar kiritishni so'raydigan dastur tuzing.
# Agar foydalanuvchi manfiy son kiritsa, uni hisobga olmang (continue).
# Agar foydalanuvchi 0 kiritsa, siklni to'xtating (break) va yakuniy yig'indini ekranga chiqaring.
# Medium (O‘rtacha - Jarayonni boshqarish)

yigindi=0
while True:
     son=float(input("Sonni kiriting "))
     if son<0:
          continue
          
     elif son==0:
          break
     yigindi=yigindi + son   
print(yigindi,"Musbat son;arni yigindisi ")
      
          







# 3. Login urinishlari chegarasi
# Tizimga kirish dasturini simulyatsiya qiling. To'g'ri parol: "maxfiy".
# Foydalanuvchiga jami 3 ta urinish bering.
# Agar parol to'g'ri topilsa, "Xush kelibsiz" deb chiqaring va break orqali to'xtating.
# Agar 3 marta xato kiritilsa, "Hisob bloklandi" deb chiqaring.




parol = "manfiy"
urinish = 3

while urinish > 0:
    paroll = input("Parolni kiriting: ")
    if paroll == parol:
        print("Xush kelibsiz ")
        break
    urinish = urinish-1    
    if urinish > 0:
        print("Parol noto'g'riy ana urinib koring :")
    else:
        print("Hisob bloklandi.")
     







# 6. Aqlli Bankomat
# Dastlabki balansda 1000 unit pul bor. Foydalanuvchidan qancha pul yechishni so'rang.
# Agar so'ralgan summa balansdan ko'p bo'lsa, "Mablag' yetarli emas" deb chiqaring va continue yordamida qayta so'rang.
# Agar foydalanuvchi "quit" deb yozsa yoki balans 0 ga tushib qolsa, siklni to'xtating.
# Faqat 10 ga bo'linadigan summalarni yechishga ruxsat bering, aks holda "Faqat 10 ga karrali summa kiriting" deb qaytaring.


balans = 1000
toxtatish = "quit"

while True:
    foydalanuvchining_kiritishi = input("Kartangizdagi yechmoqchi bolgan pulni kiriting yoki quit: ")
    
    if foydalanuvchining_kiritishi == toxtatish:  # quit yozilgan bo‘lsa
        print("Sizning operatsiyangiz yakunlandi.")
        break
    foydalanuvchining_balans = float(foydalanuvchining_kiritishi)  # faqat quit bo‘lmagan holatda float
    if foydalanuvchining_balans % 10 != 0:
        print("Faqat 10 ga karrali summa kiriting!")
        continue
    if foydalanuvchining_balans > balans:
        print("Sizning kartangizdagi kamlik qiladi :")
        continue
    balans =balans-foydalanuvchining_balans
    print("Muvafqyatli yechildi", balans)
    if balans == 0:
        print("Balans tugadi." ,balans)
        break

     








