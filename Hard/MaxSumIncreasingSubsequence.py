"""
----- NAME: Max Sum Increasing Subsequence -----
----- Category: Dynamic programming -----
----- Level : Hard -----
------ BRIEF ------

Write a function that takes in a non-empty array of integers and returns the greatest sum that
can be generated from a strictly-increasing subsequence in the array as well as an array of the numbers in that subsequence.

(Strictly as in cannot be equal)

A sub sequence of an array is a set of numbers that aren't necessarily adjacent in the array but there are in the same order as they appear in the array.
For instance, the numbers [1, 3, 4] form a subsequence of the array [1,2,3,4], and so do the numbers [2 ,4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

You can assume that there will only be one increasing subsequence with the greatest sum.

Sample input:   array = [ 10, 17, 20, 30, 50, 11, 30]
Sample output:  array [110, [10, 20, 30, 50]] // The sub sequence [10, 20, 30, 50] is strictly increasing and use the greatest son:110.


------ Hints -----
- Try building an array of the same length as the input array. At each index in this new array,
store the maximum sum that can be generated from an increasing subsequent ending with the number found that index in the input array.

- Can you efficiently keep track of potential sequences in another array?
Instead of storing entire sequences, try storing the indices of previous numbers.
For example, at index three in this other array,
store the index of the before-last number in the max-sum increasing subsequent ending with the number at index 3.

------ Complexity ------ 
Time: O() 
Space: O() 

------ Approach ------

"""

####################################################
## Time: O(n^2) - where n is the length of the input array . ^2 because we have to check back on all values at each iteration
## Space: O(n) - Building an  array the size of the array
####################################################

def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]               # Store the index of the previous number in the increasing sub sequence that ends up at that index 
    sums = [num for num in array]
    maxSumIdx = 0

    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx],buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))