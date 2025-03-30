from string import *
from time import sleep
from os import path, remove, system
from tkinter import simpledialog as sd
from gtts import *
import random
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Kirjeldus
    :param list kasutajad: Kirjeldus
    :param list paroolid: Kirjeldus
    :rtype: list,list
    """
    while True:
        nimi=input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                        #räägimine("Sinu kasutajanimi on "+nimi,"et")
                        #räägimine("Sinu salasõna on "+parool,"et")
                        saada_kiri()
                    break
                else:
                    räägimine("Nõrk salasõna!","et")
                    print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    #mail=sd.askstring("Kirjuta oma e-posti!","Kuhu saada kirja?")
    #email(mail)
    return kasutajad, paroolid
def räägimine(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas
        Nimi on järjendis kasutajad
        Salasõna on paroolide järjendis
        Nimi ja salasõna indeksid on võrdsed 
    :param list kasutajad:...
    :param list paroolid:...
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")              
        if nimi in kasutajad:            
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        break                   
                except:
                    print("Vale nimi või salasõna!")
                    if p==5: 
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
            break
        else:
            print("Kasutajat pole")

def nimi_või_parooli_muurmine(list_:list):
    """
    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list_
def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend

def taasta_parool():
    kasutajanimi = input("Sisesta kasutajanimi: ")
    if kasutajanimi not in kasutajad:
        print("Kasutajat ei leitud!")
        return

    indeks = kasutajad.index(kasutajanimi)
    uus_parool = loo_parool()
    paroolid[indeks] = uus_parool
    print(f"Sinu uus parool: {uus_parool}")

def kirjuta_failisse(fail:str,järjend=[]):
    """Salvestame tekst failisse
    """
    #n=int(input("Mitu: "))
    #for i in range(n):
    #    järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'w',encoding="utf-8")
    for element in järjend:
        f.write(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,'a')
    text=input("Sisesta tekst:")
    f.write(text+"\n")
    f.close()
def failide_kustutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")
def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":")# , - разделитель
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())
    
        #k,v=line.strip().split(":")
        #kus_vas[k]=v
        
    fail.close()
    return kus,vas #,kus_vas

import smtplib, ssl
from email.message import EmailMessage
def saada_kiri():
    kellele = input("Kellele: ")
    kiri = "Sa oled registreeritud."
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "q1zeka1q@gmail.com"
    password = "dplq jefv axuu sygu"
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = "E-kiri saatmine"  # from Entry
    msg['From'] = "Evgeniy Vasilev"
    msg['To'] = kellele

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        print("Informatsioon: kiri oli saadetud")
    except Exception as e:
        print("Tekkis viga!", e)
    finally:
        server.quit()
       
def genereeri_parool(pikkus=12)-> any:
    """Generereerib automaatselt parooli, mis sisaldab numbreid, tähti ja erimärke
    :param int pikkus: Parooli pikkus, vaikimisi 12 tähemärki
    :rtype: any: Tagastab genereeritud parooli
    """
    # Первый вариант кода из задания в moodle (так как создает более надежный пароль)
    str0=".,:;!_*-+()/#¤%&"
    str1='0123456789'
    str2='qwertyuiopasdfghjklzxcvbnm'
    str3=str2.upper()
    str4=str0+str1+str2+str3
    ls=list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    uus_parool=''.join([random.choice(ls) for x in range(12)])
    # Пароль готов

    return uus_parool

def saada_uus_parool(uus_parool):
    kellele = input("Kellele: ")
    kiri = (f"Teie uus parool: {uus_parool}")
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "q1zeka1q@gmail.com"
    password = "dplq jefv axuu sygu"
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = "Unustanud parooli taastamine"  # from Entry
    msg['From'] = "Evgeniy Vasilev"
    msg['To'] = kellele

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        print("Informatsioon: kiri oli saadetud")
    except Exception as e:
        print("Tekkis viga!", e)
    finally:
        server.quit()

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
    msg["From"] = sender_email
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
    email_entry.delete(0, END)
    teema_entry.delete(0, END)
    kiri_box.delete("1.0", END)
    lisa_entry.delete(0, END)

def vaheta_teema():
    global dark_mode
    dark_mode = not dark_mode
    root.configure(bg="#2E2E2E" if dark_mode else "white")
dark_mode = False