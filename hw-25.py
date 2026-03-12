# 1. Oson bosqich: "Bozorlik ro'yxati"
# Bu bosqichda asosiy maqsad — ro'yxat yaratish va unga element qo'shishni o'rganish.
# Vazifa: bozorlik deb nomlangan bo'sh ro'yxat yarating. Unga .append() 
# yordamida kamida 4 ta mahsulot qo'shing (masalan: "Olma", "Non", "Sut", "Tuxum").
# Amal: Ro'yxatdagi ikkinchi elementni ("Non") ekranga chiqaring va oxirgi'
# ' elementni .pop() yordamida o'chirib tashlang.
# Natija: Yakuniy ro'yxatni konsolga chiqaring.

# list=[]
# list.append("Olma")
# list.append("Non")
# list.append("Sut")
# list.append("Tuxum")
# list.pop(-1)
# print(list[1],)
# print(list)







# 2. O'rta bosqich: "Saralash va Filtrlash"
# Bu bosqichda ro'yxat metodlari va sikllar (for loop) bilan ishlash talab etiladi.
# Vazifa: Ixtiyoriy 10 ta sondan iborat sonlar ro'yxatini tuzing (masalan: [12, 5, 20, 8, 15, ...]).
# Amal:
# Ro'yxatni kichigidan kattasiga qarab saralang (.sort()).
# Yangi juft_sonlar degan bo'sh ro'yxat oching.
# for sikli yordamida asosiy ro'yxatdagi faqat juft sonlarni ajratib, yangi ro'yxatga joylang.
# Natija: Ikkala ro'yxatni ham ekranga chiqaring va ularning uzunligini (len) ko'rsating.


# son=[37,29,30,12,32,4,1,9,8,99]
# juft_son=[]
# son.sort()
# for x in son:
#     if x%2==0:
#         juft_son.append(x)

# print(f"sonlar: {son}\njuft sonlar: {juft_son}")






# 1. Oson bosqich: "Ismlar filtri"
# Bu bosqichda siz ro'yxatni qidirish va o'zgartirishni mashq qilasiz.
# Vazifa: 5 ta do'stingiz ismidan iborat dustlar ro'yxatini tuzing.
# Amal:
# Foydalanuvchidan bitta ism so'rang.
# Agar bu ism ro'yxatda bo'lsa, uni o'chirib tashlang (.remove()).
# Agar ro'yxatda bo'lmasa, "Bunday ism topilmadi" deb xabar chiqaring.
# Natija: Yangilangan ro'yxatni alifbo tartibida chiqaring.


# dostlar=["anvar","quronboy","farxod","matchon","bekzod","zafar"]
# tanlov=input("ism kiriting: ")
# while tanlov not in dostlar:
#     tanlov=input("bunday ism yoq boshqa ism kiriting: ")

# else:
#     dostlar.remove(tanlov)        
# dostlar.sort()   
# print("yangilangan royhat:",dostlar)





# 2. O'rta bosqich: "Unique (Noyob) elementlar"
# Bu bosqichda siz takrorlanishlar bilan ishlashni o'rganasiz.
# Vazifa: Ichida bir xil elementlar bir necha bor qatnashgan ro'yxat yarating.
# Masalan: mevalar = ["olma", "banan", "olma", "uzum", "banan", "olcha"].
# Amal:
# Yangi bo'sh ro'yxat yarating (toza_ruyxat).
# for sikli yordamida asosiy ro'yxatni aylanib chiqing.
# Agar meva toza_ruyxat ichida yo'q bo'lsa (if item not in...), uni qo'shing.
# Natija: Faqat takrorlanmas mevalardan iborat ro'yxatni konsolga chiqaring.  
              

# mevalar=["anor","olma","uzum","anor","hurmo","uzum","banan"]
# yangi_royhat=[]
# for meva in mevalar:
#     if meva not in yangi_royhat:
#         yangi_royhat.append(meva)
# print(yangi_royhat)

    


# sayt.....
colors=["qizil","yashil","kok"]
print(colors[0])
colors[1]="sariq"
colors.append('binafsha')
colors.remove("qizil")
print(colors)



