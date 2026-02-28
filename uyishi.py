# 1.  Juft sonlar yig'indisi: foydalanuvchi son kirgizadi shu songa gacha bo'lgan barcha juft sonlarni qo'shib, umumiy natijani hisoblang.



son = int(input("Son kiriting: "))
yigindi = 0
for i in range(1, son + 1):

    if i % 2 == 0:
        yigindi = yigindi +i
        if son<0:
             continue
print("Juft sonlarni yigindisi : ", yigindi)







# 2.  Takrorlash: Foydalanuvchidan biror so'z va biror son (masalan, 5) kiritishni so'rang. Tsikl yordamida o'sha so'zni kiritilgan soncha marta chiqaring.
# assalom x assalom x assalom x


soz = input("So'z kiriting : ") 
son = int(input("Son kiriting : "))
print((soz+" x ")*son)


# Different type

soz=input("Sozni kirizing : ")
son=int(input("Snni kirizing :"))
for i in range(1,son+1):
     print(soz , end=" x ")








# 3.  Dollar kursi: 1 dan 10 gacha bo'lgan dollarning so'mdagi qiymatini jadval ko'rinishida chiqaring (masalan: "1 = 25200 so'm").



for i in range (1,11):
     i=i*12210
     print(i)






# 4.Dollar kursi:1 dan foydalanuvcgi kirgizgan songacha gacha bo'lgan dollarning so'mdagi qiymatini jadval ko'rinishida chiqaring (masalan: "1 = 25200 so'm").


kurs=25200
dollar=int(input("Dollrni kirizing : "))
for i in range (1,dollar+1):
     son=kurs*dollar
     print(son)





# 5.  Karra jadvali: Faqat 10 soni uchun karra jadvalini (7x1 dan 7x10 gacha) to'liq chiqaring.


for i in range(1,11):
     print("1 * ", i , "=", 1*i)
     print()
      
      
for i in range(1,11):
     print("2 * ", i , "=", 2*i)
     print( )
     
     
for i in range(1,11):
     print("3 * ", i , "=", 3*i)
     print( )
     
     
for i in range(1,11):
     print("4 * ", i , "=", 4*i)
     print( )
     
     
for i in range(1,11):
     print("5 * ", i , "=", 5*i)
     print( )
     
     
for i in range(1,11):
     print("6 * ", i , "=", 6*i)
     print( )



for i in range(1,11):
     print("7 * ", i , "=", 7*i)
     print( )
     
     
     
for i in range(1,11):
     print("8 * ", i , "=", 8*i)
     print( )
     
     
for i in range(1,11):
     print("9 * ", i , "=", 9*i)
     print( )
     
     
for i in range(1,11):
     print("10 * ", i , "=", 10*i)
     print( )




# Different type:

for i in range (1,11):
  for x in range(1,11):
       print(i ,"*" ,x, "=", i*x)
       print()




# 1.  Salom, Dunyo!: Ekranga "Men Pythonni o'rganyapman" jumlasini tsikl orqali 20 marta chiqaring. (13 siklda chiqarmasn va 19 siklda toxtatsin)

chiqish=str("Men pythonni organayapman")
for i in range(1,21):
     if i==13:
          continue
     if i==19:
          break
     print(chiqish)






# 2.  Sonlarni o'tkazib yuborish: 1 dan 100 gacha bo'lgan sonlarni chiqaring, lekin 5 ga bo'linadigan sonlar kelganda ularni tashlab o'tib keting (continue ishlating)

for i in range (1,101):
     if i%5==0:
          continue
     print(i)




# 3.  Koordinatalar: 2 ta son so’rimiz va shu sonlar gacha bo'lgan x va y o'qlari uchun barcha nuqtalarni chiqaring (masalan: (0,0), (0,1), (0,2)...).
# (nested loop) (2 forni bir birini ichida ishlatish)




x=int(input("1-sonni kiriting : "))
y=int(input("2-sonni kiriting : "))
for i in range(0,x+1):
     for j in range (0,y+1):
      print(i , j)
     
 


     
# 1.    Hard:
# Matritsa: 3x3 o'lchamdagi matritsani (ro'yxat ichidagi ro'yxat) ekranga chiroyli shaklda chiqaring.




# 20-dars uyga vazifa



