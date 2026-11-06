from pathlib import Path

path = Path('Exercise_Chapter_10_10_1.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("Error: File 'Exercise_Chapter_10_10_1.txt' tidak ditemukan di folder ini!")
else:

    if not contents.strip():
        print("Peringatan: File 'Exercise_Chapter_10_10_1.txt' ditemukan, KETIK TEKS DI DALAMNYA lalu tekan Ctrl + S!")
    else:
        print("--- Output Exercise 10-3 ---")
        for line in contents.splitlines():
            print(line)