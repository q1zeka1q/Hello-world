import os   #это модуль для работы с файлами и папками в операционной системе.
from random import sample

def loo_küsimused_fail():
    """Loob faili kusimused_vastused.txt koos küsimuste ja vastustega."""
    küsimused = [
        "Mis on for-tsükkel?:kordamine",
        "Mis on muutuja?:andmete hoidmise koht",
        "Mis on funktsioon?:koodilõik kindla ülesande täitmiseks",
        "Mis keel on kasutusel veebiarenduses?:HTML",
        "Mis on klass Pythoni keeles?:objektide loomise mall",
        "Mis on string?:tekstiline andmetüüp",
        "Mis on Pythoni laiend?:py",
        "Mis on andmebaas?:andmete salvestamise koht",
        "Mis on JSON?:andmevahetusformaat",
        "Mis on Git?:versioonihaldussüsteem"
    ]
    
    with open("kusimused_vastused.txt", "w", encoding="utf-8") as f:
        for küsimus in küsimused:
            f.write(küsimus + "\n")
    print("Fail 'kusimused_vastused.txt' on loodud koos küsimustega.")

def loe_failist(failinimi: str) -> dict:
    """Loeb küsimused ja vastused failist ning tagastab sõnastiku."""
    kus_vas = {}
    with open(failinimi, "r", encoding="utf-8") as f:
        for rida in f:
            küsimus, vastus = rida.strip().split(":")
            kus_vas[küsimus] = vastus
    return kus_vas

def salvesta_faili(failinimi: str, andmed: list):
    """Salvestab andmed faili."""
    with open(failinimi, "w", encoding="utf-8") as f:
        for rida in andmed:
            f.write(rida + "\n")

def küsi_küsimused(küsimused: dict, nimi: str) -> int:
    """Esitab kandidaadile 5 juhuslikku küsimust ja loendab õiged vastused."""
    õiged_vastused = 0
    valitud_küsimused = sample(list(küsimused.keys()), min(5, len(küsimused)))
    print(f"\nAlustame testi, {nimi}! Teil on {len(valitud_küsimused)} küsimust.")

    for küsimus in valitud_küsimused:
        vastus = input(f"{küsimus} ")
        if vastus.strip().lower() == küsimused[küsimus].strip().lower():
            print("Õige vastus!")
            õiged_vastused += 1
        else:
            print(f"Vale vastus! Õige vastus on: {küsimused[küsimus]}")
    
    return õiged_vastused

def peamine():
    """Peamine funktsioon kandidaatide testimiseks."""
    #Удаляет старый файл с вопросами, если он есть, и создаёт новый, чтобы обновить данные.
    if os.path.exists("kusimused_vastused.txt"):
        os.remove("kusimused_vastused.txt")
        print("Vana fail 'kusimused_vastused.txt' on kustutatud.")
    ###############################################################
    loo_küsimused_fail()

    küsimused = loe_failist("kusimused_vastused.txt")
    vastuvõetud = []
    mitte_sobivad = []

    while len(vastuvõetud) < 5:
        nimi = input("\nSisestage kandidaadi nimi (või 'lõpeta' lõpetamiseks): ")
        if nimi.lower() == "lõpeta":
            break

        õiged_vastused = küsi_küsimused(küsimused, nimi)
        print(f"{nimi} sai {õiged_vastused} õigesti vastatud küsimust.")

        if õiged_vastused >= 3:
            vastuvõetud.append((nimi, õiged_vastused))
        else:
            mitte_sobivad.append(nimi)

    vastuvõetud.sort(key=lambda x: -x[1])  
    mitte_sobivad.sort()

    salvesta_faili("vastuvõetud.txt", [f"{nimi}: {punktid} punkti" for nimi, punktid in vastuvõetud])
    salvesta_faili("eisoobi.txt", mitte_sobivad)

    print("\nVastuvõetud kandidaadid:")
    for nimi, punktid in vastuvõetud:
        print(f"{nimi} - {punktid} punkti")

    print("\nMitte sobivad kandidaadid:")
    for nimi in mitte_sobivad:
        print(nimi)

peamine()
