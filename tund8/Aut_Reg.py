from MinuOmaMoodul import *
#C:/Users/marina.oleinik/source/repos/Aut_Reg/Salasõnad.txt
salasõnad=loe_failist("parolid.txt")
kasutajanimed=loe_failist("kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine\n")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
        kirjuta_failisse('kasutajad.txt' ,kasutajanimed)
        kirjuta_failisse('parolid.txt' ,salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad")
        if vastus=="nimi":
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
        elif vastus=="mõlemad":
            print("Nimi muutmine: ")
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
            print("Parooli muutmine: ")
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
    elif vastus == 4:
        print("Unustatud parooli taastamine")
        vana_login = input("Sisestage kasutajanimi: ")
        if vana_login not in kasutajanimed:
            print("Kasutajanimi ei leitud. Proovige uuesti!")
        else:
            index_parool = kasutajanimed.index(vana_login)
            uus_parool = genereeri_parool()
            salasõnad.pop(index_parool)
            salasõnad.insert(index_parool, uus_parool)
            kirjuta_failisse('kasutajad.txt', kasutajanimed)
            kirjuta_failisse('paroolid.txt', salasõnad)
            print(f"Teie uus parool: {uus_parool}")
            saada_uus_parool(uus_parool)  # Отправляет новый пароль на почту

    elif vastus==5:
        print("Lõpetamine")

        break
    else:
        print("Tundmatu valik")
