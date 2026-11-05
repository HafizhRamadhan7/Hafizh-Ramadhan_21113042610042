class User:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"\nProfil Pengguna: {self.first_name.title()} {self.last_name.title()}")


class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = [
            "dapat menambahkan postingan",
            "dapat menghapus postingan",
            "dapat memblokir pengguna"
        ]

    def show_privileges(self):
        print(f"\nHak Akses Admin untuk {self.first_name.title()}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_baru = Admin("budi", "santoso", 30, "jakarta")
admin_baru.describe_user()
admin_baru.show_privileges()