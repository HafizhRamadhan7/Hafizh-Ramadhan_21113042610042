favorite_languages = {
    'Barra': 'python',
    'Hafizh': 'c',
    'Akhdan': 'rust',
    'Raj': 'python',
}

people_to_poll = ['Barra', 'Hafizh', 'Akhdan', 'Ghiri']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()} sudah mengisi survei!")
    else:
        print(f"Halo {person.title()}, silakan ikuti survei bahasa favorit kami.")