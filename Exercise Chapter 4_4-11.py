pizzas = ['pepperoni', 'margherita', 'bbq chicken']
friend_pizzas = pizzas[:]  # Salin list

pizzas.append('hawaiian')
friend_pizzas.append('veggie')

print("Pizza favorit aku adalah:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nPizza favorit temanku adalah:")
for pizza in friend_pizzas:
    print(f"- {pizza}")