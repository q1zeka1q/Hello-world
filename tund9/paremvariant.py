from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import time
import smtplib
import ssl
from email.message import EmailMessage

# Файл для черновиков и логов
DRAFT_FILE = "draft.txt"
LOG_FILE = "sent_log.txt"

# Функция для загрузки черновика
def load_draft():
    if os.path.exists(DRAFT_FILE):
        with open(DRAFT_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) >= 4:
                email_entry.insert(0, lines[0].strip())
                teema_entry.insert(0, lines[1].strip())
                lisa_entry.insert(0, lines[2].strip())
                kiri_box.insert("1.0", "".join(lines[3:]))

# Функция для сохранения черновика
def save_draft():
    with open(DRAFT_FILE, "w", encoding="utf-8") as file:
        file.write(email_entry.get() + "\n")
        file.write(teema_entry.get() + "\n")
        file.write(lisa_entry.get() + "\n")
        file.write(kiri_box.get("1.0", END))
    root.after(5000, save_draft)  # Автосохранение каждые 5 секунд

# Функция для выбора файлов
attachments = []
def vali_pilt():
    files = filedialog.askopenfilenames(title="Vali pildid", filetypes=[("All Files", "*.*")])
    if files:
        attachments.extend(files)
        lisa_entry.delete(0, END)
        lisa_entry.insert(0, ", ".join(attachments))

# Функция для предпросмотра письма
def preview_email():
    preview_text = f"Saaja: {email_entry.get()}\nTeema: {teema_entry.get()}\nKiri:\n{kiri_box.get('1.0', END)}\nManused: {lisa_entry.get()}"
    messagebox.showinfo("Eelvaade", preview_text)

# Функция для отправки письма
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
    sender_password = "dplq jefv axuu sygu" # Замените на ваш пароль приложения Gmail

    context = ssl.create_default_context()
    
    # Формируем письмо
    msg = EmailMessage()
    msg.set_content(kiri, subtype="plain", charset="utf-8")
    msg["Subject"] = teema
    msg["From"] = sender_email
    msg["To"] = kellele

    # Добавление вложений
    if attachments:
        for file in attachments:
            try:
                with open(file, "rb") as f:
                    file_data = f.read()
                    file_name = os.path.basename(file)
                    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
            except Exception as e:
                messagebox.showerror("Viga", f"Tõrge faili lisamisel: {file}\n{str(e)}")
                return

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, sender_password)
            server.send_message(msg)

        messagebox.showinfo("Edu!", "E-kiri saadetud!")
    except Exception as e:
        messagebox.showerror("Viga", f"E-kirja saatmine ebaõnnestus: {str(e)}")

# Очистка всех полей
def clear_fields():
    email_entry.delete(0, END)
    teema_entry.delete(0, END)
    lisa_entry.delete(0, END)
    kiri_box.delete("1.0", END)
    attachments.clear()

# Переключение темы
def toggle_theme():
    new_theme = "light" if root.tk.call("ttk::style", "theme", "use") == "clam" else "clam"
    root.tk.call("ttk::style", "theme", "use", new_theme)

root = Tk()
root.title("E-kirja saatmine")
root.geometry("450x350")

# Создание стилей ttk
style = ttk.Style()
style.theme_use("clam")

# Поля ввода
Label(root, text="EMAIL:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
email_entry = ttk.Entry(root, width=50)
email_entry.grid(row=0, column=1, pady=2)

Label(root, text="TEEMA:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
teema_entry = ttk.Entry(root, width=50)
teema_entry.grid(row=1, column=1, pady=2)

Label(root, text="LISA:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
lisa_entry = ttk.Entry(root, width=50)
lisa_entry.grid(row=2, column=1, pady=2)

Label(root, text="KIRI:").grid(row=3, column=0, sticky="w", padx=5, pady=2)
kiri_box = Text(root, width=38, height=6)
kiri_box.grid(row=3, column=1, pady=2)

# Кнопки
ttk.Button(root, text="LISA PILT", command=vali_pilt).grid(row=4, column=0, pady=5)
ttk.Button(root, text="EELVAADE", command=preview_email).grid(row=4, column=1, pady=5)
ttk.Button(root, text="SAADA", command=saada_kiri).grid(row=5, column=0, pady=5)
ttk.Button(root, text="PUHASTA", command=clear_fields).grid(row=5, column=1, pady=5)
ttk.Button(root, text="TEEMA", command=toggle_theme).grid(row=6, column=0, columnspan=2, pady=5)

# Прогресс-бар
progress_bar = ttk.Progressbar(root, mode="indeterminate", length=200)
progress_bar.grid(row=7, column=0, columnspan=2, pady=5)

# Автозагрузка черновика
load_draft()
save_draft()

root.mainloop()