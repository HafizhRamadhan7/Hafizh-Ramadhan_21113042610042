person_1 = {'first_name': 'Hafizh', 'last_name': 'Ramadhan', 'age': 18, 'city': 'Purwokerto'}
person_2 = {'first_name': 'Raya', 'last_name': 'Barradaiva', 'age': 18, 'city': 'Sukoharjo'}
person_3 = {'first_name': 'Bayu', 'last_name': 'Rahman', 'age': 17, 'city': 'Purwokerto'}

people = [person_1, person_2, person_3]

for person in people:
    name = f"{person['first_name']} {person['last_name']}"
    print(f"Nama: {name}, Umur: {person['age']}, Kota: {person['city']}")