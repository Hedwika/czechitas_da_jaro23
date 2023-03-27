# Napište program, který se po spuštění zeptá na název souboru, který má vytvořit (nebo přepsat, pokud už ten soubor existuje), a pak se zeptá na řádek textu, který má do souboru zapsat.

nazev_souboru = input("Soubor se bude jmenovat (nezapomeňte za název souboru uvést .txt): ")
radek_textu = input("Do souboru chci zapsat: ")

with open(nazev_souboru, mode='w', encoding='utf-8') as output_file:
  print(radek_textu, file=output_file)

# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---
# Řešení s komentářem:
# https://youtu.be/V7bfzzbl1A8
# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---