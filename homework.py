# Oson daraja (Easy)



# 1.Kvadrat hisoblovchi: Son qabul qilib, uning kvadratini konsolga chiqaruvchi funksiya yozing.

def kvadrat_aniqlovchi():
     son=float(input("Sonni kiriting : "))
     natija=son**2
     print(natija)
kvadrat_aniqlovchi()







# 2.Yosh hisoblagich: Tug'ilgan yilni qabul qilib, foydalanuvchining yoshini hisoblab beruvchi funksiya yarating.


def yosh_aniqlagich():
     tug_yil=int(input("Tug`ulgan yilingizni kiriting : "))
     xoz_yil=int(input("Xoirgi yilni kiriting : "))
     yosh=xoz_yil-tug_yil
     print(f"Siz {yosh} yoshdasiz ")
yosh_aniqlagich()






# 3.Juft yoki toq: Berilgan son juft bo'lsa True, toq bo'lsa False qaytaruvchi funksiya yozing.


def juft_toq():
     son=int(input("Son kiriting : "))
     if son %2==0:
      print(f" {son} :Bu son toq ")
     else:
          print(f"{son} :Bu son toq son")
juft_toq()





# 4.Eng kattasi: Ikkita son qabul qilib, ulardan kattasini ekranga chiqaruvchi funksiya tuzing.


def eng_katta_son():
     son1=int(input("1-Sonni kirizing : "))
     son2=int(input("2-Sonni kiriting :"))
     if son1>son2:
          print(f"{son1} : Eng katta son ")
     else:
          print(f"{son2} : Eng katta son ")
eng_katta_son()
     





# 5.Text uzunligi: Text qabul qilib, unda uzunligini chiqaruvchi (tayyor len() dan foydalanmaslikka harakat qiling).

def text_uzunligi():
    mant=input("Matnni kirgizing :")
    uzunlik=0
    for i in mant:
         uzunlik=uzunlik+1
     print(f"Matnning uznunlik soni  : {uzunlik}")
text_uzunligi()



# With len() --- Ishu bilan odam atsa bolad akan lekin.


def text_uzunligi():
     matn=input("Matnni kiriting : ")
     print(f"Matinning uzunlik soni : {len(matn)}")
text_uzunligi()





# O'rta daraja (Medium)



# Unli harflar: Matn qabul qilib, undagi unli harflar sonini hisoblab qaytaruvchi funksiya yozing.
 
def unli_harflar():
 matn = input("Matn kiriting: ")
 unlilar = "aiuoeAIUOE"
 natija = 0
 for i in matn:
    if i in unlilar:
        natija=natija+1 
 print(f"Unli harflar soni: {natija}")
unli_harflar()
     
          




# Parol tekshirgich: Parol (string) qabul qilib, uning uzunligi kamida 8 ta belgidan iboratligini tekshiruvchi funksiya yozing.

def parol_teshkirgich():
     while True:
       parol=input("Parol kiriting : ")
       if len(parol)>=8 :
          print("Siz bu parolni qoyishingiz mumkum  ")
          break
       else:
          print("Siz bu parolni qoya olmaysiz !")
parol_teshkirgich()







# Standart qiymat: Foydalanuvchi ismi so'ralsin va funksiya orqali ("Salom , {ism}) chiqarilsin!


def salomlashuvchi():
     ism=input("Ismingizni kiriting : ")
     print(f'Salom {ism}')
salomlashuvchi()







