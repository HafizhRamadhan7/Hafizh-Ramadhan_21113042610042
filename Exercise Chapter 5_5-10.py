current_users = ['john', 'mary', 'admin', 'sarah', 'eric']
new_users = ['Luffy', 'Zoro', 'Mikey', 'Takemitcy', 'Ole Romeny']

# Buat list versi huruf kecil untuk pemeriksaan case-insensitive
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah digunakan, silakan masukkan username lain.")
    else:
        print(f"Username '{new_user}' masih tersedia.")