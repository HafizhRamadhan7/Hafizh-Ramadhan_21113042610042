class User:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"\nProfil Pengguna: {self.first_name.title()} {self.last_name.title()}")


class Privileges:

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "dapat menambahkan postingan",
                "dapat menghapus postingan",
                "dapat memblokir pengguna"
            ]
        self.privileges = privileges

    def show_privileges(self):
        print("\nHak Akses Administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()


admin_utama = Admin("Hafizh", "Ramadhan", 18, "Purwokerto")
admin_utama.describe_user()

admin_utama.privileges.show_privileges()