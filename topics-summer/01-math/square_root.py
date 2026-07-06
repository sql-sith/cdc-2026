'''
Functions to estimate square root values.

Created on Dec 16, 2014
@author: sql.sith
'''
# from __builtin__ import False, True

def square_root(target, tolerance):
    guess = 0
    guesses = 0

    while (abs(guess * guess - target) > tolerance and
           guess * guess < target):
        guess += 0.00001
        if _debug:
            print(guess)
        guesses += 1

    if abs(guess * guess - target) > tolerance:
        raise(_NO_GOOD_SOLUTION_FOUND)

    if _debug: print(guesses)  # @IgnorePep8

    return(guess)

global _debug
_debug = False

global _NO_GOOD_SOLUTION_FOUND
_NO_GOOD_SOLUTION_FOUND = Exception(
    "Solution found is outside specified tolerance.")

if __name__ == '__main__':
    _debug = True

    square = 40
    tolerance = 0.001
    sqrt = square_root(square, tolerance)

    print("The square root of {0} is {1}.".format(square, sqrt))
    if _debug:
        print(sqrt * sqrt)

from copy import deepcopy
nested_list = [[1, 2], [3, 4]]
deep_copy = deepcopy(nested_list)
deep_copy[0][0] = 99
print(nested_list) # Output: [[1, 2], [3, 4]]
print(deep_copy) # Output: [[99, 2], [3, 4]]