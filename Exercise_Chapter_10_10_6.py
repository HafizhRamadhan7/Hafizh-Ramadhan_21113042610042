print("Masukkan dua angka untuk dijumlahkan.")

try:
    num1 = input("Angka pertama: ")
    num1 = int(num1)
    num2 = input("Angka kedua: ")
    num2 = int(num2)
except ValueError:
    print("Error: Harap masukkan angka yang valid, bukan teks!")
else:
    hasil = num1 + num2
    print(f"Hasil penjumlahan: {hasil}")