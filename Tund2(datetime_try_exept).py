from datetime import *
from calendar import *
from math import *
from random import *

# #Ülesanne 1
# tana=date.today() #
# tanaf=date.today().strftime("%B %d, %Y")

# print(f"Täna on {tana}")
# d=tana.day #nimetus omadus
# m=tana.month
# y=tana.year
# print(d)
# print(m)
# print(y)

# today=date.today()
# day=today.day
# month=today.month
# year=today.year
# days_in_month = {
#     1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
#     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
# }
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     days_in_month[2] = 29
#     days_remaining = days_in_month[month] - day
# print(f"Kuu lõpuni on janud {days_remaining} päeva")


# #Ülesanne 2
# vastus1=3+8/(4-2)*4
# vastus2=3+8/4-2*4
# vastus3=(3+8)/(4-2)*4
# print(vastus1,"\n",vastus2,"\n",vastus3)

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