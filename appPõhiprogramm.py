import tkinter as tk
from tkinter import Label, messagebox
import app  
from PIL import Image, ImageTk

# Функция проверки полей
def kontrolli_andmeid():
    kõik_täidetud = True 

    # Проверяем каждое поле
    for entry in [entry_a, entry_b, entry_c]:
        if entry.get().strip() == "":  # Если поле пустое
            entry.config(bg="red")  # Меняем фон на красный
            kõik_täidetud = False
        else:
            entry.config(bg="white") 

    return kõik_täidetud  

# Функция для кнопки "Lahenda"
def lahenda():
    if kontrolli_andmeid():  # Если все поля заполнены
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            # Вызываем функцию решения
            result = app.lahenda_ruutvõrrand(a, b, c)
            result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Viga", "Palun sisestage numbrid!")

# Функция для кнопки "Joonista"
def joonista():
    if kontrolli_andmeid():  # Если все поля заполнены
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            # Вызываем функцию построения графика
            app.joonista_graafik(a, b, c)
        except ValueError:
            messagebox.showerror("Viga", "Palun sisestage numbrid!")

# Создаём окно
root = tk.Tk()
root.title("Ruutvõrrandi lahendamine")
root.geometry("500x400")
root.configure(bg="lightgray") 
root.resizable(False, False)

# Загружаем и изменяем размер изображения
original_image = Image.open(r"C:\Users\Admin\Desktop\visual studio работы\Hello world\foni-papik-pro-bqex-p-kartinki-kletochka-na-prozrachnom-fone-13.png")
resized_image = original_image.resize((500, 400))  # Размер должен соответствовать окну
bgimage = ImageTk.PhotoImage(resized_image)

# Добавляем метку с фоновым изображением
labelLBG = Label(root, image=bgimage)
labelLBG.place(relwidth=1, relheight=1)  # Растягиваем фон на весь экран

# Заголовок
title_label = tk.Label(root, text="Ruutvõrrandi lahendamine", font=("Arial", 18, "bold"), fg="blue", bg="lightgray")
title_label.grid(row=0, column=0, columnspan=6, pady=10)

# Поля для ввода a, b, c
entry_a = tk.Entry(root, width=5, font=("Arial", 14))
entry_b = tk.Entry(root, width=5, font=("Arial", 14))
entry_c = tk.Entry(root, width=5, font=("Arial", 14))

# Размещение полей ввода
entry_a.grid(row=1, column=0, padx=5)
entry_b.grid(row=1, column=2, padx=5)
entry_c.grid(row=1, column=4, padx=5)

# Добавляем текст между полями
label_x2 = tk.Label(root, text="x** +", font=("Arial", 14), bg="lightgray")
label_x = tk.Label(root, text="x +", font=("Arial", 14), bg="lightgray")
label_eq = tk.Label(root, text="= 0", font=("Arial", 14), bg="lightgray")

# Размещаем текст между полями
label_x2.grid(row=1, column=1, padx=5)
label_x.grid(row=1, column=3, padx=5)
label_eq.grid(row=1, column=5, padx=5)

# Кнопка "Lahenda"
solve_button = tk.Button(root, text="Lahenda", command=lahenda, font=("Arial", 12), bg="green", fg="white")
solve_button.grid(row=2, column=0, columnspan=6, pady=5)

# Кнопка "Joonista"
graph_button = tk.Button(root, text="Joonista", command=joonista, font=("Arial", 12), bg="blue", fg="white")
graph_button.grid(row=3, column=0, columnspan=6, pady=5)

# Поле для результата
result_label = tk.Label(root, text="Sisestage koefitsiendid", font=("Arial", 14), fg="blue", bg="yellow")
result_label.grid(row=4, column=0, columnspan=6, pady=10)

# Запускаем окно
root.mainloop()
