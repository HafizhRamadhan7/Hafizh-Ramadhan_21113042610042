from pathlib import Path

names = []
print("Masukkan nama tamu (ketik 'quit' untuk selesai):")

while True:
    name = input("Nama: ")
    if name.lower() == 'quit':
        break
    names.append(name)

file_contents = ""
for name in names:
    file_contents += f"{name}\n"

path = Path('guest_book.txt')
path.write_text(file_contents, encoding='utf-8')
print("\nSemua nama tamu telah dicatat di guest_book.txt.")