prompt = "\nMasukkan topping (versi 1): "
topping = ""
while topping.lower() != 'quit':
    topping = input(prompt)
    if topping.lower() != 'quit':
        print(f"Menambahkan {topping}.")

# 2. Menggunakan variabel 'active' (flag)
prompt = "\nMasukkan usia Anda (versi 2): "
active = True
while active:
    age_input = input(prompt)
    if age_input.lower() == 'quit':
        active = False
    else:
        age = int(age_input)
        print(f"Usia dicatat: {age}")

# 3. Menggunakan statement 'break'
prompt = "\nMasukkan topping (versi 3): "
while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"Menambahkan {topping}.")