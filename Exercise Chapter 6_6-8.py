pet_1 = {'kind': 'kucing', 'owner': 'Rara'}
pet_2 = {'kind': 'anjing', 'owner': 'Barra'}
pet_3 = {'kind': 'kelinci', 'owner': 'Raffa'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Pemilik: {pet['owner'].title()}, Hewan: {pet['kind']}")