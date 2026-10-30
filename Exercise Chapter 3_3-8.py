locations = ['Jepang', 'Mekkah', 'Finlandia', 'Swiss', 'Perancis']

print("List asli:", locations)
print("Urutan abjad (sorted()):", sorted(locations))
print("List tetap asli:", locations)
print("Urutan abjad terbalik (sorted()):", sorted(locations, reverse=True))
print("List tetap asli:", locations)

locations.reverse()
print("Urutan dibalik dengan reverse():", locations)

locations.reverse()
print("Kembali ke urutan semula:", locations)

locations.sort()
print("Diurutkan Permanen (sort()):", locations)

locations.sort(reverse=True)
print("Diurutkan Permanen Terbalik (sort(reverse=True)):", locations)