while True:
 try:

  son1=float(input("1-sonni kiriting : "))
  amallar=input("Amallarni tanlang :  + , - , * , /   :" )
  son2=float(input("2-sonni kiriting : "))
  if amallar=="+":
      natija=son1 + son2
  elif amallar=="-":
     natija=son1 - son2
  elif amallar=="*":
      natija=son1 * son2

  elif amallar=="/":
      natija=son1 / son2
  else:
     print("Notogri amal")
     continue
  print(natija)
 except ValueError:
      print("Iltimos son kiriting : ")
      continue
 except ZeroDivisionError:
      print("0-ga bolish mumkun emas ")
      continue
 except TypeError:
      print("Sonni "" siz yozing !")
      continue
 else:
  break