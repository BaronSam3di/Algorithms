"""
----- First Duplicate Value : Medium -----
------ BRIEF ------

Given an array of integers between 1 and n, inclusive, where n is the length of the array,
write a function that:
- returns the first integer that is first to appear more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, 
your function should return the one whose first duplicate value has the minimum index.
If no integer appears more than once, you function should return -1.

Note that you're not allows to mutate the input array.

Ideas
- Could use a set?
- Could use a dictionary? 
------ Hints ------

"""
## My First Approach : Time O(n), Space O(1).
def firstDuplicateValue(array):
	cache = {}
	for num in array:
		if num not in cache:
			cache[num] = 1
			continue
		if num in cache:
			return num
    return -1

## Bruteforce Approach
def firstDuplicateValue(array):
    minimumSecondindex = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range(i + 1, len(array)):
            valueToCompare = array[j]
            if value == valueToCompare:
                minimumSecondIndex = min(minimumSecondIndex, j)

    if minimumSecondIndex == len(array):
            return -1
    return array[minimumSecondIndex]

## AE second best version
def firstDuplicateValue(array):
	seen = set()
	for value in array:
		if value in seen:
			return value
        seen.add(value)
    return -1

''' IN this solution we are using the index of the data structure as a marker. We know the values will be between 1 and n (the length of the array) 
If a value has been seen, we go to the index that has the same number as that value. eg ; if we see a 2 at index 6, we go to index 6 and turn the value negative; whatever the value is. 
This is a sign we have seen a 6 already, regardless of what value is stored at index 6.'''
def firstDuplicateValue(array):
	for value in array:
        if array[abs(value) - 1] < 0:
            return abs(value)
        array[abs(value) - 1 ] *= -1    
    return -1