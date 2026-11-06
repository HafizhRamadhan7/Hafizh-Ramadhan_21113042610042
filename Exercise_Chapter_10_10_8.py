from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"\n Error: File '{filename}' tidak ditemukan di direktori ini.")
    else:
        print(f"\nIsi dari {filename}:")
        print(contents.strip())