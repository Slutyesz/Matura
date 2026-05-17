konyv = []

with open("book.txt") as book:
    for line in book:
        konyv.append(line.strip("\n"))

def f(x):
    print(f"\n{x}. Feladat")

f(1)    

for line in konyv:
    print(line)


f(2)

IsmInput = int(input("Kérem adja meg az ismétlések számát: "))

for line in konyv:
    print(IsmInput * f" {line} \t|", end="\n")


f(3)

def atalakit(sor):
    return "".join(int(sor[i]) * sor[i + 1] for i in range(0, len(sor), 2))


f(4)

with open("comp_c.txt") as comp:
    with open("szg.txt", "w") as ki:
        for line in comp:
            sor = atalakit(line.rstrip("\n"))
            print(sor)
            ki.write(f"{sor}\n")


f(5)

TomInput = input("Kérem adja meg a tömörített ábra fáljnevét: ")
NomInput = input("Kérem adja meg a tömörítetlen ábra fáljnevét: ")

with open(TomInput) as b1:
    CharCount = 0
    MaxChar = 0
    Lines = 0
    Block = 0
    for line in b1:
        Lines += 1
        Block += len(line) / 2
        if len(line) > MaxChar: MaxChar = len(line)
        line = line.strip()
        CharCount += len(line)
    print(f"A karakterek száma a törörítettállományban: {CharCount}")

with open(NomInput) as b2:
    CharCount2 = 0
    for line in b2:
        line = line.strip()
        CharCount2 += len(line)
    print(f"A karakterek száma a törörítettállományban: {CharCount2}")

print(round(CharCount / CharCount2, 2))


f(6)

print(f"Az ábra magassága sorokban: {Lines}")
print(f"Az ábra szélessége karakterekben: {MaxChar}")
print(f"A blokkok száma: {Block}")