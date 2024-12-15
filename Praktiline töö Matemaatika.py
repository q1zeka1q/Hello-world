print("Выберите сложность: Tase 1, Tase 2 или Tase 3")
raskus = int(input("Введите 1, 2 или 3: "))
õvastus = 0  
kui_palju_näiteid = 10  
for i in range(1, kui_palju_näiteid + 1):
    a = 0
    b = 0
    kasutame = ""
    õige_vastus = 0  
    if raskus == 1:
        a = i + 1
        b = i + 2
        õige_vastus = a + b
        kasutame = "+"
    elif raskus == 2:
        a = i * 2
        b = i
        õige_vastus = a - b
        kasutame = "-"
    elif raskus == 3:
        a = i + 2
        b = i
        õige_vastus = a * b
        kasutame = "*"
    else:
        print("Ошибка! Введите 1, 2 или 3.")
        break
    print(f"Пример {i}: {a} {kasutame} {b} = ?")
    teie_vastus = int(input("Ваш ответ: "))
    if teie_vastus == õige_vastus:
        print("Правильно!")
        õvastus += 1
    else:
        print(f"Ошибка! Правильный ответ: {õige_vastus}")
hinde_protsent = (õvastus / kui_palju_näiteid) * 100
if hinde_protsent < 60:
    hinne = "Hinne 2"
elif hinde_protsent < 75:
    hinne = "Hinne 3"
elif hinde_protsent < 90:
    hinne = "Hinne 4"
else:
    hinne = "Hinne 5"
print(f"Вы правильно решили {õvastus} из {kui_palju_näiteid} примеров.")
print(f"Ваша оценка: {hinne}")
