states = dict([('Sao Paulo', 'SP'), ('Rio de Janeiro', 'RJ'), ('Minas Gerais', 'MG')])

print(states)
print(states.items())

print(f"Sao Paulo is abbreviated by {states['Sao Paulo']}")

print('-' * 10)
for i, v in states.items():
  print(f"{i} is abbreviated by {v}")

print('-' * 10)
for i, v in list(states.items()):
  print(f"{i} is abbreviated by {v}")

cities = { 
  "SP": ["Sao Caetano do Sul", "Paranapiacaba", "Aracatuba"],
  "RJ": ["Angra dos Reis", "Sao Gonçalo", "Nova Iguaçu"],
  "MG": ["Belo Horizonte", "Guaxupé", "Muzambinho"]
}

print('-' * 10)
for s, c in zip(states, cities):
  print(f"{s} zipped with {c}")

  print(f"Cities of {s}:")
  for city in cities[c]:
    print(city)