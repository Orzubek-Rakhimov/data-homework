# 1.Foydalanuvchi login kiritayotganda tasodifan boshiga yoki oxiriga bo'sh joy (space) tashlab ketsa, bu xatoni qanday bartaraf etasiz?
# "***Python***" satridagi yulduzchalarni olib tashlab, faqat so'zning o'zini qoldirish uchun ushbu metoddan qanday foydalaniladi?

# gap=input("login: ")
# x=gap.replace("*"," ")
# print(x.strip())


# 2.1 Berilgan gapdagi barcha nuqtalarni vergulga almashtiruvchi kod yozing.
# 2.2 Satr ichidagi bo'sh joylarni (probel) butunlay olib tashlash (ya'ni ""
#     ga almashtirish) uchun bu metodni qanday qo'llaysiz?

# x=""
# soz=input("gapni yozing: ")
# for i in soz:
#     if i==" ":
#         continue
#     x=x+i
# print(x.replace(".",","))


# 3.1 Matn ichida "Python" so'zi necha marta takrorlanganini aniqlang.
# 3.2 Satrdagi unli harflar (masalan, 'a') sonini hisoblashda ushbu metoddan qanday foydalaniladi?

# 
# u=0
# matin=input("yozing: ")

# print(f"python sozi:{matin.lower().count("python")}")
# print("u harfi:", matin.lower().count("u"),"ta")
# print("o va o'harflarii:", matin.lower().count("o"),"ta")
# print("e harfi:", matin.lower().count("e"),"ta")
# print("i harfi:", matin.lower().count("i"),"ta")
# print("a harfi:", matin.lower().count("a"),"ta")
# u=u+matin.lower().count("a")
# u=u+matin.lower().count("e")
# u=u+matin.lower().count("i")
# u=u+matin.lower().count("o")
# u=u+matin.lower().count("u")
# print("jami unlilar:",u)


# 4 Berilgan matndagi barcha tinish belgilarini olib tashlab, so'ngra barcha 
# so'zlarni katta harfga o'tkazuvchi va a harfini o ga aylantiruvchi dastur tuzing.
# Bunda ham for, ham yuqoridagi metodlardan foydalaning.

#  m=""
# soz=input("matin: ")
# for x in soz:
#     if x=="'":
#         continue
#     m=m+x.replace("a","o")
# print(m.upper())

