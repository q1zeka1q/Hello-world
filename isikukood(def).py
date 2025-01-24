from isikukood import *
ikoodid = []
arvud = []

while True:
    kood = input("Sisesta isikukood (või STOP): ")
    if kood.upper() == "STOP":
        break
    tulemus = töötle_kood(kood)
    if isinstance(tulemus, str):
        print(tulemus)
        arvud.append(kood)
    else:
        sugu, synnikuupaev, haigla = tulemus
        ikoodid.append((kood, sugu))
        print(f"See on {sugu}, tema sünniaeg on {synnikuupaev}, haigla: {haigla}.")
