adatok = []

with open("kiadas.txt", "r", encoding="utf-8") as be:
    for line in be:
        line = line.strip().split(";")
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[-1] = int(line[-1])

        adatok.append(line)

def f(x):
    print(f"\n{x}. Feladat:")


f(2)

SzerzoInput = input("Szerző: ")
SzerzoInputCounter = 0

for line in adatok:
    if SzerzoInput.upper() in line[3].upper():
        SzerzoInputCounter += 1
        continue

if SzerzoInputCounter > 0:
    print(f"{SzerzoInputCounter} könyvkiadás")
else:
    print("Nem adtak ki")


f(3)

Sortedadatok = sorted(adatok, key=lambda x: x[-1], reverse=True)
MaxKiad = Sortedadatok[0][-1]
MaxKiadDB = 0

for line in Sortedadatok:
    if line[-1] == MaxKiad:
        MaxKiadDB += 1

print(f"Legnagyobb példányszám: {MaxKiad}, előfordul {MaxKiadDB} alkalommal")


f(4)

ElsoKFLine = None

for line in adatok:
    if line[2] == "kf" and line[-1] > 40000:
        ElsoKFLine = line
        break

print(f"{ElsoKFLine[0]}/{ElsoKFLine[1]}. {ElsoKFLine[3]}")


f(5)

Eredmenyek = {}

for line in adatok:
    Ev = line[0]
    if Ev not in Eredmenyek.keys():
        Eredmenyek[Ev] = {
            "MK": 1 if line[2] == "ma" else 0,
            "MP": line[-1] if line[2] == "ma" else 0,
            "KK": 1 if line[2] == "kf" else 0,
            "KP": line[-1] if line[2] == "kf" else 0
        }
    elif line[2] == "ma":
        Eredmenyek[Ev]["MK"] += 1
        Eredmenyek[Ev]["MP"] += line[-1]
    else:
        Eredmenyek[Ev]["KK"] += 1
        Eredmenyek[Ev]["KP"] += line[-1]

print("Év\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám")
for ev in Eredmenyek.keys():
    print(f"{ev}\t\t{Eredmenyek[ev]['MK']}\t\t{Eredmenyek[ev]['MP']}\t\t{Eredmenyek[ev]['KK']}\t\t{Eredmenyek[ev]['KP']}")

with open("tabla.html","w", encoding="utf-8") as ki:
    ki.write("<table>\n<tr><th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldi kiadás</th><th>Külföldi példányszám</th></tr>\n")
    for ev in Eredmenyek.keys():
        ki.write(f"<tr><td>{ev}</td><td>{Eredmenyek[ev]['MK']}</td><td>{Eredmenyek[ev]['MP']}</td><td>{Eredmenyek[ev]['KK']}</td><td>{Eredmenyek[ev]['KP']}</td></tr>\n")
    ki.write("</table>")


f(6)

Konyvek = {}
print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek:")

for line in adatok:
    cím = line[3]
    év = line[0]
    példányszám = line[-1]
    if cím not in Konyvek:
        Konyvek[cím] = []
    Konyvek[cím].append((év, példányszám))

for cím, kiadások in Konyvek.items():
    kiadások.sort(key=lambda x: x[0])
    első_példányszám = kiadások[0][1]
    újrakiadások = sum(1 for év, psz in kiadások[1:] if psz > első_példányszám)
    if újrakiadások >= 2:
        print(cím)
# SortedKonyvek = sorted(Konyvek, key=lambda x: x["C"], reverse=True)

# for cím in SortedKonyvek.keys():
#     if SortedKonyvek[cím]["C"] < 2:
#         break
#     else:
#         print(cím)