class Restaurant:
    """Kelas untuk merepresentasikan restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Atribut baru dengan nilai default 0

    def describe_restaurant(self):
        """Menampilkan deskripsi restoran."""
        print(f"Restoran '{self.restaurant_name.title()}' menyajikan masakan {self.cuisine_type.title()}.")

    def open_restaurant(self):
        """Menampilkan status restoran buka."""
        print(f"Restoran '{self.restaurant_name.title()}' sekarang buka!")

    def set_number_served(self, number):
        """Mengatur jumlah pelanggan yang telah dilayani ke nilai tertentu."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("Jumlah pelanggan tidak bisa dikurangi!")

    def increment_number_served(self, additional_customers):
        """Menambahkan jumlah pelanggan yang dilayani dalam satu hari/sesi."""
        if additional_customers > 0:
            self.number_served += additional_customers



restaurant = Restaurant("Sederhana", "Padang")

print(f"Jumlah pelanggan awal yang dilayani: {restaurant.number_served}")

restaurant.number_served = 15
print(f"Jumlah pelanggan setelah diubah langsung: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Jumlah pelanggan setelah set_number_served: {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Jumlah total pelanggan setelah penambahan harian: {restaurant.number_served}")