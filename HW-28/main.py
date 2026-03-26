# open()

# "r" – oqish (read)
# "w" – yozish (write, eski malumotni ochiradi)
# "a" – oxirina qoshish (append)
# "x" – tozo fayl yaratadi (agar mavjud bosa xato baradi)
# ---------
# "t" – matn rejimi
# "b" – binary(rasm,videola uchun)


# lardan foydalanib fayl ochish

# .read() - oqidi
# .close() - yopadi
# .readline() - qatorni oqidi
# with lardan foydalanish - faylni ochadi , keyin ishi tamam bosa ozi yopadi


# a=open("Hello.text","a")
# a.write("Hello")
# a.close()

# a=open("Hello.text","r") ----boshda r ni onnina a bilan fayl ochb write bln yozdm keyn r qoyb read atdm
# # a.write("Hello")
# print(a.read())
# a.close()

# a=open("Hello.text","r") ----boshda r ni onnina a bilan fayl ochb write bln yozdm keyn r qoyb readline atdm
# # a.write(f"Hello n skclnwdnckl")
# print(a.readline())
# a.close()

# # with open("test.txt", "a") as w:
# #     w.write("salom text ...")
# with open("test.txt", "r") as w:
#     print(w.read())


# c=open("Hello.text","r")
# print(c.read())
# c.close()

# d=open("hi.txt","at")
# d.close()

# b=open("hi.txt","ab")
# b.close()

# open("hi.txt","wt")

# open("hi.txt","wb")

# open("hi.txt","xt")

# open("hi.txt","xb")

