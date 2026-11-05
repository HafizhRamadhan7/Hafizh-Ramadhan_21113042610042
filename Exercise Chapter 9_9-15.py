from random import choice

lotere_pool = [1, 5, 12, 18, 23, 34, 42, 56, 77, 89, 'A', 'B', 'C', 'D', 'E']

my_ticket = [5, 23, 'A', 'D']

percobaan = 0
berhasil = False

print("Memulai simulasi pengocokan lotere...")

while not berhasil:
    percobaan += 1
    tiket_tarikan = []
    
    while len(tiket_tarikan) < 4:
        karakter = choice(lotere_pool)
        if karakter not in tiket_tarikan:
            tiket_tarikan.append(karakter)

    if set(my_ticket) == set(tiket_tarikan):
        berhasil = True

print(f"\nSelamat! Tiket Anda {my_ticket} akhirnya menang!")
print(f"Dibutuhkan total {percobaan:,} kali pengocokan loop sampai tiket Anda keluar.")