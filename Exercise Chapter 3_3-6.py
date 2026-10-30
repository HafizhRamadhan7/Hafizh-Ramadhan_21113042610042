guests = ['Nico Robin', 'Marnie', 'Orel']

print("--- Undangan Awal ---")
for guest in guests:
    print(f"Kepada Yth. {guest}, Anda diundang ke acara makan malam.")

cant_make_it = 'Nico Robin'
print(f"\n[Info] Sayangnya, {cant_make_it} tidak dapat hadir ke makan malam.")

guests[0] = 'Kejora'

print("\n--- Undangan Diperbarui ---")
for guest in guests:
    print(f"Kepada Yth. {guest}, Anda diundang ke acara makan malam.")

print("\nKabar baik! Meja makan yang lebih besar telah ditemukan.")

guests.insert(0, 'Iqbal Ramadhan')
guests.insert(2, 'Inyong')
guests.append('Srikandi')

for guest in guests:
    print(f"Kepada Yth. {guest}, Anda diundang ke acara makan malam.")