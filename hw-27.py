# 1. Oila a'zolari (Oson)
# Bitta lug'at yarating va unda oilangiz a'zolarining ismlari (kalit)
# va ularning yoshini (qiymat) saqlang.
# Lug'atga yangi a'zo qo'shing.
# Biror a'zoning yoshini yangilang.
# Faqat ismlarni (kalitlarni) ekranga chiqaring.


# oila_azolar=dict(Sobiryoz=53,
#                  Nargiza=46,
#                  Shaxnoza=27,
#                  Shirin=23,
#                  Farxod=17)
# oila_azolar.update({"Aziza":11,"Farxod":18})
# print(oila_azolar.keys())

# 2. Lug'at elementlarini yig'ish (Oson)
# Quyidagi lug'at berilgan:
# mevalar = {"olma": 5000, "banan": 20000, "nok": 15000}
# Ushbu lug'atdagi barcha narxlarning (qiymatlarning) umumiy yig'indisini hisoblaydigan kod yozing.
# 
# 
# yigindi=0
# mevalar = dict(olma=5000,
#                banan=20000,
#                nok=15000) 
# for narx in mevalar:
#     yigindi=yigindi+mevalar[narx]
# print(yigindi)


# 3. Lug'atni tekshirish (O'rtacha)
# Foydalanuvchidan biror so'z kiritishni so'rang.
# Agar u so'z lug'atda bo'lsa, uning tarjimasini yoki tavsifini chiqaring.
# Agar bo'lmasa, "Bunday so'z mavjud emas" degan xabarni chiqaring.
# (Maslahat: .get() metodidan foydalaning)

# sozlar=dict(bir=1,ikki=2,uch=3,tort=4,besh=5)
# soz=input("soz kiriting: ").strip().lower()
# if soz in sozlar:
#     print(sozlar[soz])
# else:
#     print("bunday soz mavjud emas")



# 5. Lug'at ichida lug'at (O'rtacha)
# talabalar degan lug'at yarating. Unda har bir talabaning ismi kalit bo'lsin, 
# qiymat esa boshqa bir lug'at bo'lib, unda talabaning fanlardan olgan baholari saqlansin.
# Masalan: {"Ali": {"Matematika": 5, "Tarix": 4}}
# Ma'lum bir talabaning barcha baholarini ekranga chiqaring.
# Ushbu topshiriqlardan qaysi birining kodini birgalikda tekshirishni xohlaysiz?

# talabalar={
#     "ali":{ "matematika": 5,"ingliz": 4,"informatika": 5},
#     "vali":{"matematika": 3, "ingliz": 4, "informatika":4, },
#     "hasan":{"matematika":5,"ingliz":5,"informatika":5}
#     }
# talaba_nomi=input("talaba nomini kiriting: ").strip().lower()
# print(talabalar[talaba_nomi])


# 6. So'zlar chastotasi (O'rtacha)
# Sizga biror matn (gap) berilgan. Masalan: "olma anor olma uzum anor olma".
# Ushbu gapdagi har bir so'z necha marta takrorlanganini hisoblovchi lug'at yarating.
# Natija quyidagicha bo'lsin: {"olma": 3, "anor": 2, "uzum": 1}.
# (Maslahat: .split() metodidan foydalanib gapni ro'yxatga aylantiring).
# maxsulotlar={}
# royhat="olma anor olma uzum anor olma"
# royhat=royhat.split()
# for mahsulot in royhat:
#     if mahsulot not in maxsulotlar:
#         maxsulotlar.update({mahsulot:royhat.count(mahsulot)})
# print(maxsulotlar)



# 7. Lug'atni saralash (O'rtacha)
# Quyidagi mahsulotlar va ularning narxi berilgan:
# ombor = {"non": 3000, "shakar": 12000, "yog'": 18000, "tuz": 2000}
# Faqat narxi 10,000 dan baland bo'lgan mahsulotlarni ajratib olib, yangi lug'at hosil qiling.
# (Maslahat: "Dictionary Comprehension" usulini qo'llab ko'ring).
# yangi_ombor={}
# ombor = {"non": 3000, "shakar": 12000, "yog'": 18000, "tuz": 2000}
# for max in ombor:
#     if ombor[max]>10000:
#         yangi_ombor.update({max:ombor[max]})
# print(yangi_ombor)



# 8. Eng qimmat mahsulot (O'rtacha)
# Sizda do'kondagi mahsulotlar ro'yxati bor:
# menu = {"Osh": 25000, "Manti": 20000, "Shashlik": 15000, "Somsa": 8000}
# Lug'at ichidan eng qimmat mahsulotning ismini (kalitini) 
# va uning narxini (qiymatini) aniqlab ekranga chiqaring.
# (Maslahat: max() funksiyasidan foydalanishingiz mumkin).


# menu = {"Osh": 25000, "Manti": 20000, "Shashlik": 15000, "Somsa": 8000}
# narx=max(menu.values())
# for ovqat in menu:
#     if menu[ovqat]== narx:
#         print(f"eng qimmat ovqat: {ovqat}={narx}")