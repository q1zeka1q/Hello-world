from tund8_Euroopa_riigid import *

riik_pealinn, pealinn_riik, riigid = failist_to_dict("riigid_pealinnad.txt")
riigid = list(riik_pealinn.keys())

print("Riigid:", riigid)
print("Pealinnad:", list(riik_pealinn.values()))

while True:
    print("\nVali tegevus:")
    print("1 – Otsi riik/pealinn")
    print("2 – Lisa uus kirje")
    print("3 – Paranda kirjet")
    print("4 – Alusta viktoriini")
    print("0 – Välju")

    valik = input("Sisesta valik: ")
    
    if valik == "1":
        päring = input("Sisesta riigi või pealinna nimi: ")
        tulemus = otsi(riik_pealinn, päring) or otsi(pealinn_riik, päring)
        if tulemus:
            print(f"Tulemus: {päring} -> {tulemus}")
        else:
            print("Sellist kirjet ei leitud.")
    
    elif valik == "2":
        riik = input("Sisesta riigi nimi: ")
        pealinn = input("Sisesta pealinna nimi: ")
        lisa_kirje(riik_pealinn, riik, pealinn, "riigid_pealinnad.txt")
        pealinn_riik[pealinn] = riik
    
    elif valik == "3":
        vana = input("Sisesta vale väärtus (riik või pealinn): ")
        uus = input("Sisesta uus väärtus: ")
        parandus(riik_pealinn, vana, uus, "riigid_pealinnad.txt")
    
    elif valik == "4":
        viktoriin(riik_pealinn)
    
    elif valik == "0":
        print("Programmist väljutakse.")
        break
    
    else:
        print("Vale valik. Proovi uuesti.")