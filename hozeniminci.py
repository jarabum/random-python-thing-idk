import time
import random

strany = ["pana","orel"]
strana = random.choice(strany)
vyber = input("vyber si pana nebo orel (vše malými písmeny): ")

if strana == "pana":
    if vyber == "pana":
        print("vyhrál jsi :)")
    elif vyber == "orel":
        print("prohrál jsi :(")
    else:
        print("špatný výběr zkus to znovu ;)")
elif strana == "orel":
    if vyber == "pana":
        print("prohrál jsi :(")
    elif vyber == "orel":
        print("vyhrál jsi :)")
    else:
        print("špatný výběr zkus to znovu ;)")