a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))
op = input("Amal (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Noto‘g‘ri amal!")
