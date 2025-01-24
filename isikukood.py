# isikukood ilma def
ikoodid = []
arvud = []

while True:
    kood = input("Sisesta isikukood (või STOP): ")
    if kood == "STOP":
        break
    if len(kood) != 11 or not kood.isdigit():
        print("Vale pikkus.")
        arvud = arvud + [kood]  
    elif kood[0] not in "123456":
        print("Esimene number on vale.")
        arvud = arvud + [kood]
    else:
        kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        summa1 = 0
        for i in range(10):
            summa1 += int(kood[i]) * kaal1[i]
        jaak = summa1 % 11
        if jaak == 10:
            summa2 = 0
            for i in range(10):
                summa2 += int(kood[i]) * kaal2[i]
            jaak = summa2 % 11
        if jaak == 10:
            jaak = 0
        if jaak != int(kood[-1]):
            print("Isiskukood on vale.")
            arvud = arvud + [kood]
        else:
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
                haigla = "Ida-Tallinna Keskhaigla"
            elif jarjekord <= 270:
                haigla = "Ida-Viru Keskhaigla"
            elif jarjekord <= 370:
                haigla = "Maarjamõisa Kliinikum"
            elif jarjekord <= 420:
                haigla = "Narva Haigla"
            elif jarjekord <= 470:
                haigla = "Pärnu Haigla"
            elif jarjekord <= 490:
                haigla = "Pelgulinna Sünnitusmaja"
            elif jarjekord <= 520:
                haigla = "Järvamaa Haigla"
            elif jarjekord <= 570:
                haigla = "Rakvere, Tapa haigla"
            elif jarjekord <= 600:
                haigla = "Valga Haigla"
            elif jarjekord <= 650:
                haigla = "Viljandi Haigla"
            elif jarjekord <= 700:
                haigla = "Lõuna-Eesti Haigla"
            else:
                haigla = "Tundmatu haigla"
            sugu = "mees" if kood[0] in "135" else "naine"
            synnikuupaev = paev + "." + kuu + "." + aasta
            ikoodid = ikoodid + [(kood, sugu)]  
            print("See on", sugu, ", sünniaeg", synnikuupaev, ", haigla", haigla)
for i in range(len(arvud)):
    for j in range(len(arvud) - i - 1):
        if arvud[j] > arvud[j + 1]:
            arvud[j], arvud[j + 1] = arvud[j + 1], arvud[j]
ikoodid_naised = []
ikoodid_mehed = []
for kood, sugu in ikoodid:
    if sugu == "naine":
        ikoodid_naised = ikoodid_naised + [kood]
    else:
        ikoodid_mehed = ikoodid_mehed + [kood]
print("\nÕiged koodid:")
for kood in ikoodid_naised + ikoodid_mehed:
    print(kood)
print("\nValed koodid:")
for kood in arvud:
    print(kood)

# isikukood def
def töötle_kood(kood):
    """
    :param str kood: Личный код (isikukood), который нужно проверить. Должен состоять из 11 цифр.
    :rtype: Если код корректный, то указывается (пол, дата рождения, место рождения). Если код некорректный, возвращается строка с описанием ошибки.
    """
    kood = str(kood)

    if len(kood) != 11 or not kood.isdigit():
        vastus = "Vale pikkus."
    elif kood[0] not in "123456":
        vastus = "Esimene number on vale."
    else:
        kaalud1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        kaalud2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

        summa1 = sum(int(kood[i]) * kaalud1[i] for i in range(10))
        jaak = summa1 % 11

        if jaak == 10:
            summa2 = sum(int(kood[i]) * kaalud2[i] for i in range(10))
            jaak = summa2 % 11

        isikukood = 0 if jaak == 10 else jaak

        if isikukood != int(kood[-1]):
            vastus = "Isikukood on vale."
        else:
            algusaasta = {"1": "18", "2": "18", "3": "19", "4": "19", "5": "20", "6": "20"}
            aasta = algusaasta[kood[0]] + kood[1:3]
            kuu = kood[3:5]
            paev = kood[5:7]

            synnikuupaev = (f"{paev}.{kuu}.{aasta}")

            sugu = "mees" if kood[0] in "135" else "naine"

            jarjekord = int(kood[7:10])
            if jarjekord <= 10:
                haigla = "Kuressaare Haigla"
            elif jarjekord <= 19:
                haigla = "Tartu Ülikooli Naistekliinik"
            elif jarjekord <= 220:
                haigla = "Ida-Tallinna Keskhaigla"
            elif jarjekord <= 270:
                haigla = "Ida-Viru Keskhaigla"
            elif jarjekord <= 370:
                haigla = "Maarjamõisa Kliinikum"
            elif jarjekord <= 420:
                haigla = "Narva Haigla"
            elif jarjekord <= 470:
                haigla = "Pärnu Haigla"
            elif jarjekord <= 490:
                haigла = "Pelgulinna Sünnitusmaja"
            elif jarjekord <= 520:
                haigla = "Järvamaa Haigla"
            elif jarjekord <= 570:
                haigла = "Rakvere, Tapa haigla"
            elif jarjekord <= 600:
                haigла = "Valga Haigla"
            elif jarjekord <= 650:
                haigла = "Viljandi Haigla"
            elif jarjekord <= 700:
                haigла = "Lõuna-Eesti Haigла"
            else:
                haigла = "Tundmatu haigла"

            vastus = (sugu, synnikuupaev, haigla)

    return vastus


