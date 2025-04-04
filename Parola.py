import random
import csv
import os

# Restul codului de inițializare a constantelor și claselor...

database = HashTable()

csv_filename = "cnp_data.csv"
all_cnp = []  # Inițializează variabila înaintea blocului try

try:
    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Sare peste header

        for row in reader:
            cnp, first_name, last_name = row
            database.insert(cnp, first_name, last_name)
            all_cnp.append(cnp)

except FileNotFoundError:
    print(f"Fișierul {csv_filename} nu a fost găsit. Asigură-te că ai generat CSV-ul corect.")

if all_cnp:  # Verificăm dacă all_cnp nu este gol
    selected_cnp = random.sample(all_cnp, 1000)
    total_iterations = 0
    county_count = {county: 0 for county in county_code.values()}

    for cnp in selected_cnp:
        _, iterations = database.search_with_iterations(cnp)
        total_iterations += iterations
        county_code_value = cnp[7:9]  # Extrage codul județului din CNP
        county_name = county_code.get(county_code_value, "Necunoscut")
        county_count[county_name] += 1

    avg_iterations = total_iterations / len(selected_cnp)
    print(f"Număr total de iterații: {total_iterations}")
    print(f"Număr mediu de iterații per căutare: {avg_iterations:.2f}")

    print("\nDistribuția pe județe pentru cele 1000 de CNP-uri căutate:")
    for county, count in sorted(county_count.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            percentage = (count / len(selected_cnp)) * 100
            print(f"{county}: {count} CNP-uri ({percentage:.2f}%)")
else:
    print("Nu există CNP-uri de procesat. Verifică existența fișierului CSV sau încarcă date valide.")








