

# # Fayl ochish.
f=open("tex.txt","at")
f.close()



# # Yangi fayl yaratish(agar bu fayl bolsa xato beradi)
f=open("Matn.txt","x")
f.close()


# # Fayl bo‘lmasa yaratadi, bo‘lsa ichidagini o‘chiradi.
f=open("yusufbek.txt","w")
f.close()



#----------------------------------



# # Fayllarni oqish.

f=open("Matn.txt","r")
print(f.read())
f.close()


# # Fayllarni oqish index orqali.

f=open("Matn.txt","r")
print(f.readline(5))
f.close()

#---------------------------------------------------------------


# fayllarni with orqali oqish
with open("Matn.txt", "r") as f:
     print(f.read())
     
     
# Fayllarni with orqali indexi bilan oqish  
indexx=int(input("Indexni kiriting :")) 
with open("Matn.txt", "r") as f:
     print(f.readline(indexx))
     
 
     


