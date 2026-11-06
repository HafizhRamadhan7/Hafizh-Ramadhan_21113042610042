from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Gak nyetak pesan apa-apa (diam-diam skip)
        pass
    else:
        print(f"\nIsi dari {filename}:")
        print(contents.strip())