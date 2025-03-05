from tkinter import *
from tkinter import Tk, Label, Entry, Text, Button, filedialog, messagebox
import tkinter as tk
from tkinter import Entry
import app  
from PIL import Image, ImageTk


aken = Tk()
aken.geometry("700x700")
aken.title("Wordle")
aken.resizable(False, False)


def kontrolli():
    pass


def lahenda():
    pass



# Загружаем и изменяем размер изображения
original_image = Image.open(r"C:\Users\Admin\Desktop\visual studio работы\Hello world\tund9\graffiti-mauer-700-27783381.jpg")
resized_image = original_image.resize((700, 700))  # Размер должен соответствовать окну
bgimage = ImageTk.PhotoImage(resized_image)

label_bg=Label(aken, image=bgimage)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)


#Пишем заголовок
pealkiri = Label(aken, text="Wordle graafilise kujundiga", font=("Calibri", 24), fg="white", bg="#555", pady=20, width=40)
pealkiri.pack()

teinekiri = Label(aken, text="Hahame mängu mängima", bg="#555",fg="white", pady=20, width=30)
teinekiri.pack()

sisend=Frame(aken)
sisend.pack()


entries = []

for i in range(6):
    rea_sisestused = []
    for j in range(6):
        sisesta_taht = Entry(sisend, width=4, font=("Arial", 18, "bold"), justify="center", bg="#2C2F33", fg="white")
        sisesta_taht.grid(row=i, column=j, padx=2, pady=2, ipady=10)  #В tkinter ipady — это внутренний вертикальный отступ внутри виджета.
        rea_sisestused.append(sisesta_taht)
    entries.append(rea_sisestused)


Button(text="kontrolli", font=("Times New Roman", 18), fg="white",bg="green", command=kontrolli).place(x=235, y=495)    #.grid(row=5, column=0)
Button(text="lahenda", font=("Times New Roman", 18), fg="white",bg="green", command=lahenda).place(x=375, y=495) 


aken.mainloop()
