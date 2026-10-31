cities = {
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'fact': 'Memiliki sistem kereta tersibuk di dunia.',
    },
    'jakarta': {
        'country': 'indonesia',
        'population': '10.878.676 jiwa',
        'fact': 'Ibu kota negara Indonesia.',
    },
    'paris': {
        'country': 'prancis',
        'population': '2 juta jiwa',
        'fact': 'Dikenal sebagai Kota Cahaya.',
    },
}

for city, info in cities.items():
    print(f"\nKota: {city.title()}")
    print(f"  Negara: {info['country'].title()}")
    print(f"  Populasi: {info['population']}")
    print(f"  Fakta: {info['fact']}")