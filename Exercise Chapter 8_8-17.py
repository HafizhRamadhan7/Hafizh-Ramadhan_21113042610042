# 1. Program Pertama: Modifikasi dari 8-4 (Large Shirts)
def make_shirt(size='L', message='I love Python'):
    """Mencetak ukuran dan pesan baju kaos."""
    print(f"Membuat baju ukuran '{size}' dengan tulisan: '{message}'.")


make_shirt()
make_shirt(size='M')
make_shirt('S', 'Koding Python')


# 2. Program Kedua: Modifikasi dari 8-7 (Album)
def make_album(artist_name, album_title, songs_count=None):
    """Membuat dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    if songs_count:
        album['songs'] = songs_count
    return album


album_1 = make_album('sheila on 7', 'kisah klasik untuk masa depan')
album_2 = make_album('tulus', 'manusia', songs_count=10)

print(album_1)
print(album_2)


# 3. Program Ketiga: Modifikasi dari 8-14 (Cars)
def make_car(manufacturer, model, **car_info):
    """Menyimpan informasi tentang mobil dalam bentuk dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)