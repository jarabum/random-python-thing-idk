input = input("Napiš jméno souboru i s příponou: ")
soubor = open(input,"r") 
pocet = 0

for line in soubor:
    slova = line.split(" ")
    pocet += len(slova)
soubor.close

print("Soubor má", pocet, "slov")