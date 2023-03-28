kosik = ["-o-", "-ó-", "-ø-"]
miska = []

for jablko in kosik:
  jablko = jablko[1]
  miska.append(jablko)
  print(miska)

print(miska)

# Současný výsledek:
# V proměnné miska je: ['o', 'ó', 'ø']
# V proměnné košík je: ['-o-', '-ó-', '-ø-']

# Úkol: Zajistěte, aby se nám jablka "nemnožila", tudíž abychom na konci programu měli stále jen tři jablka: Oloupaná jablka v misce:
# V proměnné miska je: ['o', 'ó', 'ø']
# V proměnné košík je: []