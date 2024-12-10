import qrcode
import time 

url = input("zadej url nebo text do qr kodu: ")
img = qrcode.make(url)

jmeno = input("zadej jmeno qrkodu: ")
img.save(jmeno + ".png")
print("hotovo")
input("napis sem neco pro konec: ")