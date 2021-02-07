"""
----- BInarySearch : Level Easy -----
------ BRIEF ------
Write a function that takes in a sorted array of integers as well as a target integer. 
The function should use the Binary Search algorithm to determine if the target is contained in 
the array and should return its index if it is , otherwise -1.


Note: Being Sorted is a key point and requirement of Binary search.

------ Hints ------

1. The Binary Search algorithm works by finding the number in the middle of the input array and comparing it to the target number. 
Given that the array is sorted, if this middle number is smaller than the target number, then 
the entire left part of the array is no longer worth exploring since the target number can no longer be in it; similarly,
if the middle number is greater than the target number, then the entire right part of the array is no longer worth exploring. 
Applying this logic recursively eliminates half of the array until the number is found or until the array runs out of numbers.

2. write helper function that takes in two additional arguments: a left pointer and a right pointer representing the indices at 
the extremities of the array ( or subarray) that you are applying binary Search on. The first time this helper function is called,
the left pointer should be zero and the right pointer should be the final index of the input array. To find the index of 
the middle number mentioned above, simply round down the number obtained from (left + right) / 2. 
Apply this logic recursively until you find the target number or until the left pointer becomes greater than the right pointer.

------ Complexity ------ 
Time : O(log(n)) - where n is the length of the input array. This is because every cycle we are getting rid of half of the data.
Space: O(1) - 

------ Recursive Formula ------
Space: O(log(n)) - because of the call stack memory usage.  
------ Iterative Approach ------
Space: O(1) - This is because you don't need additional memory ot store , you can do it all in place in the array.

"""
# Recursive approach
# O( log(n)) time | # O( log(n)) space
def binarySearch(array,target):
    return binarySearchHelper(array, target, 0, len(array) -1 )

def binarySearchHelper(array, target, leftPointer, rightPointer):
    # base case
    if leftPointer > rightPointer:
        return -1
    middlePointer = (leftPointer + rightPointer) // 2    # floor div to round down
    potentialMatch = array[middlePointer]
    if target == potentialMatch:
        return middlePointer
    elif target < potentialMatch:
        # recursive case
        return binarySearchHelper(array , target, leftPointer, middlePointer - 1) # middle -1 becomes the new RIGHT pointer so we can ignore half the data
    else:
        # if the target is < than the match
        return binarySearchHelper(array, target, middlePointer + 1, rightPointer ) # middle +1 becomes the new LEFT pointer so we can ignore half the data


# Iterative approach
def binarySearch(array,target):
    return binarySearchHelper(array, target, 0, len(array) -1 )

def binarySearchHelper(array, target, leftPointer, rightPointer):
    # base case
    while leftPointer <= rightPointer:
        middlePointer = (leftPointer + rightPointer) // 2    # floor div to round down
        potentialMatch = array[middlePointer]
        if target == potentialMatch:
            return middlePointer
        elif target < potentialMatch:
            rightPointer = middlePointer - 1
        else:
            leftPointer = middlePointer + 1
    return -1