import random
import string

# Alguses täidetud kasutajate ja paroolide nimekirjad
kasutajad = ["kasutaja1", "kasutaja2"]
paroolid = ["Parool123!", "Salasona456*"]

def kasutaja_haldus(tegevus):
    if tegevus == "registreeri":
        nimi = input("Sisesta kasutajanimi: ")
        if nimi in kasutajanimed:
            print("Selline kasutajanimi on juba olemas!")
            return
        parool = input("Sisesta parool või jäta tühjaks automaatseks genereerimiseks: ")
        if not parool:
            parool = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
            print(f"Sinu genereeritud parool: {parool}")
        kasutajanimed.append(nimi)
        paroolid.append(parool)
        print("Registreerimine õnnestus!")
    
    elif tegevus == "autoriseeri":
        nimi = input("Sisesta kasutajanimi: ")
        if nimi in kasutajanimed:
            indeks = kasutajanimed.index(nimi)
            if paroolid[indeks] == input("Sisesta parool: "):
                print("Sisselogimine õnnestus!")
            else:
                print("Vale parool!")
        else:
            print("Sellist kasutajat ei ole!")
    
    elif tegevus == "muuda_parooli":
        nimi = input("Sisesta kasutajanimi: ")
        if nimi in kasutajanimed:
            indeks = kasutajanimed.index(nimi)
            vana = input("Sisesta vana parool: ")
            if paroolid[indeks] == vana:
                uus_parool = input("Sisesta uus parool: ")
                paroolid[indeks] = uus_parool
                print("Parool on muudetud!")
            else:
                print("Vale parool!")
        else:
            print("Sellist kasutajat ei ole!")
    
    elif tegevus == "taasta_parool":
        nimi = input("Sisesta kasutajanimi: ")
        if nimi in kasutajanimed:
            indeks = kasutajanimed.index(nimi)
            uus_parool = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
            paroolid[indeks] = uus_parool
            print(f"Sinu uus parool on: {uus_parool}")
        else:
            print("Sellist kasutajat ei ole!")