import os
import smtplib
import ssl
import imghdr
from email.message import EmailMessage
from tkinter import Tk, Label, Entry, Text, Button, filedialog, messagebox

file = None  # Инициализация переменной

EMAIL_PASSWORD = "dplq jefv axuu sygu"

def vali_pilt():
    global file
    file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    lisa_entry.delete(0, "end")
    if file:
        lisa_entry.insert(0, file)

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

# Создание GUI
root = Tk()
root.title("E-kirja saatmine")
root.geometry("400x300")
root.configure(bg="white")

# Стили
label_bg = "darkgreen"
label_fg = "white"
entry_bg = "#eef5e2"
button_bg = "darkgreen"
button_fg = "white"

# Поля для ввода
Label(root, text="EMAIL:", bg=label_bg, fg=label_fg, font=("Arial", 10, "bold"), width=10).grid(row=0, column=0, sticky="w", padx=5, pady=2)
email_entry = Entry(root, width=40, bg=entry_bg)
email_entry.grid(row=0, column=1, pady=2)

Label(root, text="TEEMA:", bg=label_bg, fg=label_fg, font=("Arial", 10, "bold"), width=10).grid(row=1, column=0, sticky="w", padx=5, pady=2)
teema_entry = Entry(root, width=40, bg=entry_bg)
teema_entry.grid(row=1, column=1, pady=2)

Label(root, text="LISA:", bg=label_bg, fg=label_fg, font=("Arial", 10, "bold"), width=10).grid(row=2, column=0, sticky="w", padx=5, pady=2)
lisa_entry = Entry(root, width=40, bg=entry_bg)
lisa_entry.grid(row=2, column=1, pady=2)

Label(root, text="KIRI:", bg=label_bg, fg=label_fg, font=("Arial", 10, "bold"), width=10).grid(row=3, column=0, sticky="w", padx=5, pady=2)
kiri_box = Text(root, width=30, height=5, bg=entry_bg)
kiri_box.grid(row=3, column=1, pady=2)

# Кнопки
Button(root, text="LISA PILT", command=vali_pilt, bg=button_bg, fg=button_fg, font=("Arial", 10, "bold"), width=12).grid(row=4, column=0, pady=10)
Button(root, text="SAADA", command=saada_kiri, bg=button_bg, fg=button_fg, font=("Arial", 10, "bold"), width=12).grid(row=4, column=1, pady=10)

root.mainloop()
