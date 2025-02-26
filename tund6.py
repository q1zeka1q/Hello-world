# #ülesane 1
# import string
# vokaali=["a", "e", "u", "o", "i", "ü", "ö", "ä"]
# konsonanti="qwrtpsdfghjklzxcvbnm"
# markid=string.punctuation  
# while True:
#     v=k=m=t=0
#     tekst=input("Sisesta mingi tekst: ").lower()
#     if tekst.isdigit():
#         break
#     else:
#         tekst_list=list(tekst)
#         print(tekst_list)
#         for taht in tekst_list:
#             if taht in vokaali:
#                 v+=1
#             elif taht in konsonanti:
#                 k+=1
#             elif taht in markid:
#                 m+=1
#             elif taht ==" ":
#                 t+=1
#     print ("Vookali: ", v)
#     print ("konsonanti: ", k)
#     print ("markid: ", m)
#     print ("Tühikud ",t)


#     #ülesane 2
# nimed=[]
# for i in range(5):
#     nimi=input(f"Sissesta nimi{i+1}: ")
#     nimed.append(nimi)
# print("Enne sorteerimist: ")
# print(nimed)
# nimed.sort()
# print("Pärast sorteerimist: ")
# print(nimed)
# print (f"Viimasena lisatud nimi on: {nimi}") 
# v=input("Kas muudame nimeid: ").lower()
# if v=="jah":
#     v=input("Nimi või positsioon: N/P").upper()
#     if v=="P":
#         print("Sisesta nimi asukoht")
#         v=int(input())
#         uus_nimi=input("Uus nimi: ")
#         nimed[v-1]=uus_nimi
#     else:
#         print("Sisesta nimi ")
#         vana_nimi=input("Vana nimi: ")
#         v=nimed.index(vana_nimi)
#         uus_nimi=input("Uus nimi: ")
#         nimed[v]=uus_nimi
#     print(nimed)
# # dublikat1
# dublta=list(set(nimed))
# print("Mitte korduv loetelu 1.variant")
# print(dublta)
# # dublikat1
# dublta=[]
# for nimi in nimed:
#     if nimi not in dublta:
#         dublta.append(nimi)
# print("Mitte korduv loetelu 2.variant")
# print(dublta)

# vanused = []
# for i in range(7):
#     vanus=int(input(f"{i+1}. Vanus: "))
#     vanused.append(vanus)
# print(f"Sisestatud vanused: {vanused}")
# print(max(vanused))
# print(min(vanused))
# print(sum(vanused)/len(vanused))



# #ülesane 3
# numbrid = [5, 8, 3, 12, 6]
# for numbrid in numbrid:
#     print("*" * numbrid)
# print()

#ülesane 4
#variant1
postiindeks = input("Sisesta postiindeks (5 numbrit): ")
if len(postiindeks) != 5: 
    print("Viga: postiindeks peab koosnema täpselt viiest numbrist.")
else:
    esimene_taht = postiindeks[0]
    if esimene_taht == "1":
        maakond = "Tallinn"
    elif esimene_taht == "2":
        maakond = "Narva, Narva-Jõesuu"
    elif esimene_taht == "3":
        maakond = "Kohtla-Järve"
    elif esimene_taht == "4":
        maakond = "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
    elif esimene_taht == "5":
        maakond = "Tartu linn"
    elif esimene_taht == "6":
        maakond = "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
    elif esimene_taht == "7":
        maakond = "Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
    elif esimene_taht == "8":
        maakond = "Pärnumaa"
    elif esimene_taht == "9":
        maakond = "Läänemaa, Hiiumaa, Saaremaa"
    else:
        maakond = "Tundmatu maakond"
    print(f"Maakond: {maakond}")
    if esimene_taht in ["1", "2", "3"]:
        print("Püsige kodus!")
    else:
        print("Kandke maske!")

#variant2
indexid = ["Tallinn", "Narva", "Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa", "Lääne-Virumaa", "Jõgevamaa", "Tartu linn", "Tartumaa", "Põlvamaa", "Võrumaa", "Valgamaa", "Viljandimaa", "Järvamaa", "Harjumaa", "Raplamaa", "Pärnumaa", "Läänemaa", "Hiiumaa", "Saaremaa"]
while 1:
    try:
        postiindeks=int(input("Postiindeks: "))
        if len(str(postiindeks))==5:
            break
        else:
            print("On vaja 5 sümboleit!!")
    except:
        print("!!!")
print("Postiindeksi analüüs: ")
index_list=list(str(postiindeks))
s1=int(index_list[0])
print(f"Postiindeks {postiindeks} on {indexid[s1-1]}")