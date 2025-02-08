from datetime import *


def kontroll_pikkus(ikood:str)->bool:
    """Kontrollib, kas isikukood on õige pikkusega.
    :param str ikood: Isikukood
    :rtype: bool
    """
    return len(ikood)==11

def kontroll_esimene_arv(ikood:str)->bool:
    """Kontrollib, kas isikukoodi esimene number on lubatud.
    :param str ikood: Isikukood
    :rtype: bool
    """
    esimene_arv=int(ikood[0])

    return esimene_arv in {1,2,3,4,5,6}

def leia_synniaeg(ikood: str)->any:
    """Leiab sünnikuupäeva isikukoodist.
    :param str ikood: Isikukood
    :rtype: tuple
    """
    esimene_arv=int(ikood[0])
    aasta=int(ikood[1:3])+(1800 if esimene_arv in {1,2} else 1900 if esimene_arv in {3,4} else 2000)
    kuu=int(ikood[3:5])
    paev=int(ikood[5:7])

    return aasta,kuu,paev

def kontroll_synniaeg(aasta:int,kuu:int,paev:int)->bool:
    """Kontrollib, kas sünnikuupäev on kehtiv ja mitte tulevikus.
    :param int aasta: Aasta
    :param int kuu: Kuu
    :param int paev: Päev
    :rtype: bool
    """
    try:
        synniaeg=datetime(aasta,kuu,paev)
        return synniaeg<=datetime.now()
    except:
        return False

def leia_kontroll_nr(ikood:str)->int:
    """Arvutab isikukoodi kontrollnumbri.
    :param str ikood: Isikukood
    :rtype: int
    """
    astme_kaal_1=[1,2,3,4,5,6,7,8,9,1]
    astme_kaal_2=[3,4,5,6,7,8,9,1,2,3]

    astme_summa_1=sum(int(ikood[i])*astme_kaal_1[i] for i in range (10))
    jaak=astme_summa_1%11  

    if jaak==10:  
        astme_summa_2=sum(int(ikood[i])*astme_kaal_2[i] for i in range (10)) 
        jaak=astme_summa_2%11    
        if jaak==10: 
            jaak=0  
    return jaak

def leia_sunnikoht(sunnikoht_num:int)->str:
    """Määrab sünnikoha isikukoodi järgi.
    :param int sünnikoht_num: Isikukoodi sünnikoha osa
    :rtype: str
    """
    haiglad=[
            [1,10,"Kuressaare Haigla"],
            [11,19,"Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"],
            [21,220,"Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"],
            [221,270,"Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"],
            [271,370,"Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"],
            [371,420,"Narva Haigla"],
            [421,470,"Pärnu Haigla"],
            [471,490,"Pelgulinna Sünнitusmaja (Tallinn), Haapsalu haigla"],
            [491,520,"Järvamaa Haigla (Paide)"],
            [521,570,"Rakvere, Tapa haigla"],
            [571,600,"Valga Haigla"],
            [601,650,"Viljandi Haigla"],
            [651,700,"Lõuna-Eesti Haigla (Võru), Põlva Haigla"]
    ]
    for alg,lopp,koht in haiglad:
        if alg<=sunnikoht_num<=lopp:
            return koht
    return "Tundmatu sünnikoht"

def leia_sugu(ikood:int)->str:
    """Määrab isiku soo.
    :param str ikood: Isikukood
    :rtype: str
    """
    esimene_arv=int(ikood[0])
    if esimene_arv in {1,3,5}:
        sugu="mees"
    else:
        sugu="naine"

    return sugu