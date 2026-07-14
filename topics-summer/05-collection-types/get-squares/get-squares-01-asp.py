from typing import Any


def set_test_cases() -> list[Any]:
    tests = []
    tests.append([])
    tests.append({1, 2, 4, 5.2})
    tests.append([2, 5, 11])
    tests.append((5, 10, 2, 17, 9, 1, 4))
    tests.append({1: 100, 2: 14, 3: 1})
    tests.append("abcde")
    return tests


def get_squares(numbers):
    '''
        Eliminates terminal exceptions on TypeError
    '''
    try:
        for i, number in enumerate(numbers):
            numbers[i] = number ** 2
    except (TypeError) as e:
        print(f"ERROR: {e}")
        return None

    return numbers


if __name__ == "__main__":
    tests = []
    tests.append([6])                 # should return [36]
    tests.append([])                  # should return []
    tests.append([5, 2, 3])           # should return [25, 4, 9]
    tests.append([-1, 0, 1])          # should return [-1, 0, 1]
    tests.append(["abc", {1, 2, 3}])  # should return ... what?
    tests.append([42])                # should return 1764 ... but will it run?

    for test_case in tests:
        print(f'\nBeginning test case: {test_case}.')
        test_case_squared = get_squares(test_case)
        print(f"Squared data: {test_case_squared}")
        print(f'Original data: {test_case}')
