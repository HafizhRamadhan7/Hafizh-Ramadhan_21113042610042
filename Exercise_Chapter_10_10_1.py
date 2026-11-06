from pathlib import Path

path = Path('Exercise_Chapter_10_10_1.txt')

# Tambahkan encoding='utf-8' jika ada Unicode/Encoding Error
contents = path.read_text(encoding='utf-8')

# 1. Membaca seluruh isi file sekaligus
print("--- Membaca Seluruh Isi File ---")
print(contents)

# 2. Membaca baris demi baris dari list
print("\n--- Membaca Baris demi Baris dari List ---")
lines = contents.splitlines()
for line in lines:
    print(line)