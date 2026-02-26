Teachers = dict()
with open(r"2018may\fogado.txt", "r", encoding="utf-8") as be:
    for line in be: 
        line = line.strip().split()
        name = line[0] + " " + line[1]
        if name in Teachers: Teachers[name].append(line[2:])
        else: Teachers[name] = [line[2:]]
print("\n2. Feladat\n"+f"A foglalások száma: {sum(len(v) for v in Teachers.values())}" + "\n3. Feladat")
print(f"{name} néven {len(Teachers[name])} időpontfoglalás van." + "\n4. Feladat" if (name := input("Adjon meg egy nevet: ")) in Teachers else "A megadott néven nincs időpontfoglalás"+"\n4. Feladat\n")
print(*sorted(tname for tname, slots in Teachers.items() for slot in slots if time in slot), sep="\n") if (time := input("Adjon meg egy érvényes időpontot (pl. 17:10): ")) else None
print("5. Feladat\n" + f"Tanár neve: {(m:=min(((t,ti,b) for t,slots in Teachers.items() for ti,b in slots), key=lambda r: r[2]))[0]} " f"\nFoglalt időpont: {m[1]}\nFoglalás Ideje: {m[2]}")
print("6. Feladat\n" + "\n".join(sorted((all_times := {t for slots in Teachers.values() for t,_ in slots})- {t for t,_ in Teachers.get("Barna Eszter", [])}))+ f"\nlegkorábban: "+ (lambda t:f"{(int(t[:2]) + (int(t[3:]) + 10)//60):02d}:" f"{(int(t[3:]) + 10)%60:02d}")(max(Teachers.get("Barna Eszter", [["00:00"]]), key=lambda r: r[0])[0]))