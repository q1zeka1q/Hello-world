import numpy as np  
import matplotlib.pyplot as plt  # Библиотека для графиков
from math import sqrt  

# Функция для решения квадратного уравнения (добавили D)
def lahenda_ruutvõrrand(a, b, c):
    d = b**2 - 4*a*c 

    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)  
        x2 = (-b - sqrt(d)) / (2 * a)  
        return f"D = {d:.2f}\nJuured: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif d == 0:
        x1 = -b / (2 * a)  
        return f"D = {d:.2f}\nÜks juur: x = {x1:.2f}"
    else:
        return f"D = {d:.2f}\nJuur puudub"  

# Функция для построения графика
def joonista_graafik(a, b, c):
    x = np.linspace(-10, 10, 400)  # Создаём 400 точек от -10 до 10
    y = a*x**2 + b*x + c 

    plt.figure(figsize=(6, 4))  # Создаём окно для графика
    plt.plot(x, y, label=f"{a}x** + {b}x + {c}")  # Рисуем параболу
    plt.axhline(0, color='black', linewidth=1)  # Горизонтальная линия
    plt.axvline(0, color='black', linewidth=1)  # Вертикальная линия
    plt.grid()  # Включаем сетку
    plt.show()  # Показываем график
