class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Menampilkan deskripsi restoran."""
        print(f"Restoran '{self.restaurant_name.title()}' menyajikan masakan {self.cuisine_type.title()}.")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="Es Krim"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Cokelat", "Vanilla", "Stroberi", "Matcha"]

    def display_flavors(self):
        print(f"\nVarian rasa es krim di {self.restaurant_name.title()}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


kedai_eskrim = IceCreamStand("Mixue Delight")
kedai_eskrim.describe_restaurant()
kedai_eskrim.display_flavors()