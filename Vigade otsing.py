from math import *  # было написано import * from math

# были написаны не правильно формулы и также  сначала пишутся формулы а потом все результаты а не формула результат ну покрайне мере мне так нравится больше.
print("Ruudu karakteristikud")
a=float(input("Sisesta ühe külje pikkus => "))   #неправильные ковычки небыло написано float
b=float(input("Sisesta teise külje pikkus => "))  #это дополнительная строка которую надо была добавить
S=a*b  
P=2*(a+b)
di=sqrt(a**2+b**2)   # сдесь было написано полностью math.sqrt
print("Ruudu pindala", S) 
print("Ruudu ümbermõõt", P)   #сдесь были не правильные кавычки
print("Ruudu diagonaal", round(di,2)) 


print("Ristküliku karakteristikud") # лишня скобка
a=float(input("Sisesta ristküliku 1. külje pikkus => ")) # эсли брать формулу то это должно быть a, небыло написано float
b=float(input("Sisesta ristküliku 2. külje pikkus => ")) # эсли брать формулу то это должно быть b, небыло написано float
S=a*b # заменил буквы на а и b
P=2*(a+b) # заменил буквы на а и b, небыло знака умножить
di=sqrt(a**2+b**2) # заменил буквы на а и b, добавил по одной *, сдесь было написано полностью math.sqrt
print("Ristküliku pindala", S) # не было ковычек
print("Ristküliku ümbermõõt", P) 
print("Ristküliku diagonaal", round(di, 2))  # одной скобки не хватает и добавил цыфру 2 вот сюда round(di)


print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) # сдесь были не правильные кавычки, небыло написано float
d=2*r #небыло знака умножить
S=pi*r**2 #скобки лишнии и не хватало одной *, S=pi()*r*2
C=2*pi*r #скобки лишнии и не было знака умножить C=2pi()*r
print("Ringi läbimõõt", d) # не было запятой 
print("Ringi pindala", round(S, 2))   #добавил цыфру 2 вот сюда round(S)
print("Ringjoone pikkus", round(C, 2)) #не хватало одной скобки и добавил цыфру 2 вот сюда round(С)