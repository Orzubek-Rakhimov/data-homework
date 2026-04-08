# Dictionary

# car={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":2024,
# }
# print(car["model"])
# car.update({
#     "color":"red"
# })
# car.pop("brand")
# print(car)



# 1. Oila a'zolari (Oson)
# Bitta lug'at yarating va unda oilangiz a'zolarining ismlari (kalit) va ularning yoshini (qiymat) saqlang.
# Lug'atga yangi a'zo qo'shing.
# Biror a'zoning yoshini yangilang.
# Faqat ismlarni (kalitlarni) ekranga chiqaring.

# l={
#     "axmed":20,
#     "akbar":30,
#     "akmal":40
# }
# l["Aziz"]=10
# l["akbar"]=15
# print(l.keys())


# 2. Lug'at elementlarini yig'ish (Oson)
# Quyidagi lug'at berilgan:
# mevalar = {"olma": 5000, "banan": 20000, "nok": 15000}
# Ushbu lug'atdagi barcha narxlarning (qiymatlarning) umumiy yig'indisini hisoblaydigan kod yozing.

# mevalar = {"olma": 5000, "banan": 20000, "nok": 15000}

# h = 0
# for narx in mevalar.values():
#     h += narx
# print("Umumiy yig'indi:", h)


# 3. Lug'atni tekshirish (O'rtacha)
# Foydalanuvchidan biror so'z kiritishni so'rang.
# Agar u so'z lug'atda bo'lsa, uning tarjimasini yoki tavsifini chiqaring.
# Agar bo'lmasa, "Bunday so'z mavjud emas" degan xabarni chiqaring.
# (Maslahat: .get() metodidan foydalaning)

# lugat={
#     "Hello"
# }
# soz=input("Biror so'z kiriting: ")
# if soz in lugat:
#     print("Bu sozning manosi: Salom")
# else:
#     print("Bunday so'z mavjud emas!")


# 5. Lug'at ichida lug'at (O'rtacha)
# talabalar degan lug'at yarating. Unda har bir talabaning ismi kalit bo'lsin, qiymat esa boshqa bir lug'at bo'lib, unda talabaning fanlardan olgan baholari saqlansin.
# Masalan: {"Ali": {"Matematika": 5, "Tarix": 4}}
# Ma'lum bir talabaning barcha baholarini ekranga chiqaring.
# Ushbu topshiriqlardan qaysi birining kodini birgalikda tekshirishni xohlaysiz?

# talabalar={
#     "Ali": {
#         "Matematika": 5,
#         "Tarix": 4,
#         "Adabiyot": 4,
#         "Fizika": 5
#     },
#     "Vali": {
#         "Matematika": 2,
#         "Tarix": 2,
#         "Adabiyot": 5,
#         "Fizika": 2
#     },
#     "Aziz": {
#         "Matematika": 5,
#         "Tarix": 4,
#         "Adabiyot": 3,
#         "Fizika": 5,
#     }
# }
# print(talabalar["Ali"])


# 6. So'zlar chastotasi (O'rtacha)
# Sizga biror matn (gap) berilgan. Masalan: "olma anor olma uzum anor olma".
# Ushbu gapdagi har bir so'z necha marta takrorlanganini hisoblovchi lug'at yarating.
# Natija quyidagicha bo'lsin: {"olma": 3, "anor": 2, "uzum": 1}.
# (Maslahat: .split() metodidan foydalanib gapni ro'yxatga aylantiring).

# gap="olma anor olma uzum anor olma"
# a=gap.split()
# yignd = {}

# for soz in a:
#     if soz in yignd:
#         yignd[soz] += 1
#     else:
#         yignd[soz] = 1

# print(yignd)


# 7. Lug'atni saralash (O'rtacha)
# Quyidagi mahsulotlar va ularning narxi berilgan:
# ombor = {"non": 3000, "shakar": 12000, "yog'": 18000, "tuz": 2000}
# Faqat narxi 10,000 dan baland bo'lgan mahsulotlarni ajratib olib, yangi lug'at hosil qiling.
# (Maslahat: "Dictionary Comprehension" usulini qo'llab ko'ring).

# ombor = {"non": 3000, "shakar": 12000, "yog'": 18000, "tuz": 2000}
# newd={}

# for kalit in ombor:
#     if ombor[kalit] > 10000:
#         newd[kalit] = ombor[kalit]

# print(newd)


# 8. Eng qimmat mahsulot (O'rtacha)
# Sizda do'kondagi mahsulotlar ro'yxati bor:
# menu = {"Osh": 25000, "Manti": 20000, "Shashlik": 15000, "Somsa": 8000}
# Lug'at ichidan eng qimmat mahsulotning ismini (kalitini) va uning narxini (qiymatini) aniqlab ekranga chiqaring.
# (Maslahat: max() funksiyasidan foydalanishingiz mumkin).

# MAX OTMADIK!
