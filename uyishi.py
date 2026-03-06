# 1.Berilgan gapdagi barcha raqamlarni olib tashlang, faqat harflar qolsin.


matn=input("Raqamli matn kiriting : ")
natija=""
for i in matn:
         if i not in "0123456789":
              natija=natija+i   
print(natija) 





# 2.Foydalanuvchi kiritgan so‘z palindrom ekanligini tekshiring.

soz = input("So'z kiriting: ")
teskari = ""
for i in soz:
    teskari = i + teskari 
if soz == teskari:
    print("Bu so'z palimdron !")
else:
    print("Bu so'z palindrom emas.")





# 3. Matndagi ortiqcha bo‘shliqlarni bittaga aylantiring. ("Assalom    aleykum  aasda" => "Assalom aleykum aasda")


# Can`t do it (







# 4. So‘zlar ichidagi unli harflarni “*” belgisi bilan almashtiring.

mant=input("Biror bir soz yoki matn kiriting : ")
natija="*"
for i in mant:
     if i  in("aueioAUEIO"):
      natija=natija +'*'          
     else :
          natija=natija+i
print(natija)








# 5. Berilgan gapdagi so‘zlarni teskari tartibda joylashtiring, lekin har bir so‘z o'rni o‘zgarishsiz qolsin.
# Masalan:
  # "Assalom aleykum yurtdoshim"
  # "mishodtruy mukyela molassA" => xato bunday emas
  # "molassA mukyela mishodtruy" => to'gri


