import MyModule

while True:
    print("\nVali tegevus:")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Parooli muutmine")
    print("4 - Unustatud parooli taastamine")
    print("5 - Lõpetamine")
    valik = input("Sisesta valik: ")
    if valik == "1":
        MyModule.kasutaja_haldus("registreeri")
    elif valik == "2":
        MyModule.kasutaja_haldus("autoriseeri")
    elif valik == "3":
        MyModule.kasutaja_haldus("muuda_parooli")
    elif valik == "4":
        MyModule.kasutaja_haldus("taasta_parool")
    elif valik == "5":
        print("Programmi lõpetamine...")
        break
    else:
        print("Vale valik, proovi uuesti!")
