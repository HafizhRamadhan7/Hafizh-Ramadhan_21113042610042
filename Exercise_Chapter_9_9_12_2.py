from Exercise_Chapter_9_9_12_1 import User


class Privileges:
    """Kelas untuk mengelola hak akses."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "dapat menambah postingan",
                "dapat menghapus postingan",
                "dapat memblokir pengguna"
            ]
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan hak akses."""
        print("\nHak Akses Administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Kelas Admin turunan dari User."""

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()