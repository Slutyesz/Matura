def f(x):
    print(f"\n{x}. Feladat")


#1. Feladat
f(1)

ToronyInputSor    = int(input("Adja meg a torony sorát (0-10): "))
ToronyInputOszlop = int(input("Adja meg a torony oszlopát (0-10): "))
ToronyHajoInput   = int(input("Adja meg a toronyból látható hajóknak a számát! "))

if ToronyHajoInput > 3:
    print("Nehéz torony.")


#2. Feladat
f(2)

for i in range(ToronyInputSor - 1, ToronyInputSor + 2):
    for j in range(ToronyInputOszlop - 1, ToronyInputOszlop + 2):
        if 1 <= i <= 10 and 1 <= j <= 10 and not (i == ToronyInputSor and j == ToronyInputOszlop):
            print(f"{i},{j}")


#3. Feladat
f(3)

feladvany = []

with open("feladvany.txt") as fbe:
    for line in fbe:
        feladvany.append(list(map(int, line.split())))

megoldas = []

with open("megoldas.txt") as mbe:
    m_db = int(mbe.readline().strip())
    
    for _ in range(m_db):
        nev = mbe.readline().strip()
        tabla = []

        for _ in range(10):
            tabla.append(list(map(int, mbe.readline().split())))
        megoldas.append({"nev": nev, "tabla": tabla})


RosszFeladvanyNevek = []

for m in megoldas:
    egyezik = True
    for sor in range(10):
        for oszlop in range(10):
            if 1 <= feladvany[sor][oszlop] <= 9:
                if m["tabla"][sor][oszlop] != feladvany[sor][oszlop]:
                    egyezik = False
    if not egyezik:
        RosszFeladvanyNevek.append(m["nev"])


if not RosszFeladvanyNevek:
    print("Mindegyik megoldás erre a heti feladatra érkezett.")
else:
    for nev in RosszFeladvanyNevek:
        print(nev)


#4. Feladat
f(4)

JoHetiMegoldasok = [m for m in megoldas if m["nev"] not in RosszFeladvanyNevek]
HibasHajoDB = 0

for o in JoHetiMegoldasok:
    hajok = sum(1 for sor in o["tabla"] for cella in sor if cella == 11)
    if hajok != 12:
        HibasHajoDB += 1

print(f"Hibás hajószámmal rendelkező megoldások száma: {HibasHajoDB}")


#5. Feladat
f(5)

SzabalytalanSzomszédDB = 0

for m in JoHetiMegoldasok:
    hajok = []

    for sor in range(10):
        for oszlop in range(10):
            if m["tabla"][sor][oszlop] == 11:
                hajok.append((sor, oszlop))

    if len(hajok) != 12:
        continue

    Hibas = False

    for sor, oszlop in hajok:
        for dsor in range(-1, 2):
            for doszlop in range(-1, 2):
                if dsor == 0 and doszlop == 0:
                    continue
                nsor, noszlop = sor + dsor, oszlop + doszlop

                if 0 <= nsor < 10 and 0 <= noszlop < 10:
                    szomszed = m["tabla"][nsor][noszlop]

                    if szomszed == 11 or (1 <= szomszed <= 9):
                        Hibas = True
        if Hibas: break
    if Hibas:
        SzabalytalanSzomszédDB += 1

print(f"Szabálytalan szomszédságú megoldások száma megfelelő hajószámmal: {SzabalytalanSzomszédDB} db.")


#6. Feladat
f(6)

HelyesNevek = []

for m in JoHetiMegoldasok:
    t = m["tabla"]
    HajokHelye = [(r, c) for r in range(10) for c in range(10) if t[r][c] == 11]

    if len(HajokHelye) != 12:
        continue

    
    SzomszedHiba = False

    for r, c in HajokHelye:
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = dr + r, dc + c
                
                if 0 <= nr < 10 and 0 <= nc < 10:
                    if t[nr][nc] == 11 or (1 <= t[nr][nc] <= 9):
                        SzomszedHiba = True
        if SzomszedHiba: break
    if SzomszedHiba: continue


    ToronyHiba = False

    for r in range(10):
        for c in range(10):
            if 1 <= t[r][c] <= 9:
                LathatoHajok = 0

                for i in range(10):
                    if t[r][i] == 11: LathatoHajok += 1

                for j in range(10):
                    if t[j][c] == 11: LathatoHajok += 1

                if LathatoHajok != t[r][c]:
                    ToronyHiba = True
                    break
        if ToronyHiba: break
    

    if not ToronyHiba:
        HelyesNevek.append(m["nev"])


for nev in HelyesNevek:
    print(nev)