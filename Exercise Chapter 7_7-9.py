sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'turkey', 'pastrami', 'club']
finished_sandwiches = []

print("Maaf, kedai kami telah kehabisan roti pastrami hari ini.\n")

# Menghapus semua 'pastrami' dari list sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya telah membuatkan roti {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nSeluruh sandwich yang berhasil dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich.title()}")