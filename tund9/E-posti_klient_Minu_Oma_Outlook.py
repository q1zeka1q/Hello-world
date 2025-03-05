import os
from tkinter import *
import smtplib, ssl, imghdr
from email.message import EmailMessage
from PIL import Image, ImageTk
from tkinter import Tk, Label, Entry, Text, Button, filedialog, messagebox

EMAIL_PASSWORD = "dplq jefv axuu sygu"
#vali_pilt() — открывает окно выбора изображения, сохраняет его путь и отображает в поле lisa_entry.
def vali_pilt():
    global file
    file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    lisa_entry.delete(0, "end")
    if file:
        lisa_entry.insert(0, file)
  #saada_kiri() — собирает данные из полей, создаёт email с текстом и вложением (если есть), затем отправляет его через Gmail SMTP.
def saada_kiri():
    kellele = email_entry.get().strip()
    teema = teema_entry.get().strip()
    kiri = kiri_box.get("1.0", "end").strip()

    if not kellele or not teema or not kiri:
        messagebox.showerror("Viga", "Palun täitke kõik väljad!")
        return

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "q1zeka1q@gmail.com"

    context = ssl.create_default_context()
    
    msg = EmailMessage()
    msg.set_content(kiri, subtype="plain", charset="utf-8")
    msg["Subject"] = teema
    msg["From"] = "q1zeka1q@gmail.com"
    msg["To"] = kellele
    
    if file:
        try:
            with open(file, "rb") as fpilt:
                pilt = fpilt.read()
                img_type = imghdr.what(None, pilt)
                if img_type:
                    msg.add_attachment(pilt, maintype='image', subtype=img_type)
                else:
                    messagebox.showwarning("Hoiatus", "Valitud fail ei ole toetatud pilt.")
        except Exception as e:
            messagebox.showerror("Viga", f"Pildi lugemine ebaõnnestus: {e}")
            return
    
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, EMAIL_PASSWORD)
            server.send_message(msg)
        messagebox.showinfo("Informatsioon", "Kiri oli saadetud!")
    except Exception as e:
        messagebox.showerror("Tekkis viga!", str(e))

def puhasta_vorm():
    email_entry.delete(0, END)  # 0, END - от начала до конца
    teema_entry.delete(0, END)
    kiri_box.delete("1.0", END)  # 1.0, END - с первой строки до конца
    lisa_entry.delete(0, END)  # Сбрасывает поле с путём картинки до '...'

# Создание GUI
root = Tk()
root.title("E-kirja saatmine")
root.geometry("400x300")
root.configure(bg="white")


# Поля для ввода
Label(root, text="EMAIL:", bg="darkgreen", fg="white", font=("Arial", 10, "bold"), width=10).grid(row=0, column=0, sticky="w", padx=5, pady=2)
email_entry = Entry(root, width=40, bg="#eef5e2")
email_entry.grid(row=0, column=1, pady=2)

Label(root, text="TEEMA:", bg="darkgreen", fg="white", font=("Arial", 10, "bold"), width=10).grid(row=1, column=0, sticky="w", padx=5, pady=2)
teema_entry = Entry(root, width=40, bg="#eef5e2")
teema_entry.grid(row=1, column=1, pady=2)

Label(root, text="LISA:", bg="darkgreen", fg="white", font=("Arial", 10, "bold"), width=10).grid(row=2, column=0, sticky="w", padx=5, pady=2)
lisa_entry = Entry(root, width=40, bg="#eef5e2")
lisa_entry.grid(row=2, column=1, pady=2)

Label(root, text="KIRI:", bg="darkgreen", fg="white", font=("Arial", 10, "bold"), width=10).grid(row=3, column=0, sticky="w", padx=5, pady=2)
kiri_box = Text(root, width=30, height=5, bg="#eef5e2")
kiri_box.grid(row=3, column=1, pady=2)

# Кнопки
Button(root, text="LISA PILT", command=vali_pilt, bg="darkgreen", fg="white", font=("Arial", 10, "bold"), width=12).grid(row=4, column=0, pady=10)
Button(root, text="SAADA", command=saada_kiri, bg="darkgreen", fg="white", font=("Arial", 10, "bold"), width=12).grid(row=4, column=1, pady=10)
Button(root, text="Kustuta", command=puhasta_vorm,bg="darkred", fg="white", font=("Arial", 10, "bold"), width=12).grid(row=5, column=1, pady=10)
root.mainloop()
