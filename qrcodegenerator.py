import qrcode
import time 
import os

url = input("zadej url nebo text do qr kodu: ")
img = qrcode.make(url)

jmeno = input("zadej jmeno qrkodu: ")
img.save(jmeno + ".png")
print("hotovo")
moznost = input("chcete smazat qr kod (Y/N): ")
if moznost == "Y" or moznost == "y":
    os.remove(jmeno + ".png")
    print("smazano")
    time.sleep(3)
else:
    print("sbohem")
    time.sleep(3)