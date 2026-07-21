# A Grab Bag of Problems

Tonight, there are three problems for you to choose from. When I tell you which ones are more or less difficult, that is based on my assessment of how a typical student in our class would see the problems. I could be wrong.

1. **The Eagle Has Landed**
   This problem has you pick out a safe place to land on the moon. Good luck. It's the hardest one, as it involves arrays of arrays (two-dimensional arrays), and we haven't talked about them yet, although I'm sure W3Schools discusses them at some point.
2. **When is My Party?**
   This has you determine how many days it is until a person's next birthday. You can start from the date given and count up to the end of that month, then add in all the days from the upcoming months until you get to their birthday month, and then add in the number of days until their birthday in that last month. There is an easier way to do it if you search for some documentation. I've labeled this one as moderate difficulty.
3. **Word Smashup**
   I've labeled this one as the easiest, as you get to split words in half and smush them together. There are a couple of additional rules you need to pay attention to, though.


## Quick Primer on Arrays of Arrays.

> Note: in the README for **The Eagle Has Landed**, they give an example array that is also used as the first test case. However, it's a square array (2 by 2), so it doesn't necessarily make clear how you address arrays of arrays if you've never seen them before. I'm going to show you how to do that with an array of arrays that is not a square, so that the pattern is (hopefully) more clear. If you read the comments and the code, it should explain what I'd like you to know.

```python
grid = [[1,2,3,4],[5,6,7,8]]
# the above statement is the same as:
grid = [
    [1,2,3,4]
    [5,6,7,8]
]
print(grid)
[[1, 2, 3, 4], [5, 6, 7, 8]]
# grid is an array with two members:
print(grid[0])
[1, 2, 3, 4]
print(grid[1])
[5, 6, 7, 8]

# grid[0] and grid[1] are both arrays with four members each:
print (grid[0][0], grid[0][1], grid[0][2], grid[0][3])
1 2 3 4

print (grid[1][0], grid[1][1], grid[1][2], grid[1][3])
5 6 7 8

# So, in the test case, when they say that the top-right corner of the 
# following two-dimensional array is the safest spot, they call that array 
# location `[0][1]`. That's because it's it is in the first array (index 
# number 0), and within that array it is in the second spot (index number 1).

grid = [
  [1, 0],   # grid array 0 (grid[0]) containing grid[0][0] and grid[0][1]
  [2, 0]    # grid array 1 (grid[1]) containing grid[1][0] and grid[1][1]
]
```
