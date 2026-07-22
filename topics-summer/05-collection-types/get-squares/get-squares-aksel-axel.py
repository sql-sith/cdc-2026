# cspell: ignore aiuhigwjk iughwr

def get_squares(numbers):
    """Get the square of all the elements of an iterable.
    """
    new_numbers = []
    dict_k = []
    if isinstance(numbers, dict):
        dict_k = list(numbers)
        numbers = numbers.values()
    for number in numbers:
        try:
            new_numbers.append(number ** 2)
        except TypeError:
            new_numbers.append(None)
    if isinstance(numbers, set):
        return set(new_numbers)
    if isinstance(numbers, list):
        return new_numbers
    if isinstance(numbers, tuple):
        return tuple(new_numbers)
    if len(dict_k) > 0:
        new_dict = {}
        for k, v in zip(
            dict_k,
            new_numbers):
            new_dict[k] = v
        return new_dict
    if isinstance(numbers, str):
        return "I hate being squared."
    if isinstance(numbers, bytes):
        return b"I hate being squared."
    return new_numbers # Fallback


if __name__ == "__main__":
    from test_cases import set_test_cases as stc
    tests = stc() # Sets the test cases
    #tests.append([6])                 # should return [36]
    #tests.append([])                  # should return []
    #tests.append([5, 2, 3])           # should return [25, 4, 9]
    #tests.append([-1, 0, 1])          # should return [-1, 0, 1]
    #tests.append(["abc", {1, 2, 3}])  # should return ... what?
    #tests.append([42])                # should return 1764 ... but will it run?
    #tests.append([42, 36, "aiuhigwjk", "iughwr", 21872])
    #tests.append([1j]) # = i = sqrt(-1)

    for test_case in tests:
        print(f'\nBeginning test case: {repr(test_case)}')
        test_case_squared = get_squares(test_case)
        print(f"Squared data: {repr(test_case_squared)}")
        # print original data here
        print(f"Original data: {repr(test_case)}")
