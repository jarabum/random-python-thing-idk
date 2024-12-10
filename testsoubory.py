with open("soubor.txt", "r+") as f:
    obsah = f.read()
    f.write("blablablabla hahahaahaha")
print(obsah)

with open("soubor.txt", "w") as f:
    f.write("je to smazany jooooooooooooo je to smazany")