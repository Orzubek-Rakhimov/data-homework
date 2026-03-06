
# 1
# Foydalanucgidan son so'raladi va shu sonni 1 dan 10 gacha bo'lgan sonlar ko'paytmasi chiqariladi
# input => 20 | 30
# 20 | 30
# 40  | 60
# 60  | 90
# ...
# 180 | 270
# 200 | 300


# 2
# Foydalanuvchidan son lar so'ralavradi qachongi foydalanuchi manfiy son kirgizguncha va bundan keyin oldingi kirgizilgan sonlar ko'paytmasi chiqarilsin
#  10
# 50 
# 100
# 5
# 2 
# -1 | -23

# 10 * 50 * 100 * 5 * 2 = 500_000



# 2 chini javobi
son = int(input("Sonni kiritng: "))
n = 1
while n <= 10 : 
    print(son * n) 
    n = n + 1
  
  
  # 10  
son = int(input("Sonni kiriting:"))
kopaytma = 1
while son > -1 : 
    kopaytma = kopaytma * son 
    son = int(input("Sonni kiriting:")) 
print(kopaytma)



# 3
# Foydalanuvhcidan 1dan 100gacha son kirgizish so'raladi (xoxlagancha) qachonki foydalanuvchi "stop"
# deb yozsa o'shanda programa to'xtashi va
# kirgizilgan sonlarning o'rta qiymatini chiqarishi kerak
# 1 - 100
# "stop"
# 5
# 10
# 6
# 3
# stop
# (5 + 10 + 6 + 3 ) / 4 = 6


# 3 chini javobi
# "10"
son_yoki_stop = input("Sonni kiring: ")
yigindi = 0
k = 0

while son_yoki_stop != "stop":
    # 10
    son = int(son_yoki_stop)
    
    
    if 1 <= son and son <= 100:
        yigindi = yigindi + son
        k = k + 1
    else:
        print("Sonni to'g'ri kiriting!")
        
    son_yoki_stop = input("Sonni kiring: ")

print( yigindi / k)
