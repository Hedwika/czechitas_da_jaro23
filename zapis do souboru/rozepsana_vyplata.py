# Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

# Nejprve tyto informace vypište na terminál
# Poté program upravte tak, aby vypsal tyto výsledky do souboru

vykaz = []

with open("vyplata.txt", encoding="utf-8") as rocni_vykaz:
  for radek in rocni_vykaz:
    vykaz.append(radek[0:3])

# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu.
hodinova_mzda = input("Zadejte hodinovou mzdu: ")
hodinova_mzda_int = int(hodinova_mzda)

# Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok
# Pozn: je třeba převést hodnoty v seznamu na typ integer!
vykaz_int = []

for mesic in vykaz:
  mesic_int = int(mesic)
  vykaz_int.append(mesic_int)

with open('rozepsana_vyplata.txt', mode='w', encoding='utf-8') as output_file:
  for mesic in vykaz_int:
    mesicni_vyplata = hodinova_mzda_int*mesic
    print(mesicni_vyplata)
    print(mesicni_vyplata, file=output_file)

# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---
# Řešení s komentářem:
# https://youtu.be/FOm45Qagyw8
# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---