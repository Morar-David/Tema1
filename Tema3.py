meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
pretmax=7

def afisare():
    while studenti:
        student=studenti.pop(0)
        comanda=comenzi.pop(0)
        meniu.remove(comanda)
        istoric_comenzi.append((student, comanda))
        print(f"{student} a comandat {comanda}.")
        tavi.pop()

def inventar():
    print(f"S-au comandat {10-meniu.count('papanasi')} papansai, {3-meniu.count('ceafa')} ceafa, {6-meniu.count('guias')} guias.")
    print(f"Mai sunt {len(tavi)} tavi.")
    print(f"Mai sunt papanasi: {bool(meniu.count('papanasi'))}. "
          f"Mai este ceafa: {bool(meniu.count('ceafa'))}. "
          f"Mai este guias: {bool(meniu.count('guias'))}.")

def finante():
    suma=(10-meniu.count('papanasi'))*preturi[0][1]+(3-meniu.count('ceafa'))*preturi[1][1]+(6-meniu.count('guias'))*preturi[2][1]
    print(f"Cantina a incasat: {suma} lei.")
    print(f"Produse care costa cel mult {pretmax} lei: ")
    for i in range(0,len(preturi)):
       if(preturi[i][1]<=pretmax):
           print(f"{preturi[i]}")

afisare()
inventar()
finante()