"""
----- MonoTonicArray : Medium -----

------ BRIEF ------
Write a function that takes in an array of integers and returns a boolean representing weather the array is monotonic.

An array( or Function)  is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. 
Simply, non-decreasing elements aren't necessarily exclusively increasingly; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

------ Hints ------

------ NOTes ------

What about if the numbers are the same! THis is why we have Non-decreasing and non-creaseing. Like a platau.

------ Complexity ------ 
Time: O(n) 
Space: O(1) 

------ Approach 1 ------

First determine the direction the array is going in. 

But what if we had an array [1,1,1,1,2]. IT would be hard to tell the monotonicity from the first two integers.
To be more thorough we can still start with the first two values but we just store a non-meaningful direction , for example 0. 
If we eventually come accross a meaningful direction, by which we mean one that goes down or goes up from the plateau then we compare the difference of the two array values to check if they ever break the meaningful direction. 
The downside with implimenting this approach is it not entirely clear of what the meaning direction variable means.

------ Approach 2 ------
The Second approach is to consider the question in a way that considers if the array is entirely non-decreaseing only. 
Is our array is trending upwards, true or false. This is simpler to implement.
We can then implement a copy of that logic with a second flag.

You assume it's non-decreasing and non-decreasing attributes are both True. The boolean result returned if only one of these is false will still be true, so monotonic.
If it changes direction then both will end up false and the retruns result will be no-monotonic.

"""
## Approach 1 
def isMonotonic(array):
    if len(array) <= 2:                                     # if the array is just one number it will be monotonic
        return True
    direction = array[1] - array[0]                         # 
    for i in range(2, len(array)):      
        if direction == 0:                                  # if the direction is meaningful. Could be the same number for the first 5 numbers etc
            direction = array[i] - array[i -1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    return True

def breaksDirection(direction, previousInt, currentint):
    difference = currentint - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0


## Approach 2
def isMonotonic(array):
    isNonDecreaseing = True
    isNonIncreaseing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:                     # if at any time we are Non-increasing or NonDecreasing, the array is not monotonic
            isNonDecreaseing = False
        if array[i] > array[i - 1]:
            isNonIncreaseing = False
    return isNonDecreaseing or isNonIncreaseing         # if both are still true, then it is Monotonic.
