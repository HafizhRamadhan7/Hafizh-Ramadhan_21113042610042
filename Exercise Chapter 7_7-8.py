sandwich_orders = ['tuna', 'turkey', 'club', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya telah membuatkan roti {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nSeluruh sandwich yang telah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich.title()}")