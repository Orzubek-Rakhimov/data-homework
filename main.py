#  tasks.json

# [
#     {
#         "id":1,
#         "title":"Qarzni berish",
#         "time":"21:00",
#         "done":True
#     },
#      {
#         "id":2,
#         "title":"Qarzni berish",
#         "done":False
#     },
#       {
#         "id":3,
#         "title":"Qarzni berish",
#         "done":False
#     }
# ]


# 1. Hamma Taskni ko'rsatish
# 2. Yangi Task Kirgazish
# 3. Taskni o'chirish
# 4. Taskni bajaril(ma)gan deb belgilash
# 5. Vaqni o'zgartirish
# 6. Chiqish

import json
import time



def tasks():
    with open("tasks.json" , "r") as f:
        tasklar = f.read()
        if not tasklar:
            tasklar = []
        json_tasklar = json.loads(tasklar)
        print(f"===============================================")
        for task in json_tasklar:
            print(f"{task["id"]} * {task["title"]}*{task["xozirgi_vaqt"]} * {task["done"]}")    
        print(f"===============================================")



def add_task():
   try:
        task_title = input("Taskni kirgazing:")
        xozirgi_vaqt= time.strftime("%H:%M:%S")
        with open("tasks.json" , "r") as f:
                tasklar = f.read()
                if not tasklar:
                    tasklar = []

                json_tasklar = json.loads(tasklar)
                list_uzunligi = len(json_tasklar)
                id = list_uzunligi + 1

                task = {
                    "id":id,
                    "title":task_title,
                    "time":xozirgi_vaqt,
                    "done":False
                }
                json_tasklar.append(task)
                json_tasklar_file = json.dumps(json_tasklar)
                with open("tasks.json" , "w") as ff:
                    ff.write(json_tasklar_file)
   except Exception as e:
       print("task qoshishda xato" , e)
        

def delete_task():
     id = int(input("Taskni idsini kiritng: "))
     with open("tasks.json" , "r") as f:
        tasklar = f.read()
        if  len(tasklar) == 2:
            print("============================")
            print("Hech qanday task mavjud emas")
            print("============================")
            return
        json_tasklar = json.loads(tasklar)
        MATCH = False
        yangi_tasklar = []
        for task in json_tasklar:
            if task["id"] == id:
                MATCH = True
            else:
                yangi_tasklar.append(task)
        
        with open("tasks.json" , "w") as ff:
            json_yangi_tasklar_file = json.dumps(yangi_tasklar)
            ff.write(json_yangi_tasklar_file)


def done_task():
    id = int(input("Taskni idsini kiritng: "))
    with open("tasks.json" , "r") as f:
        tasklar = f.read()
        if  len(tasklar) == 2:
            print("============================")
            print("Hech qanday task mavjud emas")
            print("============================")
            return
        json_tasklar = json.loads(tasklar)
        for task in json_tasklar:
            if task["id"] == id:
                if task["done"] == False:
                    task["done"] = True
                else:
                    task["done"] = False
        with open("tasks.json" , "w") as ff:
            json_tasklar_file = json.dumps(json_tasklar)
            ff.write(json_tasklar_file)


while True:
    try:
        tanlov = int(input("1.Hamma Taskni ko'rsatish\n2.Yangi Task Kirgazish\n3.Taskni o'chirish\n4.Taskni bajaril(ma)gan deb belgilash\n5. Chiqish\n (1-5) sonni kirgazing: \n"))

        if tanlov == 1:
            # 1. Fayldan o'qish
            # 2. List va lug'atga aylantirish
            # 3. Ekranga to'gri formatda chiqarish
            tasks()

        elif tanlov == 2:
            # 1. Foydalanuvchidan task olish
            # 2. Task Id berish
            # 3. Yanagi taskni faylga yozish
            add_task()
        elif tanlov == 3:
            # 1. Foydalanuvchidan id ni olish
            # 2. id bormi yoqmi tekshirish
            # 3. Fayldan ochirish
           delete_task()
        elif tanlov == 4:
            # 1. Foydalanuvchidan id ni olish
            # 2. id bormi yoqmi tekshirish
            # 3. Done ozgartiramiz 
            # 4. Faylga yozamiz
            done_task()
        elif tanlov == 5:
            break
        else:
            raise Exception()
    
    except ValueError:
        print("===================")
        print("Butun son kiriting!")
        print("===================")
    except:
        print("======================")
        print("(1-5) Sonni kirgazing!")
        print("======================")
