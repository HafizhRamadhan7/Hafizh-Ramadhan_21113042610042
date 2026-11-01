def make_album(artist_name, album_title, songs_count=None):
    """Membuat dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    if songs_count:
        album['songs'] = songs_count
    return album

album1 = make_album('sheila on 7', 'kisah klasik untuk masa depan')
album2 = make_album('coldplay', 'a head full of dreams')
album3 = make_album('tulus', 'manusia', songs_count=10)

print(album1)
print(album2)
print(album3)