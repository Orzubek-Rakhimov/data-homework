import os
#1."kitoblar.txt" fayliga 5 ta sevimli kitob nomini yozing va keyin ularni o‘qib ekranga chiqaring.


with open("kitoblar.txt","w") as kitob:
    print( kitob.write("\n Harry Poter\n Hukumatnig 48 qonuni\n Round Up\n Stiv Jobs-Iphone Tarixi \n Mock Ielts"))
with open("kitoblar.txt","r")as kitob:
     print(kitob.read())




# 2."baholar.txt" fayliga 5 ta baho yozing (masalan: 85, 90, 78, 100, 67) va keyin o‘qib o‘rtacha bahoni hisoblang.

baholar ={
    "Algebra": 90,
    "Ona tili": 80,
    "Jismoniy tarbiya": 100,
    "Informatika": 100,
    "Tarix": 70
    }
with open("baholar.txt", "w") as f:
    for fan, baho in baholar.items():
        f.write(f"{fan}: {baho}\n") 
with open("baholar.txt","r")as f:
     print(f.read())
# print(f"Orta baxo; {baholar.values/5}") <---Xamma jayi zor getyatirganda python pythonni minusini topdim shunninfunksiya qoshmaganlarinin 



# 3."matn.txt" fayliga bir necha jumla yozing va keyin o‘qib eng uzun so‘zni toping.

with open("matn.txt","w")as f:
     f.write("Assalomu aleykum xurmatli futbol muxlislari sizlarni El-Classico \noyinida korib turganimdan juda xursandman.")
with open("matn.txt","r")as f:
     matn=(f.read())
     
sozlar = matn.split()      
uzun_soz = ""

for soz in sozlar:
    if len(soz) > len(uzun_soz): 
        uzun_soz = soz

print(f"Eng uzun soz:{ uzun_soz}")


os.remove("kitoblar.txt")
os.remove("baholar.txt")
os.remove("matn.txt")


