from datetime import *
from calendar import *
from math import *
from random import *

# Ülesanne 1
tana=date.today() 
tanaf=date.today().strftime("%B %d, %Y")

print(f"Täna on {tana}")
d=tana.day #nimetus omadus
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

detsP=monthrange(2024,12)[1] #31
novP=monthrange(2024,11)[1] #30
jaak=detsP+novP-d
jaak2=novP-d
print(f"Aasta lõppuni on {jaak}")
print(f"Kuu lõppuni on {jaak2}")


#Ülesanne 2
vastus1=3+8/(4-2)*4
vastus2=3+8/4-2*4
vastus3=(3+8)/(4-2)*4
print(vastus1,"\n",vastus2,"\n",vastus3)

#Ülesanne 3
try:
    R=float(input("Sisesta R: "))
    Sk=pi*R**2
    Lk=2*pi*R
    Skv=(2*R)**2
    Lkv=2*R*4
    print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRingi ümbermõõt on {Lkv}\n")

except:
    print("On vaja number!") 

#2variant
R=round(random()*100) #0.0...1.0
Sk=pi*R**2
Lk=2*pi*R
Skv=(2*R)**2
Lkv=2*R*4
print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRingi ümbermõõt on {Lkv}\n")


#Ülesanne 4
d=2.5 #mündi d
maa=6378 #maa radius km
maa*=100000 #maa radius sm maa=maa * 100000
lmaa=2*pi*maa 
kogus=int(lmaa/d)
print(f"On vaja {kogus} mündi. \nMeil on vaja {kogus*2} eur")


#Ülesanne 5
kill_koll = "Kill-Koll"
killadi_koll = "Killadi-Koll"
killkoll = "Killkoll"
print(f"{kill_koll}, {kill_koll}, {killadi_koll}, {kill_koll}, {kill_koll}, {killadi_koll}, {kill_koll}, {kill_koll}, {killkoll},\n{kill_koll}")


#Ülesanne 6    # Три двойных кавычки (""") в Python используются для создания многострочных строк
luletus = """  
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""
print(luletus.upper())


#Ülesanne 7
print("Kirjutage ristküliku lähiskülgede pikkused")
a=float(input("Kirjutage ühe lähiskülge pikkus "))
b=float(input("Kirjutage teise lähiskülge pikkus "))
P=2*(a+b)
S=(a*b)
print(f"Ristküliku ümbermõõd on {round(P)}")
print(f"Ristküliku pindala on {round(S)}")



#Ülesanne 8
print("Kütusekulu arvutamine")
L=float(input("Sisestage tangitud kütuse liitrid "))
D=float(input("Sisestage läbitud kilomeetrid "))
R=(L/D)*100 # Cредний расход топлива на 100 км
print(f"Keskmise kütuse kuulu 100km kohta on {round(R, 2)} liitrid")



#Ülesanne 9
print("Kui kaugele jõuab M minutiga")
V=29.9 #средняя скорость в километрах в час, в данном случае 29,9
M = float(input("Sisestage aeg minutites: ")) 
kaugele_jõuab = V * (M / 60)
print(f"Rulluisutaja jõuab {round(M)} minutiga {round(kaugele_jõuab, 2)} kilomeetri kaugusele.")



#Ülesanne 10
print("Ajateisendus")
minutes = int(input("Sisestage aeg minutites: "))  
hours = minutes // 60  # Целые часы
remaining_minutes = minutes % 60  # Оставшиеся минуты
print(f"Aeg: {hours}:{remaining_minutes}")
