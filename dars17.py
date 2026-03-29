                               # easy❗
# 1-mashiq 3 ga bolinadigan sonlarni chetlab otib a 13 sonida dastur tugaydi
# x=0
# while x<15:
#     x=x+1
#     if x%3==0:
#         continue
#     elif x==14:
#         break
#     print(x)

# 2-mashiq berilgan sonlardan manfiy sonlarni yoqoqtib va boshqa sonlar kopaytmasi chiqarish❗
# a=1
# while True:
#     son=int(input('sonni kiriting: '))
#     if son<0:
#         continue
#     elif son==0:
#         print("dastur toxtadi.")
#         break
#     a=a*son
# print("yig'indi:",a)

                                 #medium❗
# 3-mashiq uch urinishda qod togri yozish
# x=0
# while True:
#     qod=input("parolni kiriting: ")
#     x=x+1
#     if qod!='maxfiy':
#         print("xato to'g'ri yozing❗")
#         if x==3:
#             print("Hisob bloklandi.\nDadajon desangam foydasi yoq endi😂")
#             break
#     else:  
#         print("hush kelibsiz.")
#         break

                                 #hard❗
# 5- mashiq tub son aniqlash
# son=int(input("sonni kiriting: "))
# if son<=1:
#     print("tubson emas")
# x=2
# while x<son:
#     if son%x==0:
#         print("tub son emas")
#         break
#     x=x+1
# else:
#     print("tub son")
    
# 6 chi mashq bankaomat❗
# balans=1000
# while True:
#     if balans==0:
#             print("Hisobda pul qolmadi")
#             break
#     summa=int(input("faqat 10 ga bolinadigan sondagi summani kiriting: "))
#     if summa>1000:
#         print("mablag' yetarli emas❗")
#     elif summa%10!=0:
#         continue
#     else:
#         print("xisobingizda:",balans-summa,"USD qoldi")
#     balans=balans-summa
