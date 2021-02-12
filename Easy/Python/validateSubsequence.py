"""
------- Validate SubSequence : Easy -------
Given two non-empty arrays of integers, write a function that determines wheather the
second (sub) array is a subsequence of the main (N) one. 

A subsequence of an array is a set of numbers that aren't necessarily adjacent 
in the array but that are in the same order as they appear in the array.

For instance, the numbers [1,3,4] form a subsequence of the array [1,2,3,4] 
and so do the numbers [2,4]. Note that a single number in an array and the array
itself are both valid subsequences of the array.

------- Solution -------
We are going to have to traverse both arrays. 
We will initialise a pointer under the first element of the subsequence and then 
traverses the main array looking for that in the main array.

Each time we find a match in the main array ot the pointer we move the pointer to the right. 
As soon as a sub array element is not found wwe cna ignore the rest of the sub array and end the algorithm.
Once we have exhausted the entire sub array pointer the algorithm ends. 

Complexity 
Time : O(N)  where N is the main array. 
Space: O(1)
"""

# O(n) time | O(1) space
def validateSubsequence(mainArray , candidateArray):
    arrayIndex = 0.
    candidateIndex = 0
    while arrayIndex < len(mainArray) and candidateIndex < len(candidateArray): 
        if mainArray[arrayIndex] == candidateArray[candidateIndex]:
            candidateIndex += 1                  # keep score on the matches
        arrayIndex += 1                         # regardless of the result, move on
    return candidateIndex == len(candidateArray)  # If the score matches the len of the S_Array, Its a match

# O(n) time | O(1) space
def validateSubsequence(mainArray, candidateArray):
    candidateIndex = 0               
    for value in mainArray:
        if candidateIndex == len(candidateArray): 
            break 
        if candidateArray[candidateIndex] == value:
            candidateIndex += 1
    return candidateIndex == len(candidateArray)