"""
----- NAME: Max Subset No Adjacent -----
----- Category: Dynamic programming -----
----- Level :  -----
------ BRIEF ------
Write a function takes in an array of positive integers and 
returns the maximum some of the non-adjacent elements in the array.

If the input array is empty, the function should return 0.

------ Hints ------


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
total = 0
for i in range(0,array -1,2):
    if total + i < total:
        total += i
return total

maxSums[i] = max(maxSums[i-1] , maxSums[i - 2] + array[i]
  

"""

####################################################
## Time: O(n) - where n is the length of the array 
## Space: O(1) - we only store 3 values at a time so its constant
####################################################

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0],array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first

####################################################
## 
## Time: O(n) - where n is the length of the array 
## Space: O(n) - 
####################################################

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2,len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    return maxSums[-1]



 