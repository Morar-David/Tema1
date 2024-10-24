# This is a sample Python script.
from string import punctuation

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#('David Morar')


text = "Ce ar face Elena Lasconi dacă ar fi președinta Ucrainei. „Cred că la anul s-ar încheia acest ! război”"

def articol(text):
    jumatate = len(text) // 2
    part1 = text[:jumatate]
    part2 = text[jumatate:]

    part1 = part1.upper().strip()


    part2 = part2[::-1]

    part2 = part2.capitalize()

    punctuatie = '.,!?'

    part2 = ''.join(char for char in part2 if char not in punctuatie)

    rezultat = part1 + ' ' + part2
    return rezultat

rezultat = articol(text)
print(rezultat)



