favorite_places = {
    'Barra': ['Solo', 'Yogyakarta'],
    'Fawwaz': ['tokyo'],
    'Nona': ['bandung', 'malang', 'lombok'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place.title()}")