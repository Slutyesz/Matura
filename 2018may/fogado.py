Teachers = dict()

with open("fogado.txt", "r", encoding="utf-8") as be:
    for line in be:
        line = line.strip().split()
        nev = line[0] + " " + line[1]

        if nev in Teachers:
            Teachers[nev].append(line[2:])
        else:
            Teachers[nev] = [line[2:]]

def f(x):
    print(f"\n{x}. Feladat")


#2. Feladat
f(2)

print("\n2. Feladat\n"+f"A foglalások száma: {sum(len(v) for v in Teachers.values())}")


#3. Feladat
f(3)

TeacherInput = input("Adjon meg egy nevet: ")

if TeacherInput in Teachers:
    print(f"{TeacherInput} néven {len(Teachers[TeacherInput])} időpontfoglalás van.")
else:
    print("A megadott néven nincs időpontfoglalás.")


#4. Feladat
f(4)

IdopontInput = input("Adjon meg egy érvényes időpontot (pl. 17:10): ")
Slots = []

for teacher in Teachers:
    for slot in Teachers[teacher]:
        if IdopontInput in slot:
            Slots.append(teacher)

with open("adatok.txt","w", encoding="utf-8") as ki:
    for teacher in Slots:
        ki.write(teacher + "\n")


#5. Feladat
f(5)

legkorabbi=[]
for tanar in Teachers:
    legkorabbi.append((tanar, min(Teachers[tanar], key= lambda x:x[1])))
leg = (min(legkorabbi, key = lambda x:x[1][1]))
print('Tanár neve:',leg[0])
print('Foglalt időpont:', leg[1][0])
print('Foglalalás ideje:', leg[1][1])


#6. Feladat
f(6)

lehetséges = ['16:00','16:10','16:20','16:30','16:40','16:50','17:00','17:10','17:20','17:30','17:40','17:50']
foglalasai = [foglalt[0] for foglalt in Teachers["Barna Eszter"]]
szabad = set(lehetséges) - set(foglalasai)
print(*sorted(szabad), sep='\n')
print('Barna Eszter legkorábban távozhat:',end=' ')
print(lehetséges[lehetséges.index(max(foglalasai))+1])