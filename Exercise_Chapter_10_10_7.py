print("Kalkulator Penjumlahan (ketik 'q' untuk keluar)")

while True:
    num1 = input("\nAngka pertama: ")
    if num1.lower() == 'q':
        break

    num2 = input("Angka kedua: ")
    if num2.lower() == 'q':
        break

    try:
        total = int(num1) + int(num2)
    except ValueError:
        print("Error: Salah satu atau kedua input bukan angka. Silakan coba lagi.")
    else:
        print(f"Hasil: {num1} + {num2} = {total}")