# 1.Berilgan gapdagi barcha raqamlarni olib tashlang, faqat harflar qolsin.
# a=input("Gapni kiriting: ")
# b = ""
# for x in a:
#     if x not in "0123456789":
#         b = b+x
# print(b)

# 2.Foydalanuvchi kiritgan so‘z palindrom ekanligini tekshiring.
# ---

# 3. Matndagi ortiqcha bo‘shliqlarni bittaga aylantiring. ("Assalom    aleykum  aasda" => "Assalom aleykum aasda")
# a=input("Gapni kiriting: ")
# b = a.split()
# n=""
# for i in b:
#     n=n+(i+" ")
# print(n)

# 4. So‘zlar ichidagi unli harflarni “*” belgisi bilan almashtiring.
# a=input("Sozlarnni kiriting: ")
# u="uioeaUIOEA"
# n=""
# for i in a:
#     if i in u:
#         n+="*"
#     else:
#         n+=i
# print(n)
# 5. Berilgan gapdagi so‘zlarni teskari tartibda joylashtiring, lekin har bir so‘z o'rni o‘zgarishsiz qolsin.
# Masalan:
   # "Assalom aleykum yurtdoshim"
   # "mishodtruy mukyela molassA" => xato bunday emas
   # "molassA mukyela mishodtruy" => to'gri
# a=input("Sozlarnni kiriting: ")
# c=""
# for i in a:
#     c=i+c
# print(c)
