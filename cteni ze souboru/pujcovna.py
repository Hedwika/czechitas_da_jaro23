# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

# Pozor! V souboru s daty je ještě jeden problém, který není na první pohled vidět!

# Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().

ujete_kilometry = 0

radky = []

with open("auta.txt", encoding="utf-8") as auta:
  for radek in auta:
    radky.append(radek)

radky.pop(-1)

for radek in radky:
  radek = radek.strip()
  radek = radek.replace(",", ".")
  radek = radek[9:]
  radek = float(radek)
  # ujete_kilometry += radek
  ujete_kilometry = ujete_kilometry + radek

print(f"Součet ujetých kilometrů za všecha auta je {ujete_kilometry*1000} km.")

# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---
# Řešení s komentářem:
# https://youtu.be/plOl4DztCa0
# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---