import json
import random
import copy

# Citire date din JSON
with open("date.json", "r") as f:
    data = json.load(f)

bancnote = sorted(data["bancnote"], key=lambda b: -b["valoare"])
produse = data["produse"]
valori = [b["valoare"] for b in bancnote]
stoc_initial = {b["valoare"]: b["stoc"] for b in bancnote}

# Programare dinamica cu stoc limitat
def calculeaza_rest(rest, stoc):
    MAX = float('inf')
    dp = [MAX] * (rest + 1)
    dp[0] = 0
    folosit = [{} for _ in range(rest + 1)]

    for valoare in valori:
        for r in range(rest, -1, -1):
            for k in range(1, stoc[valoare] + 1):
                suma = r - k * valoare
                if suma < 0 or dp[suma] == MAX:
                    break
                if dp[suma] + k < dp[r]:
                    dp[r] = dp[suma] + k
                    folosit[r] = folosit[suma].copy()
                    folosit[r][valoare] = k

    if dp[rest] == MAX:
        return None
    return folosit[rest]

# Simularea clientilor
def simuleaza_clienti():
    stoc = copy.deepcopy(stoc_initial)
    client_id = 1

    while True:
        produs = random.choice(produse)
        pret = produs["pret"]
        plata = pret + random.randint(1, 20)
        rest = plata - pret

        print(f"\nClient #{client_id}")
        print(f"Produs: {produs['nume']} | Pret: {pret} lei | Plata: {plata} lei | Rest: {rest} lei")

        solutie = calculeaza_rest(rest, stoc)

        if solutie is None:
            print("❌ Nu se poate oferi restul cu stocul actual.")
            print("Simularea se oprește.")
            break

        print("✅ Rest oferit cu bancnote:")
        for v in sorted(solutie.keys(), reverse=True):
            print(f"  {v} lei x {solutie[v]}")
            stoc[v] -= solutie[v]

        client_id += 1

# Rulează simularea
if __name__ == "__main__":
    simuleaza_clienti()
