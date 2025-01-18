ikoodid = []
arvud = []

while True:
    kood = input("Sisesta isikukood (või STOP): ")

    if kood == "STOP":
        break

    if len(kood) != 11 or not kood.isdigit():
        print("Vale pikkus.")
        arvud.append(kood)
        continue

    if kood[0] not in "123456":
        print("Esimene number on vale.")
        arvud.append(kood)
        continue

    summa1 = 0
    kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    for i in range(10):
        summa1 += int(kood[i]) * kaal1[i]

    jaak = summa1 % 11

    if jaak == 10:
        summa2 = 0
        kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        for i in range(10):
            summa2 += int(kood[i]) * kaal2[i]
        jaak = summa2 % 11

    if jaak == 10:
        jaak = 0

    if jaak != int(kood[-1]):
        print("Kontrollnumber on vale.")
        arvud.append(kood)
        continue

    aasta_algus = {"1": "18", "2": "18", "3": "19", "4": "19", "5": "20", "6": "20"}
    aasta = aasta_algus[kood[0]] + kood[1:3]
    kuu = kood[3:5]
    paev = kood[5:7]
    jarjekord = int(kood[7:10])

    if jarjekord <= 10:
        haigla = "Kuressaare Haigla"
    elif jarjekord <= 19:
        haigla = "Tartu Ülikooli Naistekliinik"
    elif jarjekord <= 220:
        haigla = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif jarjekord <= 270:
        haigla = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif jarjekord <= 370:
        haigla = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif jarjekord <= 420:
        haigla = "Narva Haigla"
    elif jarjekord <= 470:
        haigla = "Pärnu Haigla"
    elif jarjekord <= 490:
        haigla = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif jarjekord <= 520:
        haigla = "Järvamaa Haigla (Paide)"
    elif jarjekord <= 570:
        haigla = "Rakvere, Tapa haigla"
    elif jarjekord <= 600:
        haigla = "Valga Haigla"
    elif jarjekord <= 650:
        haigla = "Viljandi Haigla"
    elif jarjekord <= 700:
        haigla = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        haigla = "Tundmatu haigla"

    sugu = "mees" if kood[0] in "135" else "naine"

    ikoodid.append((kood, sugu))
    print(f"See on {sugu}, sünniaeg {paev}.{kuu}.{aasta}, haigla {haigla}.")

arvud.sort()
ikoodid.sort(key=lambda x: (x[1] == "mees", x[0]))

print("\nÕiged koodid:")
for kood, _ in ikoodid:
    print(kood)

print("\nValed koodid:")
for kood in arvud:
    print(kood)
