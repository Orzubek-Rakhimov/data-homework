# Oson
# 1. Kvadratlar jadvali: 1 dan 20 gacha bo'lgan sonlarning kvadratini (i**2) ekranga jadval ko'rinishida chiqaring.


for i in range(1,21):
     print (i)
     i=i**2
print(i)











# 2. Foydalanuvchidan son so'raymiz va shu sondan 1 ga cha bolgan sonlarni chiqaramiz ( 100 => 100,99,98 ....1) ( 5 => 5,4,3,2,1)



son=int(input("Son kiriting :"))
for i in range(son,0,-1):
     print(i)








# O'rtacha


# 3.  Foydalanuvchidan son so'ralsi9n va shu sonni 1 dan 10 gacha ko'paytmasi chiqarilsin ( 5 => 5 * 1 = 5, 5 * 2 = 10 , 15,20 .... 45,50) ( 7 => 7,14,21,28 ... 63,70)

son=int(input("Sonni kirgizing :"))
for i in range(1,11):
     i=son*i
     print(i)















# 4.   Faktorialni topish: Berilgan musbat butun sonning faktorialini (masalan, 5! = 1*2*3*4*5) for yordamida hisoblaydigan dastur tuzing 

son=int(input("Sonni kiriting :"))
n=1
for i in range (1,son+1):
     n=n*i
     print(n)












# Qiyin


# 5. Tub sonlarni aniqlash: 1 dan 100 gacha bo'lgan oraliqdagi barcha tub sonlarni (faqat o'ziga va 1 ga bo'linadigan sonlar) topib chiqaring  (2,3,5,7 ... 97)















# 6. Yulduzchali piramida: Ichma-ich tsikllar yordamida quyidagi shaklni hosil qiling (int)
# => (5)
# *
# **
# ***
# ****
# *****
# => (6)
# *
# **
# ***
# ****
# *****
# ******

