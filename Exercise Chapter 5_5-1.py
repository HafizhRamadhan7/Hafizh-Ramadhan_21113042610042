#Menyatakan
car = 'subaru'
age = 21
topping = 'mushrooms'

# 5 Pengujian yang Menghasilkan nilai TRUE
print("=== 5 Tests Evaluating to TRUE ===")

print("1. Is car == 'subaru'? I predict True.")
print(f"   Result: {car == 'subaru'}\n")

print("2. Is car != 'audi'? I predict True.")
print(f"   Result: {car != 'audi'}\n")

print("3. Is age == 21? I predict True.")
print(f"   Result: {age == 21}\n")

print("4. Is age >= 18? I predict True.")
print(f"   Result: {age >= 18}\n")

print("5. Is topping == 'mushrooms'? I predict True.")
print(f"   Result: {topping == 'mushrooms'}\n")

# 5 Pengujian yang Menghasilkan nilai FALSE
print("=== 5 Tests Evaluating to FALSE ===")

print("6. Is car == 'audi'? I predict False.")
print(f"   Result: {car == 'audi'}\n")

print("7. Is car == 'Subaru'? I predict False.")  # Sensitif huruf kapital
print(f"   Result: {car == 'Subaru'}\n")

print("8. Is age < 18? I predict False.")
print(f"   Result: {age < 18}\n")

print("9. Is age == 30? I predict False.")
print(f"   Result: {age == 30}\n")

print("10. Is topping == 'pepperoni'? I predict False.")
print(f"    Result: {topping == 'pepperoni'}\n")