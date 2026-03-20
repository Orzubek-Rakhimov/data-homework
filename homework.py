# 1. Oila a'zolari (Oson)
# Bitta lug'at yarating va unda oilangiz a'zolarining ismlari (kalit) va ularning yoshini (qiymat) saqlang.
# Lug'atga yangi a'zo qo'shing.
# Biror a'zoning yoshini yangilang.
# Faqat ismlarni (kalitlarni) ekranga chiqaring.



azolar={
    "Sardor":"19 yosh",
    "Malik":"17 yosh",
    "Muslima":"14 yosh",
    "Javozir":"13 yosh"
}
azolar.update({"Yusufbek":"16 yosh"})
print(azolar["Sardor"])
print(azolar.keys())








# 2. Lug'at elementlarini yig'ish (Oson)
# Quyidagi lug'at berilgan:
# mevalar = {"olma": 5000, "banan": 20000, "nok": 15000}
# Ushbu lug'atdagi barcha narxlarning (qiymatlarning) umumiy yig'indisini hisoblaydigan kod yozing.




mevalar={
    "olma":5000,
    "banann":20000,
    "nok":15000    
}
narxlar=0

for narx in mevalar.values():
    narxlar=narxlar+narx
print(f"Xamma mevalarning narxlari :{narxlar}")









# 3. Lug'atni tekshirish (O'rtacha)
# Foydalanuvchidan biror so'z kiritishni so'rang.
# Agar u so'z lug'atda bo'lsa, uning tarjimasini yoki tavsifini chiqaring.
# Agar bo'lmasa, "Bunday so'z mavjud emas" degan xabarni chiqaring.
# (Maslahat: .get() metodidan foydalaning)




soz=input("Sozni kiriting :")
sozlar={
    "Salom":"Hello",
    "Xayr":"Bye",
    "Olma":"Apple",
    "Maktab":"School",
    "Kitob":"Book"
    
}
natija=sozlar.get(soz)
if natija:
    print(f"Sozning tarjimasi : {natija}")
else:
    print("Bunday soz topilmadi")








# 5. Lug'at ichida lug'at (O'rtacha)
# talabalar degan lug'at yarating. Unda har bir talabaning ismi kalit bo'lsin, qiymat esa boshqa bir lug'at bo'lib, unda talabaning fanlardan olgan baholari saqlansin.
# Masalan: {"Ali": {"Matematika": 5, "Tarix": 4}}
# Ma'lum bir talabaning barcha baholarini ekranga chiqaring.
# Ushbu topshiriqlardan qaysi birining kodini birgalikda tekshirishni xohlaysiz?


talabalar = {
    "Ali":
        {"Matematika":5,
         "Ona tili":5,
         "Informatika":5, 
         "Ingiliz tili":4},
    "Yusufbek": 
         {"Matematika":100,
         "Ona tili":100,
         "Informatika":100,
          "Ingiliz tili":100},
    "Javoxir":
        {"Matematika":2,
         "Ona tili":2, 
         "Informatika":2, 
         "Ingiliz tili":2},      
    "Farxod": 
        {"Matematika":4, 
         "Ona tili":4, 
         "Informatika":5, 
         "Ingiliz tili":5},
    "Said":
        {"Matematika":4,
         "Ona tili":5,
         "Informatika":4,
         "Ingiliz tili":5}
}

talaba_tanlash = input("Talabani ismini kiriting: ")
baholar=talabalar.get(talaba_tanlash)
if talaba_tanlash == "Yusufbek":
    print("Bu talaba be baxo")
elif baholar:
    print("Baholar:", baholar)
else:
    print("Bunday talaba mavjud emas")







# 6. So'zlar chastotasi (O'rtacha)
# Sizga biror matn (gap) berilgan. Masalan: "olma anor olma uzum anor olma".
# Ushbu gapdagi har bir so'z necha marta takrorlanganini hisoblovchi lug'at yarating.
# Natija quyidagicha bo'lsin: {"olma": 3, "anor": 2, "uzum": 1}.
# (Maslahat: .split() metodidan foydalanib gapni ro'yxatga aylantiring).







# 7. Lug'atni saralash (O'rtacha)
# Quyidagi mahsulotlar va ularning narxi berilgan:
# ombor = {"non": 3000, "shakar": 12000, "yog'": 18000, "tuz": 2000}
# Faqat narxi 10,000 dan baland bo'lgan mahsulotlarni ajratib olib, yangi lug'at hosil qiling.
# (Maslahat: "Dictionary Comprehension" usulini qo'llab ko'ring).


ombor={
    "non":3000,
    "shakar":12000,
    "yog":18000,
    "tuz":2000    
}
baland_narx = {}
for maxsulot in ombor:
    if ombor.get(maxsulot) > 10000:  
        baland_narx[maxsulot] = ombor.get(maxsulot)
print(baland_narx) 







# 8. Eng qimmat mahsulot (O'rtacha)
# Sizda do'kondagi mahsulotlar ro'yxati bor:
# menu = {"Osh": 25000, "Manti": 20000, "Shashlik": 15000, "Somsa": 8000}
# Lug'at ichidan eng qimmat mahsulotning ismini (kalitini) va uning narxini (qiymatini) aniqlab ekranga chiqaring.
# (Maslahat: max() funksiyasidan foydalanishingiz mumkin).









# "brand", "model", "year" kalitlari va "Ford", "Mustang", 2024 qiymatlari bilan car nomli dictionary yarating.
# "model" kalitining qiymatini ekranga chiqaring.
# Yangi kalit "color" qo‘shing va qiymatini "red" qilib belgilang.
# "brand" kalitini pop() yordamida o‘chiring.
# Yakuniy dictionary’ni ekranga chiqaring.


car={
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":"2024",
}
car.update({"Color":"Red"})
car.pop("Brand")
print(car)
