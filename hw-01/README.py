# 1.Foydalanuvchi login kiritayotganda tasodifan boshiga yoki oxiriga bo'sh joy (space) tashlab ketsa, bu xatoni qanday bartaraf etasiz?
# a=input("Loginni kiriting: ")
# print(a.strip())

# "***Python***" satridagi yulduzchalarni olib tashlab, faqat so'zning o'zini qoldirish uchun ushbu metoddan qanday foydalaniladi?
# a=input("Loginni kiriting: ")
# print(a.strip("*"))



# 2.1 Berilgan gapdagi barcha nuqtalarni vergulga almashtiruvchi kod yozing.
# a=input("Gapni kiriting: ")
# print(a.replace(".",","))

# 2.2 Satr ichidagi bo'sh joylarni (probel) butunlay olib tashlash (ya'ni "" ga almashtirish) uchun bu metodni qanday qo'llaysiz?
# a=input("Gapni kiriting: ")
# print(a.replace(" ",""))

# 3.1 Matn ichida "Python" so'zi necha marta takrorlanganini aniqlang.
# a=input("Matnni kiriting: ")
# print(a.count("Python"))

# 3.2 Satrdagi unli harflar (masalan, 'a') sonini hisoblashda ushbu metoddan qanday foydalaniladi?
# a=input("Matnni kiriting: ")
# print(a.count("a"))

# 4 Berilgan matndagi barcha tinish belgilarini olib tashlab, so'ngra barcha so'zlarni katta harfga o'tkazuvchi va a harfini o ga aylantiruvchi dastur tuzing. Bunda ham for, ham yuqoridagi metodlardan foydalaning.
# # "g'afur" => "GOFUR"
# a=input("Matnni kiriting: ")
# t="'.,!-()?:;"
# for i in t:
#     a=a.replace(t,"")
# a=a.replace("a","o")
# print(a.upper())
