def print_models(unprinted_designs, completed_models):
    """Simulasi mencetak desain 3D hingga daftar desain kosong."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Menampilkan semua model yang berhasil dicetak."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)