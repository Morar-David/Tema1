import random


cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progress = ["_" for _ in cuvant_de_ghicit]


incercari_ramase = 6
litere_incercate = []


print("Cuvânt de ghicit:", " ".join(progress))
print(f"Încercări rămase: {incercari_ramase}")


while incercari_ramase > 0 and "_" in progress:

    litera = input("Introdu o literă: ").lower()


    if len(litera) != 1 or not litera.isalpha():
        print("Introduceți o singură literă validă.")
        continue
    elif litera in litere_incercate:
        print("Această literă a fost deja încercată.")
        continue
    else:
        litere_incercate.append(litera)


    if litera in cuvant_de_ghicit:
        for index, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progress[index] = litera
    else:
        incercari_ramase -= 1
        print("Litera nu este în cuvânt.")


    print("Cuvânt de ghicit:", " ".join(progress))
    print(f"Încercări rămase: {incercari_ramase}")


if "_" not in progress:
    print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvântul era:", cuvant_de_ghicit)








