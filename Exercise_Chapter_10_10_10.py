from pathlib import Path

# Membaca file teks kamu
path = Path('Exercise_Chapter_10_10_1.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(" File 'Exercise_Chapter_10_10_1.txt' tidak ditemukan!")
else:
    # Mengubah teks jadi huruf kecil & menghitung kata 'in'
    count_all = contents.lower().count('in')
    count_exact = contents.lower().count('in ')

    print("--- Output Exercise 10-10 ---")
    print(f"Kemunculan 'in' (termasuk di dalam kata seperti 'line'): {count_all} kali")
    print(f"Kemunculan 'in ' (hanya kata mandiri 'In'): {count_exact} kali")