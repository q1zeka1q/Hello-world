from random import *
# def summa3(arv1:int, arv2:int, arv3:int)->int:
#     """Tagastab kolme täisarvu summa 
#     :param int arv1: Esimine number
#     :param int arv2: Teine number
#     :param int arv3: Kolmas number
#     :rtype: int
#     """
#     summa=arv1+arv2+arv3
#     return summa

# Ülesane1
# def arithmetic(a1:float, a2:float, a3:str)->any:
#     """
#     :param foat a1: arrv1
#     :param foat a2: arrv2
#     :param str t:atitmeetiline tehing 
#     :rtype: var Määramata tüüp (float or str)
#     """
#     if a3=="+":
#         vastus=a1+a2
#     elif a3=="-":
#         vastus=a1-a2
#     elif a3=="*":
#         vastus=a1*a2
#     elif a3=="/":
#         vastus=a1/a2
#     else:
#       vastus="Неизвестная операция"
#     return vastus

#ülesane2
# def is_year_leap(aasta:int)->bool:
#     """
#     liigaasta
#     Tagastab true, kui liigaasta ja false kui on tavaline aasta
#     :parem int aasta: aasta number
#     :rtype: bool tagastab loogilised formadis tulemus
#     """
#     if aasta%4==0:
#         v=True
#     else:
#         v:False
#     return v



#ülesane3
# def square(külg: float):
#     """
#     Arvutab ruudu omadused: ümbermõõt, pindala ja diagonaal.
#     :param külg: ruudu külje pikkus
#     :rtype: (ümbermõõt, pindala, diagonaal)
#     """
#     ümbermõõt = 4 * külg
#     pindala = külg * külg
#     diagonaal = (2 ** 0.5) * külg
#     return ümbermõõt, pindala, diagonaal

#ülesane4
# def season(kuud: int)->str:
#     """
#     ::
#     :param kuud: Номер месяца (1–12)
#     :rtype: Время года (talv, kevad, suvi, sügis)
#     """
#     if kuud in (12, 1, 2):
#         vastus="talv"
#     elif kuud in (3, 4, 5):
#         vastus ="kevad"
#     elif kuud in (6, 7, 8):
#         vastus= "suvi"
#     elif kuud in (9, 10, 11):
#         vastus="sügis"
#     else:
#         vastus="Vigane kuu number"
#     return vastus

# # #ülesane5
# def bank (a:float, years:int)->float:
#     """
#     :param a: Начальная сумма вклада (евро)
#     :param years: Срок вклада (лет)
#     :rtype: Итоговая сумма на счету

#     """

#     for _ in range(years):
#         a +=a*0.10
#         return round (a, 2)

#ülesane6


# def is_prime(a=randint(0,1000))->bool:
#     """
#     :param x: Число от 0 до 1000
#     :rtype: True, если число простое, иначе False
#     """
#     print(a)
#     v=True
#     for i in range(2,a):
#         if a%i==0:
#             v=False
#     return v

#ülesane7
def date(päev: int, kuu: int, aasta: int) -> bool:
    """
    Kontrollib, kas antud kuupäev eksisteerib kalendris.

    :param päev: Päev (1-31)
    :param kuu: Kuu (1-12)
    :param aasta: Aasta (>0)
    :return: True, kui kuupäev on õige, muidu False
    """
    if päev in range(1, 31) and kuu in [1, 3, 5, 7, 8, 10, 12]:
        v = True
    elif päev in range(1, 29) and kuu == 2 and is_year_leap(aasta):  
        v = True
    elif päev in range(1, 30) and kuu in [4, 6, 9, 11]:
        v = True
    else:
        v = False
    return v
   

