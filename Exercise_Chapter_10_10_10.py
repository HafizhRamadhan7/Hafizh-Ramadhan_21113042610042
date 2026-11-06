from pathlib import Path

path = Path('Exercise_Chapter_10_10_1.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("File 'Exercise_Chapter_10_10_1.txt' tidak ditemukan!")
else:
    print("--- Isi File Terbaca ---")
    print(repr(contents))  # Gunakan repr untuk melihat karakter tersembunyi
    print("------------------------")

    count_in = contents.lower().count('in ')
    count_python = contents.lower().count('python')

    print(f"\nHasil Perhitungan:")
    print(f"- Kata 'in ': {count_in} kali")
    print(f"- Kata 'python': {count_python} kali")