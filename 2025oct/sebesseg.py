adatok = []

with open("ut.txt") as be:
    TotalDistance = int(be.readline())
    for line in be:
        line = line.strip().split()
        line[0] = int(line[0])
        try:
            line[1] = int(line[1])
            adatok.append(line)
        except Exception:
            adatok.append(line)



def f(x):
    print(f"\n{x}. Feladat")


f(2)

for line in adatok:
    if "Varos" in str(line[1]):
        print(line[1])


f(3)

VizsgaltInput = float(input("Adja meg a vizsgált szakasz hosszátt km-ben! "))
VizsgalandoSzakasz = VizsgaltInput * 1000
CurrentSpeedMin = 90
CurrentSpeedLimit = 90
InVaros = False

for line in adatok:
    if line[0] > VizsgalandoSzakasz:
        break
    
    if isinstance(line[1], str):
        if line[1] == "]":
            InVaros = False
        elif 4 <= len(line[1]) <= 30:
            InVaros = True
    
    if isinstance(line[1], int):
        CurrentSpeedLimit = line[1]
    elif line[1] == "#" or line[1] == "%":
        CurrentSpeedLimit = 50 if InVaros else 90
    elif isinstance(line[1], str) and 4 <= len(line[1]) <= 30:
        CurrentSpeedLimit = 50
    elif line[1] == "]":
        CurrentSpeedLimit = 90
    
    if CurrentSpeedLimit < CurrentSpeedMin:
        CurrentSpeedMin = CurrentSpeedLimit

print(f"Az első {VizsgaltInput} km-en {CurrentSpeedMin} km/h volt a legalacsonyabb megengedett sebesség.")


f(4)

InVarosDistance = 0
LastCityStart = 0

for line in adatok:
    if 4 <= len(str(line[1])) <= 30:
        LastCityStart = line[0]

    if line[1] == "]":
        InVarosDistance += (line[0] - LastCityStart)

print(f"Az út {round(InVarosDistance/TotalDistance * 100, 2)} százaléka vezet településen belül.")


f(5)

VarosInput = input("Adja meg egy település nevét! ")
InVarosInput = False
SebKorTDB = 0
VarosInputStart = 0

for line in adatok:
    if InVarosInput and str(line[1]) == "]":
        VarosInputDistance = line[0] - VarosInputStart
        break

    if str(line[1]).upper() == VarosInput.upper():
        InVarosInput = True
        VarosInputStart = line[0]

    if InVarosInput and isinstance(line[1], int):
        SebKorTDB += 1

print(f"A sebességkorlátozó táblák száma: {SebKorTDB}")
print(f"Az út hossza a településen belül {VarosInputDistance} méter.")


f(6)

# Gyűjtjük össze a településeket
cities = []
current_city = None
for line in adatok:
    if isinstance(line[1], str) and 4 <= len(line[1]) <= 30 and line[1] not in ["#", "%", "]"]:
        if current_city is None:
            current_city = {"name": line[1], "start": line[0]}
    elif line[1] == "]" and current_city is not None:
        current_city["end"] = line[0]
        cities.append(current_city)
        current_city = None

# Megkeressük a beolvasott települést
idx = None
for i, city in enumerate(cities):
    if city["name"].upper() == VarosInput.upper():
        idx = i
        break

if idx is None:
    print("A megadott település nem található.")
else:
    # Számoljuk a távolságokat a szomszédokhoz
    dist_prev = float('inf')
    dist_next = float('inf')
    prev_name = None
    next_name = None
    
    if idx > 0:
        prev_city = cities[idx - 1]
        dist_prev = cities[idx]["start"] - prev_city["end"]
        prev_name = prev_city["name"]
    
    if idx < len(cities) - 1:
        next_city = cities[idx + 1]
        dist_next = next_city["start"] - cities[idx]["end"]
        next_name = next_city["name"]
    
    # Meghatározzuk a legközelebbit
    if dist_prev < dist_next:
        closest = prev_name
    elif dist_next < dist_prev:
        closest = next_name
    else:
        # Ha egyenlő, akkor a kezdőponthoz közelebbit, ami az előző
        closest = prev_name if prev_name else next_name
    
    print(f"A legközelebbi település: {closest}")
