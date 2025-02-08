from isikukood import *
ikoodid=[] 
arvud=[]   


while True:
    try:
        ikood=input("\nSisestage isikukood (või sisestage 'X' lõpetamiseks): ")

        if ikood.lower()=="x":  
            break
        if not kontroll_pikkus(ikood):
            print("Isikukood peab sisaldama 11 numbrit!")
            arvud.append(ikood)
            continue
        aasta,kuu,paev=leia_synniaeg(ikood)
        if not kontroll_synniaeg(aasta,kuu,paev):
            print("Vale sünniaeg isikukoodis!")
            arvud.append(ikood)
            continue
        sunniaeg=f"{paev}.{kuu}.{aasta}"
        kontroll_num=int(ikood[10])
        jaak=leia_kontroll_nr(ikood)
        if jaak!=kontroll_num:  
            print("Vale kontroll number!")
            arvud.append(ikood)
            continue
        sunnikoht_num=int(ikood[7:10])
        sunnikoht=leia_sunnikoht(sunnikoht_num)
        if sunnikoht=="Tundmatu sünnikoht":
            print("Vale sünnikoht!")
            arvud.append(ikood)
            continue
        sugu=leia_sugu(ikood)


        print(f"See on {sugu}, tema sünnipäev on {sunniaeg}.\nSünnikoht on {sunnikoht}.")
        ikoodid.append(ikood)

    except:
        print("Sisestage isikukood!")

arvud.sort() 
ikoodid_naised=[ikood for ikood in ikoodid if int(ikood[0]) in {2,4,6}]

ikoodid_mehed=[ikood for ikood in ikoodid if int(ikood[0]) in {1,3,5}]
ikoodid=ikoodid_naised+ikoodid_mehed

print(f"\nÕiged isikukoodid: {ikoodid}")
print(f"\nVigased isikukoodid: {arvud}")
print()
