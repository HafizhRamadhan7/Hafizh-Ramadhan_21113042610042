from Exercise_Chapter_11_11_3_1 import Employee


def test_give_default_raise():
    """Menguji kenaikan gaji default ($5,000)."""
    emp = Employee('Budi', 'Santoso', 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000


def test_give_custom_raise():
    """Menguji kenaikan gaji dengan jumlah kustom."""
    emp = Employee('Budi', 'Santoso', 50000)
    emp.give_raise(10000)
    assert emp.annual_salary == 60000