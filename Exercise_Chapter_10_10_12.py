import json
from pathlib import Path

path = Path('favorite_number.json')

try:
    contents = path.read_text(encoding='utf-8')
    fav_number = json.loads(contents)
except FileNotFoundError:
    fav_number = input("Berapa angka favorit Anda? ")
    contents = json.dumps(fav_number)
    path.write_text(contents, encoding='utf-8')
    print("Terima kasih, angka favorit Anda berhasil disimpan!")
else:
    print(f"Saya tahu angka favorit Anda! Angka itu adalah {fav_number}.")