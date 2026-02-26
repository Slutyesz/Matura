import math

adatok = []
EladottJegy, JáratHossz, TizAr = 0,0,0

with open("eladott.txt", "r", encoding="utf-8") as be:
    idx = 0

    for line in be:
        line = line.strip().split()
        utas = {}
        
        if idx == 0:
            EladottJegy  = int(line[0])
            JáratHossz   = int(line[1])
            TizAr        = int(line[2])
        else:
            utas["id"]   = idx
            utas["szam"] = int(line[0])
            utas["kezd"] = int(line[1])
            utas["lesz"] = int(line[2])
            adatok.append(utas)
        idx += 1
        
def f(x):
    print(f"\n{x}. Feladat")


#2. Feladat
f(2)

print(f"Az utosó vásárló sorszáma: {adatok[-1]['szam']}, és az általa beutazott táv: {adatok[-1]['lesz'] - adatok[-1]['kezd']} km.")


#3. Feladat
f(3)

for idx, line in enumerate(adatok, 1):
    if line["kezd"] == 0 and line["lesz"] == JáratHossz:
        print(idx,end=" ")
print()


#4. Feladat
f(4)

def jegyar(felszall, leszall, egyseg_ar):
    tav = leszall - felszall
    # Minden megkezdett 10 km számít
    egysegek = math.ceil(tav / 10)
    alapar = egysegek * egyseg_ar
    # Kerekítés 5-re: az utolsó számjegy alapján
    maradek = alapar % 10
    if maradek in [1, 2]: return alapar - maradek
    if maradek in [3, 4]: return alapar + (5 - maradek)
    if maradek in [6, 7]: return alapar - (maradek - 5)
    if maradek in [8, 9]: return alapar + (10 - maradek)
    return alapar

osszes_bevetel = sum(jegyar(a["kezd"], a["lesz"], TizAr) for a in adatok)
print(f"A társaság összes bevétele: {osszes_bevetel} Ft")


#5. Feladat
f(5)

UtolsoElotti = 0
FelLeCounter = 0

for line in adatok:
    if line["kezd"] > UtolsoElotti:
        UtolsoElotti = line["kezd"]

for line in adatok:
    if line["kezd"] == UtolsoElotti or line["lesz"] == UtolsoElotti:
        FelLeCounter += 1

print(f"Az utolsó elötti állomáson {FelLeCounter} ember szállt fel és le.")


#6. Feladat
f(6)

Megallohelyek = []

for line in adatok:
    if line["kezd"] not in Megallohelyek and line["kezd"] != 0:
        Megallohelyek.append(line["kezd"])
    if line["lesz"] not in Megallohelyek and line["lesz"] != JáratHossz:
        Megallohelyek.append(line["lesz"])

print(f"A kezdő és a végpont között összesen {len(Megallohelyek)} helyen áll meg a busz.")


#7. Feladat
f(7)

TavInput = int(input("Adjon meg egy távolságot (km): "))
MaxUlles = 0
Ulesek = {}

with open("kihol.txt", "w", encoding="utf-8") as ki:
    for ules in range(1,49):
        utas_id = "üres"
        for line in adatok:
            if line["szam"] == ules and line["kezd"] <= TavInput < line["lesz"]:
                utas_id = f"{line['id']}. utas"
                break
        ki.write(f"{ules}. ülés: {utas_id}\n")
