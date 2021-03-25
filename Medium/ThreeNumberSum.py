"""
----- Three Number Sum : Level -----
------ BRIEF ------
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 

The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplits. 

The numbers in each triplet should be ordered in ascending order, and the triplits themselves should be ordered in ascending order with respect to the numbers they hold. 

If no, three numbers sum up to the target sum, the function should return an empty array. 

------ Hints ------

------ Approach ------
- Three for loops is a possibility, similar to two number sum but that would run at O(n^3) time. 

The technique that can be used on other array problems, with a left and a right pointer. 

First we sort the array in assending order. 
 
We set up three pointers: 
- CURRENT NUMBER (CN) - Starting at the lowest number in the array.
- LEFT NUMBER (LN) - For each iteration, starts the number to the right of the CN.
- RIGHT NUMBER (RN) - Right most Number 

CURRENT_SUM = CN + LN + R

IF CURRENT_SUM == TARGET_SUM , append the current sum to our RESULT_ARRAY.

IF CURRENT_SUM < TARGET_SUM , we will move the LEFT pointer UP to get bigger. (Make our SMALLEST number BIGGER)

IF CURRENT_SUM > TARGET_SUM , we will move the RIGHT pointer DOWN to get bigger. (Make our LARGEST number SMALLER)

Once we find our first match we will move both LN and RN pointers one step toward each other.
Once the two pointers pass each other , we are done with this round of iteration.

We then reset the iteration, incrementing the CN and all relative pointers. 



------ Complexity ------ 
Time = O(n^2) - Iterating through like a double for loop.
Space = O(n) - We might end up storing every number. Worst case all numbers are part of a triplet. 
"""

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for idx in range(len(array)-2):         # "- 2" because we are looking for triplets. Our last CN will have to be the third value from the end so we have two further values to try and sum with
        leftPointer = idx + 1
        rightPointer = len(array) -1
        while leftPointer < rightPointer:   # pointers have not passed each other yet. 
            currentSum = array[idx] + array[leftPointer] + array[rightPointer]
            if currentSum == targetSum:
                triplets.append([array[idx], array[leftPointer], array[rightPointer]])
                leftPointer += 1
                rightPointer -= 1
            elif currentSum < targetSum:        # Incramenting left increases CN
                leftPointer += 1
            elif currentSum > targetSum:
                rightPointer -= 1               # decramenting right reduces CN
    return triplets