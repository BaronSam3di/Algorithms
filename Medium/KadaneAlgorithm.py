"""
----- NAME: Kadane's Algorithm -----
----- Category: Famous Algorithms -----
----- Level : Medium  -----
------ BRIEF ------

Aimed at solving the "maximum subarray problem".


Write a function that takes in a non-empty array of integers and returns the maximum sum that
can be obtained by summing up all of the integers in a non-empty subarray of the input array.

A subarray must only contain adjacent numbers (numbers next to each other in the input array).

Remember , you don't need to return the sub array, juts the sum

For example with this array: [3,5,-9 ,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
the functions would return 19 because 19 is the sum of [1,3,-2,3,4,7,2,-9,6,3,1]

------ Hints ------


------ Complexity ------ 


------  Approach ------

USe dynamic programming. 
Solve the problem by checking the total for subarrays that end in different values.

"""

####################################################
## Time O(n) | Space O(1) - where n is the length of the array
####################################################
def kadanesAlgorithm(array):
    maxEndingHere = array[0]                                    # initialise the 
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num,maxEndingHere + num)            # formula 1 
        maxSoFar = max(maxSoFar,maxEndingHere)                  # formula 2
    return maxSoFar
