

 # #ülesane1

# nimi=input("Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper() and nimi=="JUKU":
#     if nimi=="JUKU":
#         print("Lähme kino")
#         try:
#             vanus=int(input(f"Kui vana sa oled {nimi} ?"))
#             if vanus<0:
#                 print("viga")
#             elif vanus<=6:
#                 print("tasuta")
#             elif vanus<15:
#                 print("lastepilet")
#             elif vanus<=65:
#                 print("täispilet")
#             elif vanus<=100:
#                 print("sooduspilet")
#             else:
#                 print("vale andme tüüb")
#         except:
#             print("Täisarv oli vaja sisestada")
#     else:
#        print("Ootan Juku")
# else:
#     print("Segatud sõna")
# print()
      
# #ülesane2
# nimi1=input("1. Mis on sinu nimi? ")
# nimi2=input("2. Mis on sinu nimi? ")
# nimed=["Evgeniy", "Nikita"]
# if nimi1.isalpha() and nimi2.isalpha():
#     if (nimi1 in nimed) and (nimi2 in nimed):
#         print("Nad on pinginabrid")
#     else:
#         print("Nad ei jole pinginabrid")
# else:
#     print("Viga")


#     #2 variant

# if (nimi1=="Evgeniy" and nimi2=="Nikita") or (nimi2=="Evgeniy" and nimi1=="Nikita"):
#     print("Nad on pinginabrid")
# else:
    # print("Nad ei jole pinginabrid")



#   #ülesane3
# try:
#     a=float(input("Toa pikkus "))
#     b=float(input("Toa laius "))
#     S=a*b
#     print(f"Põranda pindala on {S} m**2")
#     vastus=input("Kas tahab remondi teha?(jah-1/ei-0) ")
#     if vastus.upper()=="JAH" or vastus=="1":
#         print("remont")
#         hind=float(input("Ühe meetri Hind: "))
#         summa=hind*S
#         print(f"Remondi Kulud: {summa} euro ")
#     elif vastus.upper()=="EI" or vastus=="0":
#         print("-")
#     else:
#         print("Ei sa aru")
# except:
#     print("Numbrid!!!")

# #ülesane4 Найди цену со скидкой 30%, если первоначальная цена больше 700.
# hind=float(input("Ведите первоночальную цену: "))
# if hind>700:
#    skidka = 0.30  # 30% скидка
#    so_skidkoi = hind * (1 - skidka)
#    print(f"Цена со скидкой: {so_skidkoi:.2f}")
# else:
#     print("Скидка не применяется, так как цена меньше или равна 700.")


# #ülesane5 "Спроси температуру и сообщи, превышает ли она 18 градусов (рекомендуемая комнатная температура зимой)."
# temperature = float(input("Введите температуру: "))
# if temperature > 18:
#     print("Температура выше 18 градусов. Рекомендуемая комнатная температура зимой.")
# else:
#     print("Температура 18 градусов или ниже. Это ниже рекомендуемой комнатной температуры зимой.")


# #ülesane6 "Спроси рост человека и сообщи, является ли он низким, средним или высоким (границы определите сами)."
# pikkus = float(input("Введите ваш рост: "))
# if pikkus<160:
#     print("Вы низкого роста")
# elif 160 <= pikkus <= 180:
#     print("Вы среднего роста")
# else:
#     print("Вы высокого роста")


#ülesane7 Спроси у человека рост и пол, и сообщи, является ли он низким, средним или высоким (можно использовать несколько вложенных блоков условий).
pikkus = float(input("Введите ваш рост в сантиметрах: "))
sugu = input("Введите ваш пол (м/ж): ")# м - мужской, ж - женский

if sugu == "м":  # Для мужчин
    if pikkus < 160:
        print("Вы низкого роста для мужчины.")
    elif 160 <= pikkus <= 180:
        print("Вы среднего роста для мужчины.")
    else:
        print("Вы высокого роста для мужчины.")
elif sugu == "ж":  # Для женщин
    if pikkus < 150:
        print("Вы низкого роста для женщины.")
    elif 150 <= pikkus <= 170:
        print("Вы среднего роста для женщины.")
    else:
        print("Вы высокого роста для женщины.")
else:
    print("Пол указан некорректно. Введите 'м' для мужчины или 'ж' для женщины.")



#ülesane8 
kaubad=["piim", "leib", "sai"] #Квадратные скобки ([]) используются в Python для создания списка — это структура данных, которая позволяет хранить несколько элементов в одном объекте.
hind_piim=2.5
hind_leib=1.8
hind_sai=1.5
