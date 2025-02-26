from random import *
import random 
def failist_to_dict(f: str):
    riik_pealinn={}  # sõnastik {"Riik": "Pealinn"}
    pealinn_riik={}  # sõnastik {"Pealinn": "Riik"}
    riigid = []  # järjend, kus talletakse riigide nimetused
    
    file = open(f, 'r', encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')  # k-võti, v-väärtus
        riik_pealinn[k] = v  # täidame riik_pealinn
        pealinn_riik[v] = k  # täidame pealinn_riik
        riigid.append(k)
    file.close()
    
    return riik_pealinn, pealinn_riik, riigid

def otsi(sõnastik, päring):
    """
    Поиск по словарю.
    """
    #ищет значение по слову в словаре
    if päring in sõnastik:
        return sõnastik[päring]
    return None


def lisa_kirje(sõnastik, riik, pealinn, failinimi):
    """
    Добавляет новую запись в словарь и сохраняет её в файл.
    """
    #выесняет если страны в файле если есть то нечего не добовляет если нету то добовляет в когнц списка
    if riik in sõnastik:
        print(f"Riik {riik} on juba sõnastikus.")
    else:
        sõnastik[riik] = pealinn
        print(f"Lisatud: {riik} - {pealinn}")
        with open(failinimi, 'a', encoding='utf-8') as file:
            file.write(f"{riik}-{pealinn}\n")


def uuenda_fail(failinimi, sõnastik):
    """
    Обновляет весь файл на основе текущего словаря.
    """
    #когда испровляется ошибка то текстовый файл обновляется
    with open(failinimi, 'w', encoding='utf-8') as file:
        for riik, pealinn in sõnastik.items():
            file.write(f"{riik}-{pealinn}\n")
    print("Fail uuendatud.")


def parandus(sõnastik, vana, uus, failinimi):
    """
    Исправляет название страны или столицы в словаре и обновляет файл.
    """
    #Ищет, что нужно исправить — название страны или название столицы.
    leidnud = False
    for riik, pealinn in list(sõnastik.items()):
        if riik.lower() == vana.lower():
            sõnastik[uus] = pealinn  # Добавляем новую страну с прежней столицей
            del sõnastik[riik]  # del это инструментом для удаления записи.
            leidnud = True
            print(f"Parandatud riik: {riik} -> {uus}")
        elif pealinn.lower() == vana.lower():    # Если столица совпадает с "vana"
            sõnastik[riik] = uus # Обновляем столицу для соответствующей страны
            leidnud = True
            print(f"Parandatud pealinn: {pealinn} -> {uus}")
    
    if leidnud:
        uuenda_fail(failinimi, sõnastik)
    else:
        print("Viga: kirjet ei leitud.")


def viktoriin(sõnastik):
    """
    Викторина по странам и столицам, максимум 10 вопросов.
    """
    if not sõnastik:
        print("Sõnastik on tühi, viktoriini ei saa alustada.")
        return

    küsimused = list(sõnastik.items())  # приврошает словарь в список пар (страна, столица)
    õiged = 0
    kokku = min(len(küsimused), 10)

    for i in range(kokku):
        riik, pealinn = küsimused[i]
        if choice([True, False]):  # Случайно выбираем тип вопроса
            vastus = input(f"Mis on riigi {riik} pealinn? ")
            if vastus.strip().lower() == pealinn.lower():
                print("Õige vastus!")
                õiged += 1
            else:
                print(f"Vale vastus. {riik} pealinn on {pealinn}.")
        else:
            vastus = input(f"Millise riigi pealinn on {pealinn}? ")
            if vastus.strip().lower() == riik.lower():
                print("Õige vastus!")
                õiged += 1
            else:
                print(f"Vale vastus. {pealinn} on {riik} pealinn.")
    
    tulemus = (õiged / kokku) * 100
    print(f"\nSul oli {õiged} õiget vastust {kokku}-st küsimusest. Tulemus: {tulemus:.2f}%")

