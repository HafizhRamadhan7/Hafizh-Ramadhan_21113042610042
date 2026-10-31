number = input("Masukkan sebuah angka: ")
number = int(number)

if number % 10 == 0:
    print(f"Angka {number} adalah kelipatan 10.")
else:
    print(f"Angka {number} bukan kelipatan 10.")