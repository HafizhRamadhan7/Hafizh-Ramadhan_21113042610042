class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Kapasitas baterai: {self.battery_size} kWh.")

    def get_range(self):
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225

        print(f"Mobil ini dapat menempuh jarak sekitar {range_miles} mil dalam sekali pengisian.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # Instance Battery dijadikan atribut


mobil_listrik = ElectricCar('nissan', 'leaf', 2024)
print(mobil_listrik.get_descriptive_name())
mobil_listrik.battery.get_range()
mobil_listrik.battery.upgrade_battery()
mobil_listrik.battery.get_range()