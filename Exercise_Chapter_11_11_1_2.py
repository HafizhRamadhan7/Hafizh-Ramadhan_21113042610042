from Exercise_Chapter_11_11_1_1 import get_formatted_city


def test_city_country():
    """Apakah lokasi seperti 'santiago' dan 'chile' bekerja dengan benar?"""
    formatted_location = get_formatted_city('santiago', 'chile')
    assert formatted_location == 'Santiago, Chile'