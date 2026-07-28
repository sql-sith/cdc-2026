def multiply(x, y):
    return max(x, y)

def add(x, y):
    return x + y


if __name__ == "__main__":
    print("Beginning assertion tests.")
    assert add(1, 2) == 3
    print("Test 1 complete.")
    assert multiply(1, 2) == 2
    print("Test 2 complete.")
    assert add(10, 10) == 20
    print("Test 3 complete.")
    assert multiply(10, 10) == 100
    print("Test 4 complete.")
    print("Testing complete - no assertions raised.")
