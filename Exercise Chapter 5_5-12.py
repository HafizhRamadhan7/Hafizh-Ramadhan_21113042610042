# Contoh penulisan kondisi if yang SUDAH RAPI sesuai PEP 8:
# Menggunakan 1 spasi di sekitar operator '==' dan '<'

age = 18

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Harga tiket kamu adalah ${price}.")