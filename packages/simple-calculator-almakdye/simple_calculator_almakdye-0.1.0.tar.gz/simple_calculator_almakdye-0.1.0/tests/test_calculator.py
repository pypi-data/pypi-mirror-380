from simple_calculator_almakdye.cli import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(5, 0) == "خطأ! لا يمكن القسمة على صفر."
