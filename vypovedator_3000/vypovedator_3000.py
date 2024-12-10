import time
import os

input("press ENTER to start ")
os.system("cls")
jmeno_souboru = input("napiš jméno souboru: ")
soubor = open(jmeno_souboru + ".txt","x")
soubor.close
loop = True
soubor = open(jmeno_souboru + ".txt","a")
print("užívejte používání vašeho programu :)")
print("napiš konec pro konec programu")
print("---------------------------------------------------------------------------------------------")
while loop:
    policajt = input("co řekl policajt: ")
    if policajt == "konec" or policajt == "KONEC" or policajt == "Konec":
        loop = False
        break
    soubor.write("policajt: " + policajt + "\n")
    podezřelí = input("co řekl podezřelej: ")
    if podezřelí == "konec" or podezřelí == "KONEC" or podezřelí == "Konec":
        loop = False
        break
    if not podezřelí == "konec" or not podezřelí == "KONEC" or not podezřelí == "Konec":
        soubor.write("podezřelej: " + podezřelí + "\n")
soubor.close
os.system("cls")
print("děkujeme za používání policejního softwaru :)")
print("program se vypne za 3 vteřiny")
print()
print("by:jarabum")
time.sleep(3)