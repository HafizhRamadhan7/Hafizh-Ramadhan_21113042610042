import pytest
from Exercise_Chapter_11_11_3_1 import Employee


@pytest.fixture
def employee_instance():
    """Membuat instansi Employee yang digunakan oleh semua fungsi uji."""
    return Employee('Budi', 'Santoso', 50000)


def test_give_default_raise(employee_instance):
    """Menguji kenaikan gaji default ($5,000) menggunakan fixture."""
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 55000


def test_give_custom_raise(employee_instance):
    """Menguji kenaikan gaji kustom ($10,000) menggunakan fixture."""
    employee_instance.give_raise(10000)
    assert employee_instance.annual_salary == 60000

if __name__ == '__main__':
    pytest.main([__file__])