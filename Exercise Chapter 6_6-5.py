rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'citarum': 'indonesia',
}

# 1. Cetak kalimat tiap sungai
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

print("\n--- Nama Sungai ---")
for river in rivers.keys():
    print(river.title())

print("\n--- Nama Negara ---")
for country in rivers.values():
    print(country.title())