class User:
    """Kelas untuk membuat profil pengguna."""

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"\nProfil Pengguna: {self.first_name.title()} {self.last_name.title()}")
        print(f"- Umur: {self.age} tahun")
        print(f"- Kota: {self.city.title()}")

    def greet_user(self):
        """Menampilkan salam untuk pengguna."""
        print(f"Halo, {self.first_name.title()}! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menambah jumlah percobaan login sebesar 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mereset jumlah percobaan login menjadi 0."""
        self.login_attempts = 0

user1 = User("Hafizh", "Ramadhan", 18, "Purwokerto")
user2 = User("Iqbal", "Ramadhan", 22, "bandung")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()