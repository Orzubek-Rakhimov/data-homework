#Foydalanuvchidan 3 ta input olinadi 
# 3 ta inputdan qaysi biri eng kattasi ekanligini chiqarsin agar 3 sam dang bolsa hammasi teng dab chiqarsn.

son1=float(input("1 chi sonni kirizing : "))

son2=float(input("2 chi sonni kirizing : "))

son3=float(input("3 chi sonni kirizing : "))

if son1==son2 and son2==son3:
     print("Hamma son teng ")
     
elif son1>son2 and son1>son3:
     print(son1, "Eng katta son ")
     
elif son2>son1 and son2>son3:
     print(son2, "Eng katta son ")
     
elif son3>son1 and son3>son2:
     print(son3, "Eng katta son")
     
elif son1==son2 and son3<son1:
     print( son1,"Eng katta son son1 va son2 ")
     
elif son1==son3 and son2<son1:
     print(son1, "Eng katta son son1 va son3 ")
     
elif son2==son3 and son1<son2:
     print(son2, "Eng katta son son2 va son3")
     
elif son2==son1 and son3<son2:
     print(son2, "Eng katta son son2 va son1 ")
     
elif son3==son1 and son2<son3:
     print(son3, "Eng katta son son3 va son1")
     
elif son3==son2 and son1<son3:
     print(son3, "Eng katta son son3 va son2")
else:
     print("Xatolik")