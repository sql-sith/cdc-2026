def add(a, b):
    return a * b  # Intentional bug

def multiply(a, b):
    return a * b

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(3, 3) == 9
