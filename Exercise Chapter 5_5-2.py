# 1. Pengujian kesamaan dan ketidaksamaan string
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("Is fruit != 'banana'? I predict True.")
print(fruit != 'banana')

print("Is fruit == 'orange'? I predict False.")
print(fruit == 'orange')


# 2. Pengujian menggunakan method lower()
car = 'Audi'
print("\nIs car.lower() == 'audi'? I predict True.")
print(car.lower() == 'audi')

print("Is car.lower() == 'Audi'? I predict False.")
print(car.lower() == 'Audi')


# 3. Pengujian angka (==, !=, >, <, >=, <=)
age = 20
print("\nIs age == 20? I predict True.")
print(age == 20)

print("Is age != 20? I predict False.")
print(age != 20)

print("Is age > 18? I predict True.")
print(age > 18)

print("Is age < 18? I predict False.")
print(age < 18)

print("Is age >= 21? I predict False.")
print(age >= 21)

print("Is age <= 20? I predict True.")
print(age <= 20)


# 4. Pengujian menggunakan kata kunci 'and' dan 'or'
score_1 = 85
score_2 = 90
print("\nIs score_1 > 80 and score_2 > 80? I predict True.")
print(score_1 > 80 and score_2 > 80)

print("Is score_1 > 90 or score_2 > 90? I predict False.")
print(score_1 > 90 or score_2 > 90)


# 5. Pengujian apakah item ADA di dalam list
toppings = ['mushrooms', 'onions']
print("\nIs 'mushrooms' in toppings? I predict True.")
print('mushrooms' in toppings)

print("Is 'pepperoni' in toppings? I predict False.")
print('pepperoni' in toppings)


# 6. Pengujian apakah item TIDAK ADA di dalam list
banned_users = ['andrew', 'carolina']
print("\nIs 'marie' not in banned_users? I predict True.")
print('marie' not in banned_users)

print("Is 'andrew' not in banned_users? I predict False.")
print('andrew' not in banned_users)