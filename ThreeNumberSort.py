"""
----- Three Number Sort : Medium -----

------ BRIEF ------
You are given a main array of integers and another array of three unique integers.
The first array is guaranteed to only contain integers that are in the second array, 
and the second array represents a desired order for the integers in the first array.

For example, a second array of [x, y, z] respresents a desired order 
of [x, x, ..., x, y, y,..., y, z, ..., z] in the first array.

Write a function that sorts the first array to the desired order in the second array.

The function should perform this in place (i.e, it should run with constant space: O(1) space.)

Note that the desired order won't necessarily be ascending or descending and that the first array 
won't necessarily contain all three integers found 
in the second array - it might only contain one or two.

------ Hints ------

------ Complexity ------ 

------ ## Naive approach
# Bucket approach
You make three buckets for each value in the unique array and then count the amounts of each value in the main array. You then the amounts of these values into the main array ( or reorder it).
This requires at east two passes of counting over.




"""

## First pass

def threeNumberSort(array, order):
	for key, val in enumerate(array):
		if val == order[0]:
			array.insert(0, array.pop(key))
		if val == order[2]:
			array.insert(len(array), array.pop(key))
	return array

## Naive Approach Time: O(n) , Space O(1) - where n is the length of the array
def threeNumberSort(array, order):
    valueCounts = [0,0,0]                           # these 3 will act like the buckets

    for element in array:                           
        orderIdx = order.index(element)             # get the comparative index of the element in the order array 
        valueCounts[orderIdx] += 1                  # add a count of the value 
    
    for i in range(3):
        value = order[i]
        count = valueCounts[i]

        numElementsBefore = sum(valueCounts[:i])    # the starting index to be changeing these new values at
        for n in range(count):
            currentIdx = numElementsBefore + n 
            array[currentIdx] = value
    
    return array


## 2nd Approach Time: O(n) , Space O(1) - where n is the length of the array
def threeNumberSort(array, order):
    firstValue = order[0]
    thirdValue = order[2]

    firstIdx = 0
    for idx in range(len(array)):
        if array[idx] == firstValue:
            array[firstIdx], array[idx] = array[idx], array[firstIdx]
            firstIdx += 1

    thirdIdx = len(array) -1
    for idx in range(len(array) -1, -1, -1):
        if array[idx] == thirdValue:
            array[thirdIdx], array[idx] = array[idx], array[thirdIdx]
            thirdIdx -= 1
    
    return array


## 3rd Approach Time: O(n) , Space O(1) - where n is the length of the array
def threeNumberSort(array, order):
    firstValue = order[0]
    secondValue = order[1]

    firstIdx , secondIdx , thirdIdx = 0 , 0 , len(array) -1


    while secondIdx <= thirdIdx:
        value = array[secondIdx]

        if value == firstValue:
            array[secondIdx], array[firstIdx] = array[firstIdx] , array[secondIdx]
            firstIdx += 1
            secondIdx += 1

        elif value == secondValue:
            secondIdx += 1

        else:
            array[secondIdx], array[thirdIdx] = array[thirdIdx] , array[secondIdx]
            thirdIdx -= 1
    return array