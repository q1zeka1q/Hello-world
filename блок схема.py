try:
    P = int(input("Введите количество чисел (P): ")) 
    if P <= 0:
        print("Количество чисел должно быть больше 0.")
    else:
        negative_sum = 0
        total_sum = 0
        for i in range(P):
            number = float(input(f"Введите число {i+1}: ")) 
            total_sum += number
            if number < 0:  
                negative_sum += number
        print(f"Сумма отрицательных чисел: {negative_sum}")
        print(f"Общая сумма чисел: {total_sum}") 
except:
    print("Ошибка ввода. Введите числовое значение.")
        

# 1. ülesane
N = int(input("Введите количество чисел: "))
max_num = int(input("Введите число: "))
for _ in range(N - 1):
    num = int(input("Введите число: "))
    if num > max_num:
        max_num = num
print(f"Максимальное число: {max_num}")

# 2. ülesane
while True:
    num = int(input("Введите число: "))
    if num == 13:
        print(77)
    else:
        print(num)

# 3. ülesane
distance = 10
sum_distance = 0
for day in range(7):
    sum_distance += distance
    distance *= 1.1
print(f"Суммарный путь спортсмена: {sum_distance:.2f} км")

# 4. ülesane
M = int(input("Введите длину ткани (в метрах): "))
while True:
    pikkus = int(input("Введите длину требуемого куска ткани: "))
    if pikkus > M:
        choice = input("Материала не хватает. Выкупить остаток? (да/нет): ")
        if choice.lower() == 'да':
            print(f"Продан остаток длиной {M} метров.")
            break
        else:
            print("Переход к следующему покупателю.")
            continue
    else:
        M -= pikkus
        print(f"Осталось ткани: {M} метров.")

        # 5. ülesane
while True:
    choice = input("Хотите вычислить площадь трапеции? (да/нет): ")
    if choice != 'да':
        break
    a = float(input("Введите длину основания a: "))
    b = float(input("Введите длину основания b: "))
    h = float(input("Введите высоту h: "))
    area = 0.5 * (a + b) * h
    print(f"Площадь трапеции: {area}")

# 6. ülesane
num = int(input("Введите целое число: "))
if num % 3 == 0:
    print("Число делится на 3 без остатка.")
else:
    print("Число не делится на 3 без остатка.")