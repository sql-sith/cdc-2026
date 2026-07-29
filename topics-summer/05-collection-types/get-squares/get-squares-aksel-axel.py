# cspell: ignore aiuhigwjk iughwr

def get_squares(numbers):
    """Get the square of all the elements of an iterable.
    """
    # >> Setup and dictionary checking <<
    new_numbers = []
    keys_of_dict = []
    numbers_was_dict = False
    if isinstance(numbers, dict):
        numbers_was_dict = True
        # ^ Because `numbers` becomes an itterable in this
        #   if statement, it's not possible to rely on the
        #   `isinstance` used lower down in this function.
        keys_of_dict = list(numbers)
        numbers = numbers.values()
    # >> Squaring <<
    for number in numbers:
        try:
            new_numbers.append(number ** 2)
        except TypeError:
            new_numbers.append(None)
    # >> Return the same type inputted <<
    if numbers_was_dict:
        new_dict = {}
        for k, v in zip(
            keys_of_dict,
            new_numbers):
            new_dict[k] = v
        return new_dict
    if isinstance(numbers, set):
        return set(new_numbers)
    if isinstance(numbers, list):
        return new_numbers
    if isinstance(numbers, tuple):
        return tuple(new_numbers)
    if isinstance(numbers, str):
        return "I hate being squared."
    if isinstance(numbers, bytes):
        return b"I hate being squared."
    # >> Fallback to returning a list of squared values <<
    return new_numbers


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
