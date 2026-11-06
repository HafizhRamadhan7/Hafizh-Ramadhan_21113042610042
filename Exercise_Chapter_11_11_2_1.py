def get_formatted_city(city, country, population=None):
    """Mengembalikan format lokasi lengkap dengan populasi opsional."""
    if population:
        full_location = f"{city}, {country} - population {population}"
    else:
        full_location = f"{city}, {country}"
    return full_location.title()