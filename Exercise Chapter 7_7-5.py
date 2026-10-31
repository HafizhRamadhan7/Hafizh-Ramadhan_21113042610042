prompt = "\nBerapa usia Anda?"
prompt += "\n(Ketik 'quit' untuk keluar) "

while True:
    age_input = input(prompt)
    if age_input.lower() == 'quit':
        break
    
    age = int(age_input)
    if age < 3:
        print("Tiket Anda gratis!")
    elif age <= 12:
        print("Harga tiket Anda adalah $10.")
    else:
        print("Harga tiket Anda adalah $15.")