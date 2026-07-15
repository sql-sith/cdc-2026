import sys
from argparse import Namespace
from collections.abc import Iterable
import argparse
from typing import Any
from test_cases import set_test_cases

def get_squares(numbers):
    try:
        result = []
        for i, number in enumerate(numbers):
            result.append(number ** 2)
    except Exception as e:
        print(f'ERROR [get_squares]: {e}')
        return []

    return type(numbers)(result)


if __name__ == "__main__":
    test_cases = set_test_cases()
    for test_case in test_cases:
        try:
            print(f'\nBeginning test case: {test_case}.')
            test_case_squared = get_squares(test_case)
            print(f"Squared data: {test_case_squared}")
            print(f"Original data: {test_case}")
        except (ValueError, TypeError) as e:
            print(f'ERROR [main]: {e}')
            continue
