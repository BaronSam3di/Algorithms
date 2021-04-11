"""
----- NAME: Longest Common Subsequence -----
----- Category: Dynamic programming -----
----- Level : Hard -----
Related to "Levenstein distance" and "Max Profit with K transactions" They include the space saveing optimiseing that keeps track of two rows and not the entire array.

But these are not the most optimal . The most optimal is here.

------ BRIEF ------
Write a function that takes into strings and returns their longest common subsequence (LCS).

A sub sequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same order as they appear in the string.
For instance, the characters ["a", "c", "d"] For my sub sequence of the string "abcd", and so do the characters ["b", "d"]. 
Note that a single character in a string and the string itself are both valid subsequences of the string. 

You can assume that there will only be one longest common subsequence. 

Sample input:
str1 - "ZXVVYZW"
str1 = "XKYKZPW"

Sample output ( Longest common subsequence):
["X,"Y","Z","W"]

------ Hints ------
- Try building a two-dimensional array of the longest common sub sequences of sub string pairs of the input strings.
Let the rays of the array represent sub strings of the second input string str2. Let the first wave represent the empty string.
Let each row i thereafter represent the sub strings for str2 from 0 to i, with i excluded. 
Let the columns similarly represent the first input string str1.

- Build up the array mentioned above one row at a time. In other words, find the longest common subsequences for all the substrings of str1
represented by the columns and the empty string represented by the first row,
then all the sub strings of str1 represented by the columns and the first letter of str2 represented by the secondary etc, until you comare both full strings.
Find a formula relates the longest common sub sequence at any given point to previous sub sequences. 

- Do you really need to build and store sub sequences age point in the two-dimensional array mentioned above?
Try storing billions to determine whether or not a letter at a given point in the two-dimensional array it's part of the longest common subsequence 
as well as pointers to determine what should come before this letter in the final sub sequence.
Use these pointers to backtrack your way through the array and to build up the longest common sub sequence at the end of your algorithm. 


------ Complexity ------ 
Time: O(nm*min(n,m)) 
Space: O(nm*min(n,m)) 

------ Approach ------

"""

####################################################
## Solution 1 - 
## Time: O(nm*min(m,n)) - Where m is the length of string one and n is the length of string two. 
## Space: O(nm*min(m,n)) - because we will be storing all these values
####################################################
from typing import Coroutine


def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1) +1)] for y in range(len(str2) +1 )]  # intitialise . -1 to factor in the ""
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:                                  # are the last two letters equal. -1 to factor in the ""

                lcs[i][j] == lcs[i - 1][j - 1] + [str2[i - 1]]              # the lcs is the lcs plus the new letter as an array
            else:
                # max of the value above against the value to the left 
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key = len)    # key = len is the saying we are useing hte length rather than say the abs
        return lcs[-1][-1]
 


####################################################
## Solution 1 
## Time: O(nm) - where n is 
## Space: O(nm) - 
####################################################

def longestCommonSubsequence(str1, str2):
    # None 1 == place to store the current letter IF it is being used in the current lcs, else None
    # 0 == current length of lcs which we read on the fly
    # None 2 == pointer to the previous i index of the lcs
    # None 3 == pointer to the previous j index of the lcs
    lcs = [[ [None, 0 , None, None ] for x in range(len(str1)+1)] for y in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:

                lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
            else:
                if lcs[i - 1][j][1] > lcs[i][j - 1] [1]:                       # if the lcs above is greater than the lcs to the left
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1 , j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i  , j - 1]
    return buildSequence(lcs)

def buildSequence(lcs):

    sequence = []
    i = len(lcs) - 1                                                         # Final row in the lcs
    j = len(lcs[0]) - 1                                                      # Final col in the lcs

    while i != 0 and j != 0:
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None:
            sequence.append(currentEntry[0])
        i = currentEntry[2]                                                  #  The previous i index
        j = currentEntry[3]                                                  #  The previous j index
    return list(reversed(sequence))



####################################################
## Solution 1 
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################
def longestCommonSubsequence(str1, str2):
    # Write your code here.
    pass

####################################################
## Solution 1 
## Time: O(n) - where n is 
## Space: O(n) - 
###################################################