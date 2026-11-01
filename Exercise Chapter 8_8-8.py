def make_album(artist_name, album_title, songs_count=None):
    """Membuat dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    if songs_count:
        album['songs'] = songs_count
    return album

while True:
        print("\n--- Input Informasi Album (Ketik 'Keluar' untuk keluar) ---")
        artist = input("Nama Artis: ")
        if artist.lower() == 'keluar':
            break
            
        title = input("Judul Album: ")
        if title.lower() == 'keluar':
            break
            
        user_album = make_album(artist, title)
        print("\nDictionary album yang berhasil dibuat:")
        print(user_album)