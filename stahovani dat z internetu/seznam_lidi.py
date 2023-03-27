# Jak už jsme si ověřili v lekci, datové API na adrese https://api.kodim.cz/python-data/people obsahuje seznam lidí. Napište program, který tento seznam z API stáhne a převede z formátu JSON na Python slovníky.

import requests

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()
print(data)

# Proveďte následující úkoly
# Zjistěte kolik lidí celkem seznam obsahuje:
pocet_lidi = len(data)
print(pocet_lidi)

# Zjistěte jaké všechny informace máme o jednotlivých osobách:
keys = data[0].keys()
print(keys)

# Zjistěte, kolik je v souboru mužů a žen.
pocet_zen = 0
pocet_muzu = 0

for osoba in data:
  pohlavi = osoba["gender"]
  print(pohlavi)
  if pohlavi == "Male":
    pocet_muzu += 1
  else:
    pocet_zen += 1

print(f"Počet mužů je {pocet_muzu}.")
print(f"Počet žen je {pocet_zen}.")

# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---
# Řešení s komentářem:
# https://youtu.be/eh5q9lArYfA
# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---