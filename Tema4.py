import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progress = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# 1. Afișarea șablonului inițial
print("Cuvânt de ghicit:", " ".join(progress))
print(f"Încercări rămase: {incercari_ramase}")

# 2. Bucla principală de joc
while incercari_ramase > 0 and "_" in progress:
    # a. Cere utilizatorului o literă
    litera = input("Introdu o literă: ").lower()

    # b. Verificarea validității
    if len(litera) != 1 or not litera.isalpha():
        print("Introduceți o singură literă validă.")
        continue
    elif litera in litere_incercate:
        print("Această literă a fost deja încercată.")
        continue
    else:
        litere_incercate.append(litera)

    # Verificare literei în cuvânt
    if litera in cuvant_de_ghicit:
        for index, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progress[index] = litera
    else:
        incercari_ramase -= 1
        print("Litera nu este în cuvânt.")

    # Afișarea progresului și încercărilor rămase
    print("Cuvânt de ghicit:", " ".join(progress))
    print(f"Încercări rămase: {incercari_ramase}")

# 3. Încheierea jocului
if "_" not in progress:
    print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvântul era:", cuvant_de_ghicit)








