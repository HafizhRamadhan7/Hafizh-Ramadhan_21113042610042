responses = {}
polling_active = True

while polling_active:
    name = input("\nSiapa nama Anda? ")
    place = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")
    
    responses[name.title()] = place.title()
    
    repeat = input("Apakah ada orang lain yang ingin mengisi survei? (ya/tidak) ")
    if repeat.lower() == 'tidak':
        polling_active = False

print("\n--- Hasil Survei Liburan Impian ---")
for name, place in responses.items():
    print(f"{name} ingin mengunjungi {place}.")

location_counts = {}
for place in responses.values():
    location_counts[place] = location_counts.get(place, 0) + 1

print("\n--- Rekap Total Pemilih per Destinasi ---")
for place, count in location_counts.items():
    print(f"{place}: {count} orang")