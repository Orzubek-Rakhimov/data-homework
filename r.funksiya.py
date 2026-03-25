# b=open("b.funksiyasi.txt","rb")
# t=open("a.funksiyasi.txt","rt")
# print(b.read(),t.read())

# with open("b.funksiyasi.txt","rb") as b_1:
#  with open("a.funksiyasi.txt","rt") as t_2:
#     print(b_1.read(),t_2.read())

# with open("b.funksiyasi.txt","rb") as b_1:
#  with open("a.funksiyasi.txt","rt") as t_2:
#     print(b_1.read(5),t_2.read(8))

with open("w.funksiyasi.txt") as d_1:
    for x in d_1:
        print(x.read(),"⇨")
    print(d_1.readline())
    



