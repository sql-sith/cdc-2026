# from typing import Any


def get_squares(numbers):
    for i, number in enumerate(numbers):
        numbers[i] = number ** 2
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
        # print original data here
