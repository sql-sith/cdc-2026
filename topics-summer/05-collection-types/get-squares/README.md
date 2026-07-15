# Get Squares

Given a list of integers, return a list of their squares. Remember, in Python, lists are enclosed with square brackets:

| Expression           | What is it? |
| -------------------- | ----------- |
| [1, 2, 3]            | list        |
| (1, 2, 3)            | tuple       |
| {1, 2, 3}            | set         |
| {1: "one", 2: "two"} | dict        |

Tests:

1. `get_squares([6])` should return `[36]`.
2. `get_squares([])` should return `[]`.
3. `get_squares([5,2,3])` should return `[25,4,9]`.
4. `get_squares([-1, 0, 1])` should return `[1,0,1]`.

We will begin with a walkthrough of an existing script named `get-squares-00-earthworm.py`. Instead of using precious metals this week to indicate which scripts are better, we are using the names of snakes ... and "earthworm," for the lowest level.

Create the test cases in your __main__ code section using this code:

```python
tests = []
tests.append([6])                 # should return [36]
tests.append([])                  # should return []
tests.append([5,2,3])             # should return [25, 4, 9]
tests.append([-1, 0, 1])          # should return [-1, 0, 1]
tests.append(["abc", {1, 2, 3}])  # should return ... what?
tests.append([42])                # should return 1764
                                  #    ...but will it run?
```

In addition to printing the result of "squaring" the result of your program, add code to print the original list that you passed in?

## Bonus Question

Try running these invocations of your code and see which ones work. For each that does not, why doesn't it? Which of the broken invocations (if any exist) seem like they'd be a good idea to fix?

1. Passing in a tuple instead of a list:

- `get_squares((10, 5, 2))` should return `[100, 25, 4]`

2. Passing in a set instead of a list:

- `get_squares({6, 7})` should return `[36, 49]`

3. Passing in a dict instead of a list:

- `get_squares({1: 12, 15: 6})` will probably return `[1, 15]` (it squares the keys, not the values).
- Can you make this invocation work, squaring the values instead of the keys so that it returns `[144, 36]`? Can you do this without breaking the existing functionality?
