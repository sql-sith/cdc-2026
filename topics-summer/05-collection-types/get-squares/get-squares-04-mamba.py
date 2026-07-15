from collections.abc import Iterable
from types import GeneratorType
from typing import Any


class FormalString(str):
    def __pow__(self, exponent: int) -> 'FormalString':
        """Implements s ** n as concatenating s to itself n times."""
        if not isinstance(exponent, int):
            return NotImplemented
        return FormalString(self * exponent)

    def __mul__(self, other) -> 'FormalString':
        """Implements s * s as s + s, while preserving normal string * int."""
        if isinstance(other, str):
            # If multiplying by another string, concatenate them (Formal Language Math)
            return FormalString(self + other)
        # Otherwise, fall back to standard Python behavior (string * int)
        return FormalString(super().__mul__(other))


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


# def get_squares[T: Collection](x: T) -> T:
def get_squares(x: Iterable):
    # 1. Handle Dictionaries (Mappings)
    # We do this first because dicts iterate over keys by default, losing the values.
    if isinstance(x, dict):
        # Double the values while keeping the original keys
        double_tracked = {k ** 2: v ** 2 for k, v in x.items()}
        result = type(x)(double_tracked)

    # 2. Handle Strings
    elif isinstance(x, str):
        s = FormalString(x)
        result = s * 2

    # 3. Handle Generators / Custom Iterators
    elif isinstance(x, (GeneratorType, map, filter)):
        print("Squaring generators is not supported.")
        return NotImplemented

    # 4. Handle standard collections (list, tuple, set)
    elif type(x) in (list, tuple, set):
        # any of these can be converted to list;
        # this avoids an IDE warning.
        # i hate IDE warnings.
        if len(list(x)) == 0:
            result = x
        else:
            result = (item ** 2 for item in x)

    # 5. Deny other types
    else:
        print('Input data type is not supported.')
        return NotImplemented

    # 6. Convert and return data. Fallback to list if conversion fails.
    try:
        return type(x)(result)
    except TypeError as e:
        print("Cannot match type of original iterable. Falling back to list.")
        return list(result)


if __name__ == "__main__":
    test_cases = set_test_cases()
    for test_case in test_cases:
        try:
            print(f"\nBeginning test case: {test_case} <{type(test_case).__name__}>)")
            test_case_squared = get_squares(test_case)
            print(f"Squared data: {test_case_squared} <{type(test_case_squared).__name__}>")
            print(f"Original data: {test_case} <{type(test_case).__name__}>")
        except (ValueError, TypeError) as e:
            print(f'\nError encountered: {e}')
            continue
