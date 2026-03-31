import json

# 1. 20 ta o'quvchi yaratamiz
students = [
    {"ism": "Aziz", "familya": "Karimov", "yosh": 13},
    {"ism": "Dilshod", "familya": "Rasulov", "yosh": 15},
    {"ism": "Malika", "familya": "Tursunova", "yosh": 16},
    {"ism": "Javohir", "familya": "Qodirov", "yosh": 14},
    {"ism": "Shahnoza", "familya": "Ismoilova", "yosh": 17},
    {"ism": "Bekzod", "familya": "Nazarov", "yosh": 12},
    {"ism": "Madina", "familya": "Xudoyberdiyeva", "yosh": 18},
    {"ism": "Sardor", "familya": "Rahmatov", "yosh": 15},
    {"ism": "Nilufar", "familya": "Yusupova", "yosh": 13},
    {"ism": "Akmal", "familya": "Sobirov", "yosh": 19},
    {"ism": "Diyor", "familya": "Abdullayev", "yosh": 14},
    {"ism": "Zarina", "familya": "Hakimova", "yosh": 16},
    {"ism": "Temur", "familya": "Olimov", "yosh": 17},
    {"ism": "Gulbahor", "familya": "Qurbanova", "yosh": 12},
    {"ism": "Rustam", "familya": "Saidov", "yosh": 15},
    {"ism": "Mohira", "familya": "Aliyeva", "yosh": 14},
    {"ism": "Jasmin", "familya": "Karimova", "yosh": 18},
    {"ism": "Ulugbek", "familya": "Raximov", "yosh": 16},
    {"ism": "Laylo", "familya": "Normatova", "yosh": 13},
    {"ism": "Sanjar", "familya": "Ergashev", "yosh": 17}
]

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

with open("students.json", "r", encoding="utf-8") as f:
    data = json.load(f)

katta_students = []
for student in data:
    if student["yosh"] > 14:
        katta_students.append(student)

with open("sorted_students.json", "w", encoding="utf-8") as f:
    json.dump(katta_students, f, ensure_ascii=False, indent=4)
