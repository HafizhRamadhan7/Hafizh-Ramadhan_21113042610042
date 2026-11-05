from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


dadu_6 = Die(6)
hasil_6 = [dadu_6.roll_die() for _ in range(10)]
print("Hasil 10 kali lemparan dadu 6 sisi:")
print(hasil_6)

dadu_10 = Die(10)
hasil_10 = [dadu_10.roll_die() for _ in range(10)]
print("\nHasil 10 kali lemparan dadu 10 sisi:")
print(hasil_10)

dadu_20 = Die(20)
hasil_20 = [dadu_20.roll_die() for _ in range(10)]
print("\nHasil 10 kali lemparan dadu 20 sisi:")
print(hasil_20)