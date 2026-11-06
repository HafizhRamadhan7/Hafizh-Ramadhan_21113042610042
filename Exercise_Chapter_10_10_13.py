import json
from pathlib import Path

path = Path('user_info.json')

if path.exists():
    contents = path.read_text(encoding='utf-8')
    user_data = json.loads(contents)
    print(f"\nSelamat datang kembali, {user_data['username']}!")
    print(f"- Umur: {user_data['age']}")
    print(f"- Kota: {user_data['city']}")
else:
    username = input("Masukkan nama Anda: ")
    age = input("Masukkan umur Anda: ")
    city = input("Masukkan kota tempat tinggal Anda: ")

    user_data = {
        'username': username,
        'age': age,
        'city': city
    }

    contents = json.dumps(user_data)
    path.write_text(contents, encoding='utf-8')
    print("\nInformasi profil Anda telah disimpan!")