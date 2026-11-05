from random import choice

# Buat list berisi 10 angka dan 5 huruf (total 15 elemen)
lotere_pool = [1, 5, 12, 18, 23, 34, 42, 56, 77, 89, 'A', 'B', 'C', 'D', 'E']
tiket_menang = []

# Pilih 4 elemen acak secara unik
while len(tiket_menang) < 4:
    karakter_terpilih = choice(lotere_pool)
    if karakter_terpilih not in tiket_menang:
        tiket_menang.append(karakter_terpilih)

print("Kombinasi tiket pemenang hari ini adalah:")
print(tiket_menang)
print("\nSelamat! Tiket apa pun yang cocok dengan 4 angka/huruf di atas memenangkan hadiah!")