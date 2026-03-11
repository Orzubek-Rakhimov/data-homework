# 1.Ism-sharif: toliq_ism funksiyasini yarating. U ism va familiya qabul qilsin,
# lekin familiya kiritilmasa, u standart bo'sh matn "" bo'lsin. Funksiya birlashtirilgan matnni qaytarsin.



# def toliq_ism(ism, familiya=""):
#     return ism+familiya


# natija = toliq_ism("Yusufbek")

# print(natija)











# 2.Valyuta konvertori: kurs_hisobla funksiyasi miqdor va kurs (standart qiymati 12600) qabul qilsin.
# Funksiya so'mga aylantirilgan qiymatni qaytarsin.



def kurs_hisobla(miqdor, kurs=12600):
    return miqdor * kurs


dollar = int(input("Dollarni kiriting : "))
som = kurs_hisobla(dollar)
print(f"{dollar} AQSh dollari = {som} so'm")




#3.Do'kon cheki: hisob_kitob funksiyasi mahsulot, narh, soni va chegirma (standart 0) parametrlarini qabul qilsin.
#Argumentlarni uzatishda ularning tartibini aralashtirib yuboring (masalan, birinchi chegirma, keyin mahsulot). 
# Funksiya jami summani matn ko'rinishida qaytarsin.



