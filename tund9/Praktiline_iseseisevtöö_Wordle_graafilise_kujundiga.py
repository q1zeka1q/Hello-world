from tkinter import *
from tkinter import Tk, Label, Entry, Button, messagebox
import random
from PIL import Image, ImageTk

# Файл со словами
sonad_file = "sonad.txt"

# Глобальные переменные
salasona = ""
katsete_arv = 0
kasutatud_tahed = {}  # Хранит статус букв
est_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜÕ"

def uuenda_tahed():
    """Обновляет цвета букв в панели алфавита"""
    for letter, label in tahe_labelid.items():
        if letter in kasutatud_tahed:
            label.config(bg=kasutatud_tahed[letter])
        else:
            label.config(bg="#555", fg="white")

def kontrolli():
    global katsete_arv
    if katsete_arv >= 6:
        return  
    
    sisestatud_sona = "".join([entry.get().upper() for entry in entries[katsete_arv]])
    
    if len(sisestatud_sona) != 6:
        messagebox.showwarning("Viga", "Palun sisesta täpselt 6 tähemärki!")
        return
    
    for i in range(6):
        entry = entries[katsete_arv][i]
        letter = sisestatud_sona[i]
        entry.config(disabledforeground="white")  
        
        if letter == salasona[i]:  
            entry.config(bg="green")
            kasutatud_tahed[letter] = "green"
        elif letter in salasona:  
            entry.config(bg="yellow")
            if kasutatud_tahed.get(letter, "black") != "green":
                kasutatud_tahed[letter] = "yellow"
        else:  
            entry.config(bg="black", fg="white")
            kasutatud_tahed[letter] = "black"
    
    uuenda_tahed()
    katsete_arv += 1  
    
    if sisestatud_sona == salasona:
        messagebox.showinfo("Võit!", "Tubli! Oled leidnud õige sõna!")
        return
    
    if katsete_arv == 6 and sisestatud_sona != salasona:
        messagebox.showinfo("Mäng läbi", f"Õige sõna oli: {salasona}")

def uus_mang():
    global salasona, entries, katsete_arv, kasutatud_tahed
    katsete_arv = 0  
    kasutatud_tahed = {}  
    try:
        with open(sonad_file, "r", encoding="utf-8") as file:
            sonad = [line.strip().upper() for line in file.readlines() if len(line.strip()) == 6]
        if not sonad:
            messagebox.showerror("Viga", "Failis нет 6-буквенных sõnu!")
            return
        salasona = random.choice(sonad)  
        print("Valitud sõna:", salasona)  
        
        for row in entries:
            for entry in row:
                entry.delete(0, END)
                entry.config(bg="#2C2F33", fg="white", state=NORMAL)
        
        uuenda_tahed()
    except FileNotFoundError:
        messagebox.showerror("Viga", "Faili 'sonad.txt' ei leitud!")

def lopeta():
    aken.destroy()

aken = Tk()
aken.geometry("700x700")
aken.title("Wordle")
aken.resizable(False, False)

original_image = Image.open(r"C:\\Users\\Admin\\Desktop\\visual studio работы\\Hello world\\tund9\\graffiti-mauer-700-27783381.jpg")
resized_image = original_image.resize((700, 700))
bgimage = ImageTk.PhotoImage(resized_image)

label_bg = Label(aken, image=bgimage)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

pealkiri = Label(aken, text="Wordle graafilise kujundiga", font=("Lucida Console", 24), fg="white", bg="black")
pealkiri.pack()

tainekiri = Label(aken, text="Hakkame mängu mängima", font=("Lucida Console", 14), bg="black", fg="white")
tainekiri.pack()

sisend = Frame(aken)
sisend.pack(pady=20)

entries = []
for i in range(6):
    rea_sisestused = []
    for j in range(6):
        sisesta_taht = Entry(sisend, width=4, font=("Lucida Console", 18, "bold"), justify="center", bg="#2C2F33", fg="white")
        sisesta_taht.grid(row=i, column=j, padx=2, pady=2, ipady=15)
        rea_sisestused.append(sisesta_taht)
    entries.append(rea_sisestused)

# Панель алфавита
tahted_frame = Frame(aken, bg="#444")
tahted_frame.pack(pady=10)

tahe_labelid = {}
for index, letter in enumerate(est_alphabet):
    label = Label(tahted_frame, text=letter, font=("Lucida Console", 16, "bold"), width=3, bg="#555", fg="white")
    label.grid(row=index // 10, column=index % 10, padx=2, pady=2)
    tahe_labelid[letter] = label

# Кнопки управления
Button(text="Kontrolli", font=("Lucida Console", 18), fg="white", bg="green", command=kontrolli).place(x=125, y=595) 
Button(text="Uus Mäng", font=("Lucida Console", 18), fg="white", bg="green", command=uus_mang).place(x=295, y=595) 
Button(text="Lõpeta", font=("Lucida Console", 18), fg="white", bg="red", command=lopeta).place(x=445, y=595) 

uus_mang()
aken.mainloop()