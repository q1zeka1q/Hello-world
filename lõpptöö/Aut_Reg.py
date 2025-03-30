import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json
import difflib

# --- Lae failid --- #
paevamenyy = []
viimati_arvutatud = None
with open("lõpptöö/products.json", "r", encoding="utf-8") as f:
    tooted = json.load(f)

with open("lõpptöö/processing.json", "r", encoding="utf-8") as f:
    processing = json.load(f)

with open("lõpptöö/recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

tooted_all_nimed = list(tooted.keys()) + [v['ru'] for v in tooted.values()]
# --- Ajalugu --- #
ajalugu = []

# --- Funktsioon: leia toode --- #
def leia_toode(nimi):
    nimi = nimi.lower()
    for est, andmed in tooted.items():
        if nimi == est or nimi == andmed["ru"].lower():
            return est, andmed
    return None, None

# --- Lubatud töötlemisviisid --- #
diabeetikule_soovitatud = ["keeta", "aurutada", "hautada", "toorelt", "kuivatada", "lisada salatisse", "süüa toorelt"]

# --- arvuta: toitained --- #
def arvuta_toitained():
    nimi = toode_combobox.get().strip()
    kogus_str = kogus_entry.get().strip()

    if not nimi or not kogus_str:
        messagebox.showwarning("Viga", "Palun sisesta toode ja kogus grammides.")
        return

    try:
        kogus = float(kogus_str)
    except ValueError:
        messagebox.showerror("Viga", "Kogus peab olema arv.")
        return

    est_nimi, andmed = leia_toode(nimi)
    if not andmed:
        messagebox.showerror("Ei leitud", "Toodet ei leitud.")
        return

    if est_nimi not in ajalugu:
        ajalugu.insert(0, est_nimi)
        if len(ajalugu) > 10:
            ajalugu.pop()

    faktor = kogus / 100
    suhkur = round(andmed["suhkur"] * faktor, 2)
    sysivesikud = round(andmed["süsivesikud"] * faktor, 2)
    rasv = round(andmed["rasv"] * faktor, 2)
    kcal = round(andmed.get("kcal", 0) * faktor, 1)

    global viimati_arvutatud
    viimati_arvutatud = (est_nimi, kogus, suhkur, sysivesikud, rasv, kcal)

    maks_kogus = andmed.get("soovitatav_max", 100)
    ohutu = kogus <= maks_kogus

    tulemus_text.config(state="normal")
    tulemus_text.delete("1.0", tk.END)
    tulemus_text.insert(tk.END, f"Toode: {nimi.capitalize()} ({andmed['ru']})\n")
    tulemus_text.insert(tk.END, f"Kogus: {kogus} g\n")
    tulemus_text.insert(tk.END, f"Suhkur: {suhkur} g\n")
    tulemus_text.insert(tk.END, f"Süsivesikud: {sysivesikud} g\n")
    tulemus_text.insert(tk.END, f"Rasv: {rasv} g\n")
    tulemus_text.insert(tk.END, f"Energia: {kcal} kcal\n")

    if ohutu:
        tulemus_text.insert(tk.END, "\n✔️ See kogus on ohutu diabeetikule.\n")
    else:
        tulemus_text.insert(tk.END, f"\n⚠️ Soovituslik maksimaalne kogus: {maks_kogus} g.\n")
        tulemus_text.insert(tk.END, "⚠️ Antud kogus võib olla liigne diabeetikule.\n")

    tulemus_text.config(state="disabled")


# --- Kuva töötlemine --- #
def kuva_töötlemine():
    nimi = toode_combobox.get().strip().lower()
    est_nimi, andmed = leia_toode(nimi)
    if not est_nimi:
        messagebox.showerror("Viga", "Toodet ei leitud.")
        return

    protsessid = processing.get(est_nimi)
    if not protsessid:
        messagebox.showinfo("Info", "Selle toote kohta pole töötlemise andmeid.")
        return

    retsept_title.config(text=f"Töötlemine: {andmed['ru'].capitalize()}")

    for widget in töötlemine_info.winfo_children():
        widget.destroy()

    soovitatud = [p for p in protsessid if p in diabeetikule_soovitatud]

    if soovitatud:
        for protsess in soovitatud:
            btn = tk.Button(
                töötlemine_info,
                text=protsess.capitalize(),
                font=("Arial", 11, "bold"),
                bg="#FFECB3", fg="#000000",
                command=lambda p=protsess: kuva_retsept(est_nimi, p)
            )
            btn.pack(pady=3)
    else:
        lbl = tk.Label(
            töötlemine_info,
            text="⚠️ Töötlemisviisid pole soovitatud diabeetikutele.",
            font=("Arial", 11)
        )
        lbl.pack()

    töötlemine_retsept_label.config(text="")
    töötlemine_retsept_text.config(state="normal")
    töötlemine_retsept_text.delete("1.0", tk.END)
    töötlemine_retsept_text.config(state="disabled")

    retsept_frame.tkraise()


def kuva_retsept(toode, protsess):
    retsept = recipes.get(toode, {}).get(protsess)
    if not retsept:
        messagebox.showinfo("Retsept puudub", f"Sellele töötlemisviisile pole retsepti.")
        return

    töötlemine_retsept_label.config(text=retsept.get('title', f"Retsept: {protsess.capitalize()}"))
    töötlemine_retsept_text.config(state="normal")
    töötlemine_retsept_text.delete("1.0", tk.END)

    if isinstance(retsept, dict):
        sisu = ""
        sisu += f"\nKoostisosad:\n"
        for koostis in retsept['ingredients']:
            sisu += f"- {koostis}\n"
        sisu += f"\nJuhised:\n{retsept['instructions']}"
        töötlemine_retsept_text.insert(tk.END, sisu)
    else:
        töötlemine_retsept_text.insert(tk.END, str(retsept))

    töötlemine_retsept_text.config(state="disabled")


def tagasi_pealehele():
    main_frame.tkraise()
# --- Päevamenüü --- #
def lisa_paevamenyy(nimi, kogus, suhkur, sysivesikud, rasv, energia):
    paevamenyy.append({
        "nimi": nimi,
        "kogus": kogus,
        "suhkur": suhkur,
        "sysivesikud": sysivesikud,
        "rasv": rasv,
        "energia": energia
    })

def lisa_viimati_paevamenyy():
    if viimati_arvutatud:
        lisa_paevamenyy(*viimati_arvutatud)
        messagebox.showinfo("Lisatud", "Toode lisati päevamenüüsse.")
    else:
        messagebox.showwarning("Viga", "Arvuta toitaineid enne lisamist.")

# --- Näita päevamenüüd --- #
def kuva_paevamenyy():
    if not paevamenyy:
        messagebox.showinfo("Päevamenüü", "Päevamenüü on tühi.")
        return

    aken_menuu = tk.Toplevel(aken)
    aken_menuu.title("Päevamenüü")
    aken_menuu.geometry("600x600")
    aken_menuu.configure(bg=style_bg)



    tk.Label(aken_menuu, text="Päevamenüü", font=("Arial", 16, "bold"), bg=style_bg).pack(pady=10)

    raam = tk.Frame(aken_menuu, bg=style_bg)
    raam.pack(pady=5)


    total_suhkur = total_sys = total_rasv = total_kcal = 0

    def uuenda():
        for widget in raam.winfo_children():
            widget.destroy()

        for index, item in enumerate(paevamenyy):
            info = f"{item['nimi'].capitalize()} - {item['kogus']} g\n  Suhkur: {item['suhkur']} g | Süsivesikud: {item['sysivesikud']} g | Rasv: {item['rasv']} g | Energia: {item['energia']} kcal"
            rida = tk.Frame(raam, bg=style_bg)
            rida.pack(pady=2, fill="x")

            tk.Label(rida, text=info, bg=style_bg, anchor="w", justify="left").pack(side="left", padx=10)

            def eemalda(ind=index):
                paevamenyy.pop(ind)
                uuenda()

            tk.Button(rida, text="❌", fg="white", bg="red", font=("Arial", 10, "bold"), width=2, command=eemalda).pack(side="left")

        # Kokkuvõte
        nonlocal total_suhkur, total_sys, total_rasv, total_kcal
        total_suhkur = sum(x['suhkur'] for x in paevamenyy)
        total_sys = sum(x['sysivesikud'] for x in paevamenyy)
        total_rasv = sum(x['rasv'] for x in paevamenyy)
        total_kcal = sum(x['energia'] for x in paevamenyy)

        kokku_label.config(text=f"Kokku: Suhkur {round(total_suhkur, 2)} g | Süsivesikud {round(total_sys, 2)} g | Rasv {round(total_rasv, 2)} g | Kalorid {round(total_kcal, 1)} kcal")

    kokku_label = tk.Label(aken_menuu, font=("Arial", 12, "bold"), bg=style_bg)
    kokku_label.pack(pady=10)

    tk.Button(aken_menuu, text="Tühjenda menüü", bg="#f44336", fg="white", font=("Arial", 11, "bold"),
              command=lambda: (paevamenyy.clear(), uuenda())).pack(pady=10)

    uuenda()

def kuva_ajalugu():
    if not ajalugu:
        messagebox.showinfo("Ajalugu", "Ajalugu on tühi.")
        return

    aken_ajalugu = tk.Toplevel(aken)
    aken_ajalugu.title("Sisestatud toodete ajalugu")
    aken_ajalugu.geometry("300x300")
    tk.Label(aken_ajalugu, text="Viimased sisestused:", font=("Arial", 12, "bold")).pack(pady=10)

    for item in ajalugu:
        btn = tk.Button(
            aken_ajalugu,
            text=item.capitalize(),
            font=("Arial", 11),
            bg="#FFF3E0",
            relief="groove",
            command=lambda n=item: (toode_combobox.delete(0, tk.END), toode_combobox.insert(0, n), aken_ajalugu.destroy())
        )
        btn.pack(pady=3)

# --- Autocomplete funktsioon --- #
def update_autocomplete(event):
    typed = toode_combobox.get().lower()
    cursor_pos = toode_combobox.index(tk.INSERT)

    filtered = [item for item in tooted_all_nimed if item.lower().startswith(typed)]
    toode_combobox['values'] = filtered

    # Восстановить текст и курсор
    toode_combobox.delete(0, tk.END)
    toode_combobox.insert(0, typed)
    toode_combobox.icursor(cursor_pos)

    # Раскрыть список с задержкой, чтобы не терять фокус
    if filtered:
        toode_combobox.after(100, lambda: toode_combobox.event_generate('<Down>'))


def kustuta_andmed():
    toode_combobox.set("")               # очистка поля ввода
    kogus_entry.delete(0, tk.END)        # очистка поля граммов
    kogus_entry.insert(0, "10")          # вставка значения по умолчанию
    tulemus_text.config(state="normal")
    tulemus_text.delete("1.0", tk.END)   # очистка текста результата
    tulemus_text.config(state="disabled")

# --- GUI --- #
aken = tk.Tk()
aken.title("Toiduanalusaator")
aken.geometry("700x600")
aken.resizable(False, False)

main_frame = tk.Frame(aken, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

# --- Taustapilt --- #
try:
    taustapilt = Image.open(r"C:\Users\Admin\Desktop\visual studio работы\Hello world\lõpptöö\sook.jpg")
    taustapilt = taustapilt.resize((700, 600))
    taust_img = ImageTk.PhotoImage(taustapilt)
    taust_label = tk.Label(main_frame, image=taust_img)
    taust_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("Taustapildi laadimine ebaÕnnestus:", e)



# --- Стили и элементы UI --- #
style_bg = "#f4f7f6"
btn_green = "#43A047"
btn_blue = "#546E7A"
btn_orange = "#FB8C00"
btn_yellow = "#FFB300"
btn_white = "#FAFAFA"
font_label = ("Arial", 12)
font_btn = ("Arial", 11, "bold")

main_frame.configure(bg=style_bg)

tk.Label(main_frame, text="Diabeedi Toiduanalüsaator", font=("Arial", 26, "bold"),
         bg="#2E3B40", fg="white", padx=10, pady=10).grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")

tk.Label(main_frame, text="Toode (eesti või vene keeles):", font=font_label, bg=style_bg).grid(row=1, column=0, sticky="e", padx=5, pady=5)
toode_combobox = ttk.Combobox(main_frame, values=sorted(tooted.keys()), font=("Arial", 11), width=35)
toode_combobox.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)
toode_combobox.bind("<KeyRelease>", update_autocomplete)

tk.Label(main_frame, text="Kogus grammides:", font=font_label, bg=style_bg).grid(row=2, column=0, sticky="e", padx=5, pady=5)
kogus_entry = tk.Spinbox(main_frame, from_=10, to=1000, increment=5, font=("Arial", 11), width=10)
kogus_entry.grid(row=2, column=1, sticky="w", pady=5)

tk.Button(main_frame, text="Arvuta", font=font_btn, bg=btn_green, fg="white", width=15, relief="raised",
          activebackground="#2E7D32", activeforeground="white", bd=2, cursor="hand2", command=arvuta_toitained).grid(row=3, column=0, pady=10)

tk.Button(main_frame, text="Näita töötlemist", font=font_btn, bg=btn_blue, fg="white", width=15, relief="raised",
          activebackground="#37474F", activeforeground="white", bd=2, cursor="hand2", command=kuva_töötlemine).grid(row=3, column=1, pady=10)

tk.Button(main_frame, text="Näita ajalugu", font=font_btn, bg=btn_orange, fg="white", width=15, relief="raised",
          activebackground="#EF6C00", activeforeground="white", bd=2, cursor="hand2", command=kuva_ajalugu).grid(row=3, column=2, pady=10)

tulemus_text = tk.Text(main_frame, height=10, width=70, state="disabled", bg=btn_white, font=("Consolas", 10), relief="groove", bd=2)
tulemus_text.grid(row=4, column=0, columnspan=3, pady=10)

tk.Button(main_frame, text="Lisa päevamenüüsse", font=font_btn, bg=btn_yellow, fg="black", width=20, relief="raised",
          activebackground="#FBC02D", activeforeground="black", bd=2, cursor="hand2", command=lisa_viimati_paevamenyy).grid(row=5, column=0, columnspan=2, pady=5)

tk.Button(main_frame, text="Näita päevamenüüd", font=font_btn, bg=btn_orange, fg="white", width=20, relief="raised",
          activebackground="#E65100", activeforeground="white", bd=2, cursor="hand2", command=kuva_paevamenyy).grid(row=5, column=2, pady=5)

tk.Button(main_frame, text="Kustuta", font=("Arial", 10), width=8, height=1, 
          bg="#B0BEC5", fg="black", relief="raised",
          activebackground="#90A4AE", activeforeground="black", bd=1,
          command=kustuta_andmed).grid(row=4, column=3, padx=5, pady=10)


# --- Töötlemise ja retseptide aken --- #
retsept_frame = tk.Frame(aken, padx=20, pady=20)
retsept_frame.place(x=0, y=0, relwidth=1, relheight=1)

retsept_title = tk.Label(retsept_frame, text="Töötlemine", font=("Arial", 16, "bold"))
retsept_title.pack(pady=(0, 10))

töötlemine_info = tk.Frame(retsept_frame)
töötlemine_info.pack(pady=5)

töötlemine_retsept_label = tk.Label(retsept_frame, text="", font=("Arial", 13, "bold"))
töötlemine_retsept_label.pack(pady=(15, 5))

töötlemine_retsept_text = tk.Text(retsept_frame, width=70, height=10, wrap="word", font=("Arial", 11), state="disabled")
töötlemine_retsept_text.pack()

tk.Button(retsept_frame, text="⬅️ Tagasi", font=("Arial", 11, "bold"),bg=btn_green, fg="white", command=tagasi_pealehele).pack(pady=10)

main_frame.tkraise()
aken.mainloop()


