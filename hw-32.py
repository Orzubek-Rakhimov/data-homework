import json
import time
# 1. Hamma Taskni ko'rsatish
# 2. Yangi Task Kirgazish
# 3. Taskni o'chirish
# 4. Taskni bajaril(ma)gan deb belgilash
# 5. Vaqni o'zgartirish
# 6. Chiqish
def vazifa():
    with open("vazifa.json") as f:
        vazifalar=f.read()
        if not vazifalar:
            vazifalar=[]
        json_vazifalar=json.loads(vazifalar)
        print("———————————————————————————————")
        for vazifa in json_vazifalar:
            print(f"« {vazifa["id"]} • {vazifa["title"]} • {vazifa["done"]} • {vazifa["time"]} »")
        print("———————————————————————————————")
def shaxs_qoshish():
    try:
        shaxs_title=input("Menuga qaytish uchun 5 ni kirting!\nvazifa kirting: ")
        with open("vazifa.json") as f:
            vazifalar=f.read()
            if not vazifalar:
                vazifalar=[]
            else:
                json_vazifalar=json.loads(vazifalar)
            if json_vazifalar:
                vazifachi = json_vazifalar[-1]["id"]
                id = vazifachi+1
            else:
                id = 1
            vazifa={
                    "id":id,
                    "title":shaxs_title,
                    "done":False,
                    "time":time.ctime()
            }
            json_vazifalar.append(vazifa)
            json_vazifalar_file=json.dumps(json_vazifalar)
            with open("vazifa.json","w") as ff:
                ff.write(json_vazifalar_file)

    except Exception as e:
        print("vazifa qoshishda xato" , e)
def vazifa_ochirish():
    id=int(input("Menuga qaytish uchun 5 ni kirting!\nvazifa idsini kiriting: "))
    with open("vazifa.json") as f:
        vazifalar=f.read()
        if len(vazifalar)==2:
            print("————————————————————————————")
            print("Hech qanday task mavjud emas")
            print("————————————————————————————")
            return
        json_vazifalar=json.loads(vazifalar)
        yangi_vazifalar=[]
        for vazifa in json_vazifalar:
            if vazifa["id"] == id:
                print(f"ID: {vazifa["id"]} ochirildi")
            else:
                yangi_vazifalar.append(vazifa)
        with open("vazifa.json","w") as ff:
            json_yangi_vazifalar_file=json.dumps(yangi_vazifalar)
            ff.write(json_yangi_vazifalar_file)
def done_vazifa():
    id = int(input("Menuga qaytish uchun 5 ni kirting!\nvazifa idsini kiritng: "))
    with open("vazifa.json" , "r") as f:
        vazifalar= f.read()
        if  len(vazifalar) == 2:
            print("————————————————————————————")
            print("Hech qanday task mavjud emas")
            print("————————————————————————————")
            return
        json_vazifalar = json.loads(vazifalar)
        for vazifa in json_vazifalar:
             if vazifa["id"] == id:
                if vazifa["done"] == False:
                    vazifa["done"] = True
                else:
                    vazifa["done"] = False
        with open("vazifa.json" , "w") as ff:
            json_vazifalar_file = json.dumps(json_vazifalar)
            ff.write(json_vazifalar_file)
while True:
    try:
        tanlov = int(input("1.Hamma vazifani ko'rsatish\n2.Yangi vazifa Kirgazish\n3.vazifani o'chirish\n4.vazifani bajaril(ma)gan deb belgilash\n5. Chiqish\n (1-5) sonni kirgazing: \n✍️ : "))
        if tanlov==1:
            vazifa()
        elif tanlov==2:
            shaxs_qoshish()
        elif tanlov==3:
            vazifa_ochirish()
        elif tanlov==4:
            done_vazifa()
        elif tanlov==5:
            break
        else:
            raise Exception()
    except ValueError:
        print("———————————————————")
        print("Butun son kiriting!")
        print("———————————————————")
    except:
        print("——————————————————————")
        print("(1-5) Sonni kirgazing!")
        print("——————————————————————")
        



