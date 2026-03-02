
# Oson:



 # 1.	Sonning musbat, manfiy yoki nol ekanligini tekshiradigan dastur yozing.
# masala 

son=int(input("sonni kiriting :"))
if son<0:
    print(son, "siz manfiy son kiritingiz ")
else:
    print(son, "siz musbat son kiritingiz ")



   
    
    
#2	Agar yosh 18 ga teng yoki katta  bo'lsa → "Ovoz berish mumkin", aks holda "Juda yosh".

yosh=int(input("Yoshingizni kiriting :"))
if yosh>=18:
    print("Sizga ovoz berish mumkun")
else:
    print("Siz yoshlik qilasiz ")


    
 
 
    
#3 	2ta sonda eng kattasini chiqaradigan dastur yozing 

son1=float(input("1 chi sonni kiriting"))
son2=float(input("2 chi sonni kiriting"))
if son1==son2:
    print("Ikkala son teng ")
elif son1>son2:
    print("Birinchi son katta ")
else:
    print("Ikkinchi son katta ")






# 4.	Foydalanuvchining bali 50 ball teng yoki undan yuqori → “O’tdingiz”, aks holda “O’ta olmadingiz”

ball=int(input("Balingizni kiriting : "))
if ball>=50:
    print("Siz testdan otingiz ")
else:
    print("Siz testdan ota olmadingiz")




#Ortacha

 

# 1.	Foydalanuvchi 	kirizgan son 5 ga yoki 3 ga qoldiq siz bo’linadimi yo’qmi topilsin

son=int(input("Sonni kirizing :"))
if son % 5==0 and son % 3==0:
    print("Bu son 3 ga va 5 ga bolinadi ")
elif son %5==0 :
    print("Son 5 ga bolinadi :")
elif son%3==0 :
    print("Bu son 3 ga bolinadi ")
else:
    print("Sonlar 3 ga xam 5 ga xam bolinmaydi ")








# 2.	Agar tempratura 30 gradusdan katta bolsa issiq  va 15 gradusdan past bo’sa sovuq boshqa holatda iliq deb chiqarsin
 
harorat=float(input("Haroratni kirizing : "))
if harorat>=30:
    print(harorat, "Harorat issiq")
elif harorat<=15:
    print(harorat, "Harorat sovuq")
else:
    print(harorat, "Harorat iliq")







# 3.	Yil kabisa yoki kabisa yili emasligini chiqaruvchi dastur tuzing

yil=int(input("Yilni kiriting : "))
if yil % 400==0:
    print(yil , "Yil kaaiba yil !")
elif yil % 100==0:
    print(yil ,"Yil kasiba yil emas !")
elif yil % 4==0:
    print(yil, "Yil kasiba yil !")
else:
    print(yil, "Yil kaaiba yil emas !")





    
    # 4.	Berilgan raqam (1-100) orasida yotadimi yoqmi tekshirilsin

son=float(input("Son kiriting : "))
if son>0 and son<=100:
    print("Bu son 0-100 oraligida bor !")
else:
    print("Son 0-100 oraligida yoq ")





# 5.	Kalkulyator zatish ( * ,  / , + , - ): 2 sonni ustida bajariladigan ammalar;


son1=float(input("1-sonni kiriting : "))
amallar=input("Amallarni tanlang :  + , - , * , /   :" )
son2=float(input("2-sonni kiriting : "))
if amallar=="+":
     print(son1 + son2)
elif amallar=="-":
     print(son1 - son2)
elif amallar=="*":
      print(son1 * son2)
elif amallar=="/":
     if son2==0:
          print("0 ga bolish mumkun emas !")
     else:
      print(son1 / son2)
else:
     print("Bu yerda xato bolish mumkun emas siz amalni xato qilgan bolishingiz mumkun buni yasash uchun 30 minut vaqt ketti !")





# 6.	BMI natijasini chiqarish:
# Foydalanuvchi kilosi va bo’yini grizishi va vnda galib chiqib bmi chiqarish:
# yengil:  18.5 kichkina
# Normal : 18.5–24.9
# semiz: 25.0–29.9
# juda semizroq: 30.0 yoki baland 


boy=float(input("Boyingizni kiriting : "))
vazn=float(input("Vazningizni kiriting : "))
kv_boy=(boy**2)
bmi=vazn/kv_boy
print(bmi, "Bu sizning BMI natijangiz !")
if bmi<18.5 :
     print("Sizning BMI darajangiz Yengil ! ")
elif bmi>=18.5 and bmi<=24.9:
     print("Sizning BMI darajangiz Normal")
elif bmi >= 25.0 and bmi<=29.9:
     print("Sizning BMI darajangiz Semiz")
elif  bmi>=30:
     print("Sizning BMI darajangiz Juda semiz")
     
