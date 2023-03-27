# Na adrese https://svatky.adresa.info/json najdete API, které vám odpoví, kdo má dneska svátek.

import requests

response = requests.get('https://svatky.adresa.info/json')
data = response.json()
print(data)

# Využijte toto API k tomu, abyste napsali program, který po spuštění vypíše na obrazovku kdo má dneska svátek.
# Pokud použijete adresu https://svatky.adresa.info/json?date=DDMM, kde místo DDMM doplníte datum, dostanete jméno, které má svátek v zadaný den. Formát DDMM znamená že 6. ledna bude zapsáno jako 0601, 12. září jako 1209 apod. Napište program, který dostane na příkazové řádce číslo dne a číslo měsíce a vypíše na výstup kdo má v daný den svátek. Použijte váš program abyste zjistili, kdo má svátek 29. února.

response = requests.get('https://svatky.adresa.info/json?date=2902')
data = response.json()
print(data)

# Bonus: předchozí bod uprav tak, že nebudeš dávat funkci requests.get() adresu včetně parametru date=1209, ale pouze základní "endpoint" https://svatky.adresa.info/json a parametry (vše za ?) dodáš volitelným parametrem.

vstup = input("Zadejte datum ve formátu DDMM. Například 29. února zadejte jako 2902: ")

response = requests.get(f'https://svatky.adresa.info/json?date={vstup}')
data = response.json()
print(data)

# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---
# Řešení s komentářem:
# https://youtu.be/gyaJZhgo7qU
# ---ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas------ILoveCzechitas---