import json
from pathlib import Path

path = Path('favorite_number.json')
try:
    contents = path.read_text(encoding='utf-8')
    fav_number = json.loads(contents)
except FileNotFoundError:
    print("Belum ada angka favorit yang tersimpan.")
else:
    print(f"Saya tahu angka favorit Anda! Angka itu adalah {fav_number}.")