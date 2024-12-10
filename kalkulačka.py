a = int(input("napis cislo: "))
b = int(input("napis druhe cislo: "))
znaminko = input("znaminko: ")

if znaminko == "+":
    print(a+b)
elif znaminko == "-":
    print(a-b)
elif znaminko == "*":
    print(a*b)
elif znaminko == "/":
    print(a/b)
else:
    print("spatne znaminko")