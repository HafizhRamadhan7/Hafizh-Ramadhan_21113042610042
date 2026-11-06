from pathlib import Path

path = Path('Exercise_Chapter_10_10_1.txt')
contents = path.read_text(encoding='utf-8')

print("--- Hasil Setelah Mengganti Kata Python Menjadi C ---")
for line in contents.splitlines():
    modified_line = line.replace('Python', 'C')
    print(modified_line)