"""
----- NAME: Largest Range -----
----- Category: Arrays -----
----- Level: Hard  -----
------ BRIEF ------
Write a function that takes in an array of integers and returns an array of length to representing the largest range of integers contained in that array. 
A range is the a subrange of integers. For example, you may have a 15 numbers covering 1-5 , 7-14, 15-18 all jumbled up. The largest range would be 7-14.
The first number in the output array should be the first value in the range, well the second number should be the last value in the range.

A range of numbers is defined as a set of numbers they come right after each other in the set of real integers.
For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5.
Note the numbers do not need to be sorted or adjacent in the input array in order to form a range.

You can assume that there will only be one largest range. 

Sample input:
array = [1, 11, 3, 0 , 1, 15, 5, 2 ,4, 10, 7,12, 6]

Sample output:
[0, 7]

------ Hints ------
- How can you use a hashtag able to solve this problem with an algorithm that runs in linear time?

- Iterate through the input array once, storing every unique number in a hash table and mapping every number to a falsy value.
This hash table will not only provide fast access of the numbers in the input array,
but it will also allow you to keep track of "visited" and and "visited" numbers, 
so as not to unnecessarily repeat work.

- It's right through the input array once more, this time stopping at every number to check if the number is marked as visited in the hash table. 
If it is, skip it; if it isn't, Start expanding outwards from that number with the left number and the right number,
continuously checking if those left and right numbers are in the hash table (and us in the end array), 
and marking them as we visited in the hash table if they are.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

"""

####################################################
## Time: O(n) - where n is the length of the array
## Space: O(n) - 
####################################################

def largestRange(array):

    bestRange = []
    longestLength = 0
    nums = {}

    for num in array:
        nums[num] = True
    
    for num in array:
        if not nums[num]:                       # check if its been explored (if its false its been explored already ) 
            continue
        nums[num] = False
        currentLength = 1           
        left = num - 1
        right = num + 1

        while left in nums:                     # its in the input arrray
            nums[left] = False  
            currentLength += 1                  # increase the length by 1
            left -= 1                           # keep looking to the eft
        
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]    # + and - because we decrement/increment out of range so we need to bring these values back in range.
    
    return bestRange
