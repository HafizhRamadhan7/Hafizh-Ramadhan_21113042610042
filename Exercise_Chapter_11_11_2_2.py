from Exercise_Chapter_11_11_2_1 import get_formatted_city


def test_city_country():
    """Menguji format tanpa parameter populasi."""
    formatted_location = get_formatted_city('santiago', 'chile')
    assert formatted_location == 'Santiago, Chile'


def test_city_country_population():
    """Menguji format dengan parameter populasi."""
    formatted_location = get_formatted_city('santiago', 'chile', 5000000)
    assert formatted_location == 'Santiago, Chile - Population 5000000'