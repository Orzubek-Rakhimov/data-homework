import json

with open("student.json","r") as f:
     students=json.load(f)
kattalar=[]
for student in students:
     if student["yosh"]>14:
          kattalar.append(student)
with open ("kattalaar.json","w")as f:
     studentt=json.dump(kattalar,f)