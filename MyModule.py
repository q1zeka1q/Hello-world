import random
import string

kasutajad = ["kasutaja1", "kasutaja2"]
paroolid = ["Parool123!", "Salasona456*"]

def loo_parool():
    tegelased = string.ascii_letters + string.digits + ".,:;!_*-+()/#¤%&"
    parool = ''.join(random.choice(tegelased) for _ in range(12))
    return parool

def kontrolli_parooli(parool):
    return (any(c.isdigit() for c in parool) and
            any(c.islower() for c in parool) and
            any(c.isupper() for c in parool) and
            any(c in ".,:;!_*-+()/#¤%&" for c in parool))

def registreeri():
    kasutajanimi = input("Sisesta kasutajanimi: ")
    if kasutajanimi in kasutajad:
        print("Kasutajanimi on juba olemas!")
        return

    valik = input("Kas soovid automaatset parooli? (jah/ei): ").lower()
    if valik == "jah":
        parool = loo_parool()
        print(f"Sinu parool: {parool}")
    else:
        while True:
            parool = input("Sisesta parool: ")
            if kontrolli_parooli(parool):
                break
            print("Parool peab sisaldama suurtähti, väiketähti, numbreid ja erisümboleid!")

    kasutajad.append(kasutajanimi)
    paroolid.append(parool)
    print("Registreerimine õnnestus!")

def autoriseeri():
    kasutajanimi = input("Sisesta kasutajanimi: ")
    if kasutajanimi not in kasutajad:
        print("Kasutajat ei leitud!")
        return

    parool = input("Sisesta parool: ")
    if paroolid[kasutajad.index(kasutajanimi)] == parool:
        print("Sisselogimine õnnestus!")
    else:
        print("Vale parool!")

def muuda_andmeid():
    kasutajanimi = input("Sisesta kasutajanimi: ")
    if kasutajanimi not in kasutajad:
        print("Kasutajat ei leitud!")
        return

    indeks = kasutajad.index(kasutajanimi)
    uus_kasutajanimi = input("Sisesta uus kasutajanimi (jäta tühjaks, kui ei soovi muuta): ")
    if uus_kasutajanimi and uus_kasutajanimi not in kasutajad:
        kasutajad[indeks] = uus_kasutajanimi
        print("Kasutajanimi edukalt muudetud!")

    uus_parool = input("Sisesta uus parool (jäta tühjaks, kui ei soovi muuta): ")
    if uus_parool:
        while not kontrolli_parooli(uus_parool):
            print("Parool peab sisaldama suurtähti, väiketähti, numbreid ja erisümboleid!")
            uus_parool = input("Sisesta uus parool: ")
        paroolid[indeks] = uus_parool
        print("Parool edukalt muudetud!")

def taasta_parool():
    kasutajanimi = input("Sisesta kasutajanimi: ")
    if kasutajanimi not in kasutajad:
        print("Kasutajat ei leitud!")
        return

    indeks = kasutajad.index(kasutajanimi)
    uus_parool = loo_parool()
    paroolid[indeks] = uus_parool
    print(f"Sinu uus parool: {uus_parool}")