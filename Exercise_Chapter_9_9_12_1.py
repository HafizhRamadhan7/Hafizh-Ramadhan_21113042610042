class User:
    """Kelas dasar untuk profil pengguna."""

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        """Menampilkan ringkasan profil pengguna."""
        print(f"\nProfil Pengguna: {self.first_name.title()} {self.last_name.title()}")