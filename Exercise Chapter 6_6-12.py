cities = {
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'fact': 'Memiliki sistem kereta tersibuk di dunia.',
        'currency': 'Yen',
    },
        'jakarta': {
        'country': 'indonesia',
        'population': '10.878.676 jiwa',
        'fact': 'Ibu kota negara Indonesia.',
        'currency': 'Rupiah',
    },
    'paris': {
        'country': 'prancis',
        'population': '2 juta jiwa',
        'fact': 'Dikenal sebagai Kota Cahaya.',
        'currency': 'Euro',
    },
}

for city, info in cities.items():
    print(f"Kota: {city.title()}")
    print(f"Mata Uang: {info['currency']}")