import numbers
from random import *  #*-kõik funktsionid randidndt as rd 
from math import * #pi kasutamiseks

#Ülesane 1
print("Tere tulemast!")
nimi=input("Mis on sinu nimi? ").capitalize() #loweк(все маленькими) upper(все большое)
print("Tere tulemast! Tervitan sind ", nimi)
print("Tere tulemast! Tervitan sind "+ nimi)
vanus=int(input("Kui vana sa oled? "))
print("Tere tulemast! Tervitan sind "+nimi+" Sa oled ",vanus,"aastad vana")
print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastad vana")

# #Ülesane 2
vanus = 18
eesnimi = "zenja"
pikkus = 178
kas_käib_koolis = True
print(type(vanus),(eesnimi),(pikkus),(kas_käib_koolis))

# #Ülesane 3
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

#Ülesane 5
print("Ristkülikukujulise maatüki diagonaali pikkuse leidmine ")
N=float(input("Ristküliku ühe külje mõõtmed "))
M=float(input("Ristküliku teise külje mõõtmed "))
d=sqrt(N**2+M**2) # type: ignore
print(f"Ristkülikukuju pikkus on {round(d,2)}")

#Ülesane 6
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
aeg = float(input("Mitu tundi kulus sõiduks? "))
kiirus = teepikkus / aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#Ülesane 7
print("Kirjutaga 5 erinevad täis arvud, et leida keskmist.")
arv1= float(input("Kirjutage esimene arv. "))
arv2= float(input("Kirjutage teine arv. "))
arv3= float(input("Kirjutage kolmas arv. "))
arv4= float(input("Kirjutage neljas arv. "))
arv5= float(input("Kirjutage viies arv. "))
keskmine=(arv1+arv2+arv3+arv4+arv5)/5
print(f"Keskmine arve on {keskmine}")

#Ülesane 8
print("@..@")
print("(----)")
print("( \__/ )")
print("^^ "" ^^")

#Ülesane 9
print("Arvutage kolmnurga ümbermõõdu")
a=float(input("Kirjutage esimest täisarvulist muutujat. "))
b=float(input("Kirjutage teist täisarvulist muutujat. "))
c=float(input("Kirjutage kolmandat täisarvulist muutujat. "))
P=a+b+c
print(f"Kolmnurga ümbermõõd on {P}")

#Ülesane 10
print("Ostame pitsa koos sõbraga mis maksis 12.90 ja jätame 10% jootraha.")
print("Kui palju peab igaüks maksma?")
pitsa_hind = float(input("Sisesta pitsa hind (näiteks 12.90): "))
jootraha = pitsa_hind * 0.10  # 10% чаевые
kokku = pitsa_hind + jootraha  # Общая сумма
igaüks_peab_maksma= kokku/2   # Сколько должен каждый заплотить
print(f"Igaüks peab maksma {round(igaüks_peab_maksma,2)} €")