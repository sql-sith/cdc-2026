from typing import Any


def set_test_cases() -> list[Any]:
    tests = []
    tests.append([])
    tests.append("[]")
    tests.append({1, 2, 4, 5.2})
    tests.append([2, 5, 11])
    tests.append((5, 10, 2, 17, 9, 1, 4))
    tests.append({1: 100, 2: 14, 3: 1})
    tests.append("abcde")
    tests.append(b'4567')
    return tests
