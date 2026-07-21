from test_cases import set_test_cases

def get_squares(numbers):
    '''
        No longer squares mutable input.
    '''
    result = []

    # try:
    for i, number in enumerate(numbers):
        result.append(number ** 2)
    # except (RuntimeError, ValueError) as e:
    #     print(f"ERROR: {e}")
    #     return None

    return result


if __name__ == "__main__":
    test_cases = set_test_cases()
    for test_case in test_cases:
        try:
            print(f'\nBeginning test case: {test_case}.')
            test_case_squared = get_squares(test_case)
            print(f"Squared data: {test_case_squared}")
            print(f"Original data: {test_case}")
        except (ValueError, TypeError) as e:
            print(f'\nERROR: {e}')
            continue