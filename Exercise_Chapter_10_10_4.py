from pathlib import Path

name = input("Masukkan nama Anda: ")
path = Path('guest.txt')
path.write_text(name, encoding='utf-8')
print(f"Nama '{name}' telah disimpan ke guest.txt.")