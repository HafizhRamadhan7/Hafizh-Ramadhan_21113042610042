guests = ['Orel', 'Nico Robin', 'Marnie']

print("--- Undangan Awal ---")
for guest in guests:
    print(f"Kepada Yth. {guest}, Anda diundang ke acara makan malam.")

cant_make_it = 'Nico Robin'
print(f"\n[Info] Sayangnya, {cant_make_it} tidak dapat hadir ke makan malam.")

guests[1] = 'Iqbal Ramadhan'

print("\n--- Undangan Diperbarui ---")
for guest in guests:
    print(f"Kepada Yth. {guest}, Anda diundang ke acara makan malam.")

print("\nKabar baik! Meja makan yang lebih besar telah ditemukan.")

guests.insert(1, 'Kejora')
guests.insert(2, 'Inyong')
guests.append('Srikandi')

for guest in guests:
    print(f"Kepada Yth. {guest}, Anda diundang ke acara makan malam.")


print("\nMohon maaf, meja baru tidak sampai tepat waktu. Hanya 2 tamu yang dapat diundang.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, makan malam dibatalkan untuk Anda.")

for guest in guests:
    print(f"{guest}, Anda masih diundang ke makan malam!")

del guests[1]
del guests[0]

print("List tamu akhir (harus kosong):", guests)