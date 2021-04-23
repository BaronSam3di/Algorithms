"""
----- NAME: Four Number Sum -----
----- Category: Arrays -----
----- Level: Hard  -----
------ BRIEF ------

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets (sets of 4 ) in the array this sum up to the target some and
return to dimensional array of these quadruplets in no particular order.

If no four numbers sum up to the target some, the function should return an empty array.

Sample input:
array = [7, 6, 4, -1, 1, 2]
targetSum = 16

Sample output:

[[7, 6, 4, -1], [7, 6, 1, 2]] // The quadruplets could be ordered differently 

------ Hints ------
- Using four for loops to calculate the sums of all possible quadruplets in the array would generate an algorithm that runs in O(n^4) time, 
Where N is the length of the input array.
Can you come up with something faster using fewer for loops?

- You can calculate the sums of every pair of numbers in the array in O(n^2) time using just two loops.
Then, assuming that you've stored all the sums in a hash table, 
you can fairly easily find which two sums can be paired to add up to the target sum:
The numbers summing up to these two sums constitute candidates for valid quadruplets; 
you have to make sure that no number was used to generate both of the two sums.

- Your goal is to create a hash table mapping the sums of every pair of numbers in the array to an array of arrays,
with each subarray representing the indices of each pair summing up to that number.
Loop through the input array with a simple for loop. 
Inside this loop, loop through the input array again, starting at the index of the first loop.
At each iteration, calculate the difference between the target sum and the sum of the two numbers represented by the indices of the for loops.
If that difference is in the hash table that you're building,
then valid quadruplets can be formed by combining the current pair of numbers with each pair stored in the hash table at the difference just calculated.
Following this nested for loop, loop through the array again, this time starting at index zero all the way to the index of the first four loop.
At each iteration, calculate the sum of the two numbers represented by the indices of the four loops and add it to the hash table if it isn't already there; 
then add the pair of indices to the array that there is some in the hash table maps to.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

"""

####################################################
## Time: O(n^2) - where n is is the length of the array. At worst n^3
## Space: O(n^2) - worst case storing 
####################################################

def fourNumberSum(array, targetSum):
    
    # initialise hash table and quadruplets array to return at the end
    allPairsSums = {}
    quadruplets = []

    # skip first value as we will have nothing in the hash table
    # skip final values there are no values after it
    for i in range(1, len(array) - 1):               

        # 1st loop
        # Check if there is a value sotrein the hash that corresponds to the difference between 
        # the target sum and the sum of the current two numbers    
        for j in range(i + 1, len(array)):                          # iterate everything after current number
            currentSum  = array[i] + array[j]
            difference = targetSum - currentSum

            if difference in allPairsSums:                          # check if difference is in hash table
                for pair in allPairsSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]]) # add a new quadruplet

        # 2nd Loop 
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairsSums:
                allPairsSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairsSums[currentSum].append([array[k],array[i]])

    return quadruplets