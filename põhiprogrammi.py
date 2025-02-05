import MyModule

if __name__ == "__main__":

    while True:
        print("\nVali tegevus:")
        print("1. Registreerimine")
        print("2. Autoriseerimine")
        print("3. Muuda nime või parooli")
        print("4. Taasta parool")
        print("5. Lõpeta")

        valik = input("Sisesta valik (1-5): ")

        if valik == '1':
            MyModule.registreeri()
        elif valik == '2':
            MyModule.autoriseeri()
        elif valik == '3':
            MyModule.muuda_andmeid()
        elif valik == '4':
            MyModule.taasta_parool()
        elif valik == '5':
            print("Programmi lõpetamine.")
            break
        else:
            print("Vale valik! Proovi uuesti.")