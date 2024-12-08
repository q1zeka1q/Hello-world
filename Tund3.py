from datetime import datetime
import random

#ülesane1

nimi=input("Mis on sinu nimi? ")
if nimi.isalpha() and nimi.isupper() and nimi=="JUKU":
    if nimi=="JUKU":
        print("Lähme kino")
        try:
            vanus=int(input(f"Kui vana sa oled {nimi} ?"))
            if vanus<0:
                print("viga")
            elif vanus<=6:
                print("tasuta")
            elif vanus<15:
                print("lastepilet")
            elif vanus<=65:
                print("täispilet")
            elif vanus<=100:
                print("sooduspilet")
            else:
                print("vale andme tüüb")
        except:
            print("Täisarv oli vaja sisestada")
    else:
       print("Ootan Juku")
else:
    print("Segatud sõna")
print()
      
#ülesane2
nimi1=input("1. Mis on sinu nimi? ")
nimi2=input("2. Mis on sinu nimi? ")
nimed=["Evgeniy", "Nikita"]
if nimi1.isalpha() and nimi2.isalpha():
    if (nimi1 in nimed) and (nimi2 in nimed):
        print("Nad on pinginabrid")
    else:
        print("Nad ei jole pinginabrid")
else:
    print("Viga")


    #2 variant

if (nimi1=="Evgeniy" and nimi2=="Nikita") or (nimi2=="Evgeniy" and nimi1=="Nikita"):
    print("Nad on pinginabrid")
else:
    print("Nad ei jole pinginabrid")



  #ülesane3
try:
    a=float(input("Toa pikkus "))
    b=float(input("Toa laius "))
    S=a*b
    print(f"Põranda pindala on {S} m**2")
    vastus=input("Kas tahab remondi teha?(jah-1/ei-0) ")
    if vastus.upper()=="JAH" or vastus=="1":
        print("remont")
        hind=float(input("Ühe meetri Hind: "))
        summa=hind*S
        print(f"Remondi Kulud: {summa} euro ")
    elif vastus.upper()=="EI" or vastus=="0":
        print("-")
    else:
        print("Ei sa aru")
except:
    print("Numbrid!!!")

#ülesane4 Найди цену со скидкой 30%, если первоначальная цена больше 700.
hind=float(input("Ведите первоночальную цену: "))
if hind>700:
   skidka = 0.30  
   so_skidkoi = hind * (1 - skidka)
   print(f"Цена со скидкой: {so_skidkoi:.2f}")
else:
    print("Скидка не применяется, так как цена меньше или равна 700.")


#ülesane5 "Спроси температуру и сообщи, превышает ли она 18 градусов (рекомендуемая комнатная температура зимой)."
temperature = float(input("Введите температуру: "))
if temperature > 18:
    print("Температура выше 18 градусов. Рекомендуемая комнатная температура зимой.")
else:
    print("Температура 18 градусов или ниже. Это ниже рекомендуемой комнатной температуры зимой.")


#ülesane6 "Спроси рост человека и сообщи, является ли он низким, средним или высоким (границы определите сами)."
pikkus = float(input("Введите ваш рост: "))
if pikkus<160:
    print("Вы низкого роста")
elif 160 <= pikkus <= 180:
    print("Вы среднего роста")
else:
    print("Вы высокого роста")


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
товары = {
    "Молоко": round(random.uniform(0.5, 2.5), 2),
    "Хлеб": round(random.uniform(0.3, 1.5), 2),
    "Булка": round(random.uniform(0.2, 1.2), 2),
    "Яблоки": round(random.uniform(1.0, 3.0), 2),
    "Картофель": round(random.uniform(0.5, 2.0), 2)
}
чек = {}
print("Добро пожаловать в магазин!")
for товар, цена in товары.items():
    print(f"{товар} стоит {цена} € за штуку.")
    ответ = input(f"Хотите купить {товар}? (да/нет): ").strip().lower()
    if ответ == "да":
        try:
            количество = int(input(f"Сколько {товар} вы хотите купить? "))
            if количество > 0:
                чек[товар] = (количество, round(количество * цена, 2))
        except:
            print("Ошибка ввода. Пропускаем этот товар.")
    else:
        print(f"{товар} пропущен.")
итого = sum(стоимость for количество, стоимость in чек.values())
print("\n=== ВАШ ЧЕК ===")
for товар, (количество, стоимость) in чек.items():
    print(f"{товар}: {количество} шт. по {товары[товар]} € = {стоимость} €")
print(f"\nИТОГО: {round(итого,2)} €")
 

#ülesane9
side1 = float(input("Введите длину первой стороны: "))
side2 = float(input("Введите длину второй стороны: "))
if side1 == side2:
    print("Это квадрат.")
else:
    print("Это не квадрат.")


# ülesane10
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except:
    print("Ошибка: введите корректные числа.")
    exit()
operation = input("Выберите операцию (+, -, *, /): ").strip()
if operation == "+":
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Ошибка: деление на ноль невозможно.")
else:
    print("Ошибка: выбрана некорректная операция.")



# ülesane11
from datetime import datetime
try:
    birth_year = int(input("Введите ваш год рождения: "))
except:
    print("Ошибка: введите корректный год.")
    exit()
current_year = datetime.now().year
age = current_year - birth_year
if age % 10 == 0:
    print(f"Вам сейчас {age} лет. Это юбилей!")
else:
    print(f"Вам сейчас {age} лет. Это не юбилей.")



# ülesane12

try:
    price = float(input("Введите цену товара в €: "))
except:
    print("Ошибка: введите корректное число.")
    exit()
if price <= 10:
    discount = price * 0.10 
else:
    discount = price * 0.20  
final_price = price - discount
print(f"Скидка составляет: {discount:.2f} €")
print(f"Итоговая цена товара: {final_price:.2f} €")


#ülesane13
gender = input("Введите ваш пол (м/ж): ")

if gender == "ж":
    print("Извините, в команду принимаются только мужчины.")
else:
    try:
        age = int(input("Введите ваш возраст: "))
        if 16 <= age <= 18:
            print("Вы подходите для команды! Добро пожаловать!")
        else:
            print("Извините, ваш возраст не подходит для команды.")
    except:
        print("Ошибка: введите корректный возраст.")


#ülesane14
try:
    num_people = int(input("Введите количество людей: "))
    bus_size = int(input("Введите количество мест в одном автобусе: "))
except:
    print("Ошибка: введите корректные целые числа.")
    exit()
if num_people <= 0 or bus_size <= 0:
    print("Ошибка: количество людей и размер автобуса должны быть положительными числами.")
else:
    num_buses = (num_people + bus_size - 1) // bus_size  
    last_bus_people = num_people % bus_size  
    if last_bus_people == 0:
        last_bus_people = bus_size
    print(f"Для перевозки {num_people} человек(а) потребуется {num_buses} автобус(а/ов).")
    print(f"В последнем автобусе будет {last_bus_people} человек(а).")
