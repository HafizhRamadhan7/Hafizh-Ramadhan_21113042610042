def make_sandwich(*items):
    """Menerima arbitrary number of arguments untuk isian sandwich."""
    print("\nMembuat sandwich dengan isian berikut:")
    for item in items:
        print(f"- {item}")

make_sandwich('keju', 'daging sapi')
make_sandwich('tuna', 'tomat', 'mayones')
make_sandwich('telur', 'alpukat', 'saus sambal', 'selada')