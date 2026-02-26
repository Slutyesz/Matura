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

def Kerekites(x):   
    return 5 * round(x/5)

Bevetel = 0

for line in adatok:
    Bevetel += Kerekites(((line["lesz"] - line["kezd"])*TizAr))

print(f"A bevétele a társaságnak: {Bevetel} Ft")


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

for line in adatok:
    if line["szam"] > MaxUlles:
        MaxUlles = line["szam"]

for i in range(1, MaxUlles+1, 1):
    Ulesek[i] = "üres"

with open("kihol.txt", "w", encoding="utf-8") as ki:
    for idx, line in enumerate(adatok, 1):
        if TavInput > line["kezd"] and TavInput < line["lesz"] and TavInput == line["lesz"]:
            continue
        elif TavInput > line["kezd"] and TavInput < line["lesz"]:
            Ulesek[idx] = line["szam"]

    for ules in Ulesek:
        ki.write(f"{ules}. ülés: {Ulesek[ules]}\n")
