"""
---Easy---
BRIEF:
Take an array of distinct integer values and an 'target sum' integer value. 
Write a function that will take both of these values and 
find if there is a pair of numbers anywhere in the array that some up to the target sum.

For example : [ 3, 5, -4, 8, 11, -1, 6] , 10 

------------------------ Two For loops ----------------------- 
Two for loops would work as a brute force method. But this is not as optimal in time , specifically O(2n) time. 

------------------------ Sorted array ------------------------ 
Time: O(n log(n)) 
Space: O(1)

To extend on this sorting the array would

[-4, -1, 1, 3, 5, 6, 8, 11] , 10

We would crate a left pointer under the left most point in the sorted array, and a right pointer at the right most.
We can then sum up the values of what these two pointers. If we discover that the total is less than our target 
value and that all the number are in sorted order, moving hte right pointer would make the sum would be even smaller, which is not what we want. 
Therefore we should move the left pointer to the right to make a greater sum. 
We cna then update our sum. 

This created two rules: 
- If the sum is too small move the left pointer to the right. 
- If the sum is too large move the right pointer to the left. 

------------------------ IMPLEMENTATION: Hash table ---------------- 

A hash table could be better , tradeing up a bit of space and less time. 
This will give us constant time access to a collection of all the numbers.

y = target sum - HashedDistinctInteger

Time = O(n) - This is because we are traversing the array only once and each number we are solving for y. 
After that we are accessing values in a hash table with is constant time.
"""



""
# Two 'for loop' approach
# O(n^2) time \ O(1) space
""
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum , secondNum]

    return []             # return empty array when none are found  


""
# Hash table approach
# O(n) time \ O(n) space ( better if you value space ) 
""
def twoNumberSum(array, targetSum):
    hashTableOfNums = {}
    for num in array:
        potentialMatch = targetSum - sum
        if potentialMatch in hashTableOfNums:
            return [potentialMatch, num]
        else:
            hashTableOfNums[num] = True
    return []


""
# Two pointer approach
# O(n log(n)) time \ O(1) space ( better if you value time ) 
""
def twoNumberSum(array, targetSum):
    array.sort()
    leftPointer = 0
    rightPointer = len(array) - 1
    while leftPointer < rightPointer:
        currentSum = array[leftPointer] + array[rightPointer]
        if currentSum == targetSum:
           return [array[leftPointer], array[rightPointer]]
        elif currentSum < targetSum:
            leftPointer += 1
        elif currentSum > targetSum:
            rightPointer -= 1
    return []