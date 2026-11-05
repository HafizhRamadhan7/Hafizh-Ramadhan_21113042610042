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


class Privileges:
    """Kelas untuk mengelola hak akses administrator."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "dapat menambah postingan",
                "dapat menghapus postingan",
                "dapat memblokir pengguna"
            ]
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak akses admin."""
        print("\nHak Akses Administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Kelas Admin turunan dari User."""

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()