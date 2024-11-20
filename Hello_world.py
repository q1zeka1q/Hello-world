from random import *  #*-kõik funktsionid randidndt as rd 
from math import * #pi kasutamiseks
#Ülesane 1
# print("Tere tulemast!")
# nimi=input("Mis on sinu nimi? ").capitalize() #loweк(все маленькими) upper(все большое)
# print("Tere tulemast! Tervitan sind ", nimi)
# print("Tere tulemast! Tervitan sind "+ nimi)
# vanus=int(input("Kui vana sa oled? "))
# print("Tere tulemast! Tervitan sind "+nimi+" Sa oled ",vanus,"aastad vana")
# print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastad vana")

#Ülesane 2
vanus = 18
eesnimi = "zenja"
pikkus = 178
kas_käib_koolis = True
print(type(vanus),(eesnimi),(pikkus),(kas_käib_koolis))

#Ülesane 3
kokku=randint(1,1000)
print(f"kokku on {kokku} kommi")
kommi=int(input("Mitu kommi sa tahad? "))
kokku=kokku-kommi
print(f"Jääk on {kokku} kommi")

#Ülesane 4
print("Läbimõõdu leidmine ")
#l-ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")