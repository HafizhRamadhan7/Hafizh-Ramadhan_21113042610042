import json
from pathlib import Path

fav_number = input("Berapa angka favorit Anda? ")
path = Path('favorite_number.json')
contents = json.dumps(fav_number)
path.write_text(contents, encoding='utf-8')

print("Angka favorit Anda telah disimpan!")