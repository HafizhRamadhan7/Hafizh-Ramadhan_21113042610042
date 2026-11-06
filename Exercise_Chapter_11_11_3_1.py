class Employee:
    """Kelas untuk mengelola data karyawan dan kenaikan gaji."""

    def __init__(self, first_name, last_name, annual_salary):
        """Menyimpan nama depan, nama belakang, dan gaji tahunan."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Menambahkan kenaikan gaji (default: $5,000)."""
        self.annual_salary += amount