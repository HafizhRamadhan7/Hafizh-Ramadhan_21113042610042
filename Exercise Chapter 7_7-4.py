prompt = "\nMasukkan topping pizza pilihan Anda:"
prompt += "\n(Ketik 'quit' untuk selesai) "

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")