class Restaurant:
    """Kelas untuk merepresentasikan restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Menampilkan deskripsi restoran."""
        print(f"Restoran '{self.restaurant_name.title()}' menyajikan masakan {self.cuisine_type.title()}.")

    def open_restaurant(self):
        """Menampilkan status restoran buka."""
        print(f"Restoran '{self.restaurant_name.title()}' sekarang buka!")


restoran_1 = Restaurant("Sederhana", "Padang")
print(restoran_1.restaurant_name)
print(restoran_1.cuisine_type)
restoran_1.describe_restaurant()
restoran_1.open_restaurant()

# 9-2 Tiga instance restoran
restoran_2 = Restaurant("Sushi Tei", "Jepang")
restoran_3 = Restaurant("Gacoan", "Mie Pedas")

restoran_1.describe_restaurant()
restoran_2.describe_restaurant()
restoran_3.describe_restaurant()