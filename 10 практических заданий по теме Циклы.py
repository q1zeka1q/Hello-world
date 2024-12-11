#ülesane 2
while True:
    try:
        a=int(input("Sisesta a: "))
        break #что бы прекротить цыкал
    except:
        print("On vaja naturalne arv")
summa=0
if a>0:
    for i in range(1,a+1,1):
        summa+=i #summa=summa+i
        print(f"{i}. samm summa={summa}")
print(f"Vastus {summa}") 

#ülesane 3
p=1
for j in range(8):
    while True:
        try:
            arv=float(input(f"Sissesta {j+1} arv: "))
            break #что бы прекротить цыкал
        except:
            print("On vaja arv")
    if arv>0: p*=arv
    print(f"{j}. samm korrutis= {p}")
    print(f"lõpptulemus on {p}")


#ülesane 4
for i in range (10,21,1):
    print(i**2, end=";")
print()

# ülesane 16
for j in range(1,10):
    for i in range(1,10):
        if i==j:
            print(j,end=" ")
        else:
            print("0", end=" ")
    print()
print()




#ülesane 15 Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
for rida in range(10):
    for veerg in range(10):
        print(veerg, end=" ")
    print()
print()


#ülesane 1  Вводят 15 чисел. Определить, сколько среди них целых.
a=0
for i in range(15):
    number = input("Введите число: ")
    try:
        if float(number):
            a += 1
    except:
        print("Это не целое число.")
print(f"Количество целых чисел: {a}")


#ülesane 17 Напишите программу, печатающую столбик таблицу умножения такого вида:
for i in range(1,9):
    a=2*i
    print(f"2*1={a}")
print()

#ülesane 18  Даны натуральные числа от 20 до 50. Напечатать те из них, которые делятся на 3, но не делятся на 5.
for i in range(20,50):
    if i%3==0 and i%5!=0:
        print(i, end=" ")
print()


# ülesane 19   Даны натуральные числа от 35 до 87. Найти и напечатать те из них, которые при делении на 7 дают остаток 1 2 или 5.

# variant1
for i in range(35,88):
    if  i%7==1 or i%7==2 or i%7==5:
        print(i, end=" ")
print()


# variant2
# Числа от 35 до 87
for number in range(35, 88):
    if number % 7 in {1, 2, 5}:
        print(number)


#ülesane 9
S = float(input("Введите сумму вклада (в евро): "))
N = int(input("Введите количество лет: "))
if S > 0 and N > 0:
    for year in range(1, N + 1):
        S += S * 0.03  
        print(f"Сумма вклада после {year}-го года: {S:.2f} евро")
else:
    print("Ошибка: сумма вклада и количество лет должны быть положительными числами.")

