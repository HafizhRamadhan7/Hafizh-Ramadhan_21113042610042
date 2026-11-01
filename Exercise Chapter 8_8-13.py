def build_profile(first, last, **user_info):
    profile = {
        'first_name': first,
        'last_name': last
    }
    for key, value in user_info.items():
        profile[key] = value
        
    return profile

my_profile = build_profile(
    'Hafizh', 'Ramadhan',
    location='Purwokerto',
    field='Gambar Teknik',
    hobby='Makan'
)
print("\n--- Profil Diri ---")
print(my_profile)