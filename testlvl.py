import time

with open("lvl.txt", "r") as f:
    lvl = f.read()
if lvl == 1:
    print("lvl 1")
    input = input("Kolik je my let ;) ")
    if input == 12:
        print("spravne")
        print("toto by se mnelo zavrit")
        with open("lvl.txt", "w") as f:
            f.write("2")
    else:
        print("spatne")