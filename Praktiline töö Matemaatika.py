print("Выберите сложность: Tase 1, Tase 2 или Tase 3")
raskus = int(input("Введите 1, 2 или 3: "))
õvastus = 0  
kui_palju_näiteid = 10  
for i in range(1, kui_palju_näiteid + 1):
    a = i + 1  
    b = i + 2
    kasutame = ""
    õige_vastus = 0  
    if raskus == 1:
        õige_vastus = a + b
        kasutame = "+"
    elif raskus == 2:
        if i % 2 == 0:  
            õige_vastus = a - b
            kasutame = "-"
        else:
            b = i  
            õige_vastus = a // b 
            kasutame = "/"
    elif raskus == 3:
        if i % 2 == 0:  
            õige_vastus = a * b
            kasutame = "*"
        else:
            õige_vastus = a ** 2
            kasutame = "**"
    else:
        print("Ошибка! Введите 1, 2 или 3.")
        break
    print(f"Пример {i}: {a} {kasutame} {b if kasutame != '**' else ''} = ?")
    teie_vastus = int(input("Ваш ответ: "))
    if teie_vastus == õige_vastus:
        print("Правильно!")
        õvastus += 1
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
