# 1 Foydalanuvchidan input olinadi Toq va juft son topuchio programma tuzing.


son=int (input("Sonni kirizing :"))
if son % 2:
    print("Bu son toq son !")
else :
    print("Bu son juft son !") 







# 2 Foydalanuvchidan input olinadi va bu input uning test dagi bahosi (0-100)
# 90 va undan baland bolsa → "5"
# 80–89 → "4"
# 70–79 → "3"
# 60–69 → "2"
#  60 dan past → "1"


baxo=int(input ("Testdan olgan baxoingizni kiriting :"))

if  baxo<0 or baxo >100:
    print("Xato son kiritingiz :")
elif baxo>=90:
    print("Sizning baxoingiz: 5 ")
elif baxo>=80:
   print("Sizning baxoinggiz: 4 ")
elif baxo>=70:
    print("Sizning baxoingiz: 3 ")
elif baxo >= 60:
    print("Sizning baxoingiz: 1 ")
else:
    print("Siz esi past lox odam ekansiz:")








# 3  Foydalanuvchidan 3 ta input olinadi  3 ta inputdan qaysi biri eng kattasi ekanligini chiqarsin
# agar 3 tasi xam teng bolsa 3 tasi teng deb chiqarsin.


son1=float(input("1-Sonni kiriting :"))
son2=float(input("2-Sonni kiriting :"))
son3=float(input("3-Sonni kiriting :"))

if son1>son2 and son1>son3:
 print(son1, "Eng katta son")
elif son2>son1 and son2> son3:
    print(son2, "Eng katta son")
elif son3>son1 and son3>son2:
    print(son3, "Eng katta son")
elif son1==son2 and son2==son3:
    print("Xamma son teng !")








# 4 Foydalanuvchidan 2 ta input olinadi (1-login , 2-kod)
# kiritgan 2 ta inputi login va kod bn bir xil bo'lsa (kirish mumkin) bo'lmasa (kirish mumkin emas) dab chiqarsn.

login="Ismailov"
kod=123456789
loginn=(input("Loginni kiriting :"))
kodd=int(input("Kodinggizni kiriting :"))
if login==loginn and kod==kodd:
    print("Tizimga kirishingiz mumkun")
else:
    print("Kirishinggiz mumkun emas ! ")    



