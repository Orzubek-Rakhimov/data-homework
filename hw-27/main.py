# 1. Oila a'zolari (Oson)
# Bitta lug'at yarating va unda oilangiz a'zolarining ismlari (kalit) va ularning yoshini (qiymat) saqlang.
# Lug'atga yangi a'zo qo'shing.
# Biror a'zoning yoshini yangilang.
# Faqat ismlarni (kalitlarni) ekranga chiqaring.

# oila={
#     "Jushqin":45,
#     "Me":20
# }
# oila["Avazbek"]=23
# oila.update({"Me":"21"})

# for oila_malumoti in oila:
#     print(oila_malumoti)




#2. Lug'at elementlarini yig'ish (Oson)
# Quyidagi lug'at berilgan:
# mevalar = {"olma": 5000, "banan": 20000, "nok": 15000}
# Ushbu lug'atdagi barcha narxlarning (qiymatlarning) umumiy yig'indisini hisoblaydigan kod yozing.



# mevalar={
#    "olma": 5000,
#    "banan": 20000,
#     "nok": 15000
# }
# meva=0
# for mevalar_key in mevalar:
#     meva=meva+mevalar[mevalar_key]
# print(meva)




# 3. Lug'atni tekshirish (O'rtacha)
# Foydalanuvchidan biror so'z kiritishni so'rang.
# Agar u so'z lug'atda bo'lsa, uning tarjimasini yoki tavsifini chiqaring.
# Agar bo'lmasa, "Bunday so'z mavjud emas" degan xabarni chiqaring.
# (Maslahat: .get() metodidan foydalaning)


# user=input("Soz kiriting: ")

# lugat={
#     "apple":"olma",
#     "car":"mashina",
#     "eagle":"burgut",
#     "Prince":"Neymar"
# }

# print(lugat.get(user,"Bunday soz mavjud emas"))







# 5. Lug'at ichida lug'at (O'rtacha)
# talabalar degan lug'at yarating. Unda har bir talabaning ismi kalit bo'lsin, 
# qiymat esa boshqa bir lug'at bo'lib, unda talabaning fanlardan olgan baholari saqlansin.
# Masalan: {"Ali": {"Matematika": 5, "Tarix": 4}}
# Ma'lum bir talabaning barcha baholarini ekranga chiqaring.
# Ushbu topshiriqlardan qaysi birining kodini birgalikda tekshirishni xohlaysiz?


# talaba=input("Talabaning ismini kiriting: ")

# talabalar={
#     "Alex":{
#         "Math":3,
#         "History":5,
#         "Geography":4,
#         "English language":3
#     },
#     "Max":{
#         "Math":5,
#         "History":4,
#         "Geography":2,
#         "English language":4
#     },
#     "Sarah":{
#         "Math":4,
#         "History":4,
#         "Geography":5,
#         "English language":5

#     }
# }


# print(talabalar.get(talaba,"Bunday talaba yoq"))







# 6. So'zlar chastotasi (O'rtacha)
# Sizga biror matn (gap) berilgan. Masalan: "olma anor olma uzum anor olma".
# Ushbu gapdagi har bir so'z necha marta takrorlanganini hisoblovchi lug'at yarating.
# Natija quyidagicha bo'lsin: {"olma": 3, "anor": 2, "uzum": 1}.
# (Maslahat: .split() metodidan foydalanib gapni ro'yxatga aylantiring).









# gap = input("Matn kiriting: ")
# sozlar = gap.split()

# natija = {}

# for soz in sozlar:
#     if soz in natija:
#         natija[soz]=natija[soz]+1
#     else:
#         natija[soz]=1
# print(natija)







# 7. Lug'atni saralash (O'rtacha)
# Quyidagi mahsulotlar va ularning narxi berilgan:
# ombor = {"non": 3000, "shakar": 12000, "yog'": 18000, "tuz": 2000}
# Faqat narxi 10,000 dan baland bo'lgan mahsulotlarni ajratib olib, yangi lug'at hosil qiling.
# (Maslahat: "Dictionary Comprehension" usulini qo'llab ko'ring).





# ombor = {"non": 3000, "shakar": 12000, "yog'": 18000, "tuz": 2000}

# yangi = {}

# for kalit, qiymat in ombor.items():
#     if qiymat > 10000:
#         yangi[kalit] = qiymat

# print(yangi)









# 8. Eng qimmat mahsulot (O'rtacha)
# Sizda do'kondagi mahsulotlar ro'yxati bor:
# menu = {"Osh": 25000, "Manti": 20000, "Shashlik": 15000, "Somsa": 8000}
# Lug'at ichidan eng qimmat mahsulotning ismini (kalitini) va uning narxini (qiymatini) aniqlab ekranga chiqaring.
# (Maslahat: max() funksiyasidan foydalanishingiz mumkin).



# menu = {
#     "Osh": 25000,
#     "Manti": 20000,
#     "Shashlik": 15000,
#     "Somsa": 8000
# }

# eng_qimmat=max(menu, key=menu.get)
# print("Eng qimmat mahsulot:",eng_qimmat)
# print("Narxi:",menu[eng_qimmat])
