try:
    a = float(input("1-Sonni kiriting: "))
    b = float((input("2-Sonni kiriting: ")))
    natija = (a ** 1000.0) / b
except ValueError:
    print(f"Butun son kirit!")
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas!")
except OverflowError:
    print("Son juda katta!")
except ArithmeticError:
    print("Matematik amal bajarilmadi!")
else:
    print(f"Javob: {natija}")
