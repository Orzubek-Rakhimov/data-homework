                        #    Oson daraja (Easy)
# 1.Kvadrat hisoblovchi: Son qabul qilib, uning kvadratini konsolga chiqaruvchi funksiya yozing.

# def kvDastur(son):
#     print(f"{son} ni kvadrati: {son*son}")
# kvDastur(son=int(input("sonni kiriting: ")))


# 2.Yosh hisoblagich: Tug'ilgan yilni qabul qilib, 
# foydalanuvchining yoshini hisoblab beruvchi funksiya yarating.

# def yoshHisoblagich(yil):
#     print(f"siz {2026-yil} yoshda siz")
# yoshHisoblagich(yil=int(input("qaysi qilda tug'ilgan siz: ")))


# 3.Juft yoki toq: Berilgan son juft bo'lsa True, toq bo'lsa False qaytaruvchi funksiya yozing.

# def Juft_OR_Toq(son):
#     if son%2==0:
#         print(True)
#     else:
#         print(False)
# Juft_OR_Toq(son=int(input("sonni kiriting: ")))

# 4.Eng kattasi: Ikkita son qabul qilib, ulardan kattasini ekranga chiqaruvchi funksiya tuzing.

# def KattaSon(son1,son2):
#     if son1>son2:
#         print("eng katta son:",son1)
#     else:
#         print("eng katta son:",son2)
# KattaSon(son1=float(input("1-son: ")),son2=float(input("2-son: ")))



# 5.Text uzunligi: Text qabul qilib, unda uzunligini 
# chiqaruvchi (tayyor len() dan foydalanmaslikka harakat qiling).

# def txt_uzunlik(text):
#     x=0
#     for harf in text:
#         x=x+1
#     print("text uzunliki:",x)
# txt_uzunlik(text=input("yozing: "))


                            #   O'rta daraja (Medium)
# 6.Unli harflar: Matn qabul qilib, undagi unli harflar sonini hisoblab qaytaruvchi funksiya yozing.

# def Unli_harf_soni(matn):
#     soni=0
#     for harf in matn:
#         if harf in "auieoAEIUO":
#             soni=soni+1
#     print("unli hariflar soni:",soni)
# Unli_harf_soni(matn=input("matinni kiriting: "))


# 7.Parol tekshirgich: Parol (string) qabul qilib, uning uzunligi 
# kamida 8 ta belgidan iboratligini tekshiruvchi funksiya yozing. 

# def Parol_yaratish(parol):

#     while True:
#         parol=input("eng kami 8 ta belgidan iborat parolyarating.\n⇨  : ")
#         if len(parol)>=8:
#             print("parol mufaqiyatli o'rnatildi.") 
#             break
# Parol_yaratish(parol=input("eng kami 8 ta belgidan iborat parolyarating.\n⇨  :"))


# 8.Standart qiymat: Foydalanuvchi ismi so'ralsin va funksiya orqali ("Salom , {ism}) chiqarilsin!
   
# def salom_ism(ism):
#     print(f"salom {ism.title()}")
# salom_ism(ism=input("ismingiz: "))