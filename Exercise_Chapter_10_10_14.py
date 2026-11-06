import json
from pathlib import Path


def get_stored_username(path):
    """Mendapatkan username jika tersimpan."""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    return None


def get_new_username(path):
    """Meminta username baru dan menyimpannya."""
    username = input("Masukkan nama Anda: ")
    contents = json.dumps(username)
    path.write_text(contents, encoding='utf-8')
    return username


def greet_user():
    """Menyapa pengguna dan memverifikasi identitas."""
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        correct = input(f"Apakah Anda {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingat Anda saat kembali, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingat Anda saat kembali, {username}!")


greet_user()