# Stáhněte si soubor words.txt a zpracujte z něj výstupní soubor ve formátu JSON obsahující slovník. Klíče budou písmena a hodnoty seznamy slov, které začínají písmenem v klíči. Pokud na nějaké písmeno žádná slova nezačínají, tak ve výstupu toto písmeno nebude. Seřaďte tyto seznamy podle abecedy. Zajistěte, aby i klíče ve výstupním JSON souboru byly seřazeny a data byla odsazena čtyřmi mezerami pro lepší čitelnost člověkem.

import json

# Otevření souboru words.txt
with open('words.txt', encoding='utf-8') as file:
  words = file.read().split()

# Výpis souboru words.txt do seznamu
print(words)

# Vytvoření prázdného slovníku (finální výstup)
output = {}

# Procházení každého elementu seznamu words
for word in words:
  # Uložení prvního písmenka z aktuálního slova do proměnné first_letter
  first_letter = word[0].lower()
  # Kontrola, zda už toto písmenko ve slovníku output máme.
  # Pokud ne:
  if first_letter not in output:
    # Vytvoř prázdný slovník jako hodnotu pod klíčem first_letter ve slovníku output
    output[first_letter] = []
  # Pokud už tento klíč ve slovníku je, přiřaď do jeho hodnoty (seznam) aktuální slovo (word)
  output[first_letter].append(word)
  # Po prvním opakování vypadá náš slovník output takto:
  # {"l": ["look"]}
  # Poté, co for cyklus narazí na slovo "leadership" a dokončí cyklus, bude slovník output vypadat následovně:
  # {
  # "l": ["look", "leadership"], 
  # "t": ["tail"], 
  # "s": ["sock"], 
  # "d": ["diet"], 
  # "b": ["breakfast"], 
  # "r": ["resist"], 
  # }

# Seřadíme hodnoty pod všemi klíči podle abecedy
for key in output:
  output[key].sort()

# Seřadíme všechny klíče ve slovníku podle abecedy
output = {key: output[key] for key in sorted(output)}

# Tisk pro kontrolu
print(output)

# Uložení do souboru
with open('output.json', mode='w', encoding='utf-8') as output_file:
  json.dump(output, output_file, indent=4)

# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---
# Řešení s komentářem:
# https://youtu.be/WOO6oSE9nW0
# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---