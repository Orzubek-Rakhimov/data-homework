# 1.Foydalanuvchi login kiritayotganda tasodifan boshiga yoki oxiriga bo'sh joy (space) tashlab ketsa, bu xatoni qanday bartaraf etasiz?
login=input("Loginingizni kiriting : ")
print(login.strip( ))



# "***Python***" satridagi yulduzchalarni olib tashlab, faqat so'zning o'zini qoldirish uchun ushbu metoddan qanday foydalaniladi?

matn="***Python***"
print(matn.strip("*"))




# 2.1 Berilgan gapdagi barcha nuqtalarni vergulga almashtiruvchi kod yozing.

tex="Assalomu aleykum xurmatli o`quvchilar.\n Sizlarni yangi oquv yili bilan tabriklaymiz.\n Bu o`quv yilida active bolishingizni sorab qolamiz"
print(tex.replace(".",","))




# 2.2 Satr ichidagi bo'sh joylarni (probel) butunlay olib tashlash (ya'ni "" ga almashtirish) uchun bu metodni qanday qo'llaysiz?

mant="   Assalomu Aleykum  "
print(mant.strip(  ))




# 3.1 Matn ichida "Python" so'zi necha marta takrorlanganini aniqlang.

matn="Assalomu Aleykum xurmatli  talabalar .\n Bugungi imtixon Python dasturlash tilidan bolib otadi.\n Python da xammaga omad ! "
print(matn.count("Python"))




# 3.2 Satrdagi unli harflar (masalan, 'a') sonini hisoblashda ushbu metoddan qanday foydalaniladi?

tex="Assalomu Aleykum xurmatli  talabalar .\n Bugungi imtixon Python dasturlash tilidan bolib otadi.\n Python da xammaga omad !"
print(tex.count("a"))




# 4 Berilgan matndagi barcha tinish belgilarini olib tashlab, so'ngra barcha so'zlarni katta harfga o'tkazuvchi va a harfini o ga aylantiruvchi dastur tuzing. Bunda ham for, ham yuqoridagi metodlardan foydalaning.
# "g'afur" => "GOFUR"


