"""
----- NAME: Knapsack Problem -----
----- Category: Dynamic programming -----
----- Level : Hard -----
------ BRIEF ------

You are given an array arrays where each subarray holds two integer values and represent an item;
- the first integer is the item's monetary value,
- the second integer is the item's weight. 

You're also given an integer representing the maximum capacity of a knapsack that you have.

Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsacks's capacity, 
all the while maximizing their combined monetary value. Note that you only have one of each item at your disposal.

Write a function that returns the maximized combined value of the items that you should pick as well as an array of the indices of each item picked.

If there are multiple combinations of items that maximize the total value in the knapsack, your function can return any of them.

Sample input:
items = [[1,2],[4,3],[5,6],[6,7]]
capacity = 10

Sample output:
[10,[1,3]] # item 1) [4,3] and item 2) [6,7]

------ Hints ------
- Try building a two-dimensional array of the maximum values that knapsacks of all capacity is between 0 and c inclusive could hold,
 given one, two, three, etc, items. Let columns represent capacities and rows represent items.

- Build up the array mentioned above one row at a time. 
In other words, find the maximum values and knapsacks of all capacity is between 0 and see can hold with only one item, then to, etc, until use all items. 
Find a formula that relates the maximum value at any given point to previous values.

- Back track your way through the two-dimensional array mentioned in the first tend to find which items are in your knapsack. 
Start at the final index of the array and check whether or not the value stored at the index is equal to the value located one row above.
If it isn't, then te item represented by the current row is in the knapssack.

------ Complexity ------ 
Time: O(nc) where n is the number of items and c is the capacity of the bag 
Space: O(nc) as above

------ Approach ------
values = 2D array where x is possible weight and y is item pairs
W = weight
V= Value

if w =< j: 
values[i][j] = max(values[i-1][j] , values[i-1][j-w] + v)

if w > k:
    values[i][j] = values[i-1][j]
"""

####################################################
## Time: O(nc) - where n is the length of the items and c is the capcity
## Space: O(n) - 
####################################################


def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]                               # -1 because we have the first row with now items
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1 ):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(
					knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue
				)
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:                        # not at the first row
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))
