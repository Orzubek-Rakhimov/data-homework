# Oson
# 1. Kvadratlar jadvali: 1 dan 20 gacha bo'lgan sonlarning kvadratini (i**2) ekranga jadval ko'rinishida chiqaring.
# for i in range(1,21,1):
#     print(i**2)

# 2. Foydalanuvchidan son so'raymiz va shu sondan 1 ga cha bolgan sonlarni chiqaramiz ( 100 => 100,99,98 ....1) ( 5 => 5,4,3,2,1)
# a=int(input("Sonni kiriting: "))
# for i in range(a,0,-1):
#     print(i)

# O'rtacha
# 3.  Foydalanuvchidan son so'ralsi9n va shu sonni 1 dan 10 gacha ko'paytmasi chiqarilsin ( 5 => 5 * 1 = 5, 5 * 2 = 10 , 15,20 .... 45,50) ( 7 => 7,14,21,28 ... 63,70)
# a=int(input("Sonni kiriting: "))
# for i in range(1,11,1):
#     print(a*i)

# 4.   Faktorialni topish: Berilgan musbat butun sonning faktorialini (masalan, 5! = 1*2*3*4*5) for yordamida hisoblaydigan dastur tuzing
# a=int(input("Sonni kiriting: "))
# f=1
# for i in range(1,a+1,1):
#     f=f*i
# print(f)

# Qiyin
# 5. Tub sonlarni aniqlash: 1 dan 100 gacha bo'lgan oraliqdagi barcha tub sonlarni (faqat o'ziga va 1 ga bo'linadigan sonlar) topib chiqaring  (2,3,5,7 ... 97)
# a=0
# for i in range(1,101,1):
#     if i%i==0 and i%1==0:
#         print("tubson:",i)
#     a=a+1


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
# a=int(input("Yulduzlar sonini kiriting: "))
# for i in range(1,a,1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
