"""
----- Longest Palindrome Substring : Level -----
------ BRIEF ------
Write a function that, given a string, returns its longest palindrome substring.

A palindromic string is defind as a string that's written the same forward and backward.
Note that single-character strings are panindromes.

You can assumes that there will be one longest palindromic substring. 

------ Hints ------
- Try generateing all possible substrings of the input string and checking for their palindromicity. 
What is the runtime of the isPalindrome check? 
What is the total runtime of this approach? 

------ Time ------
Time: O(n^2) where n is the length of the string. ^2 because we do expansion between two letters and of two letters. 
Space: O(1) because we dont store anything.
------ Approach ------

Naive appriach, check every substring . This is O(n^3)
We need to check if we are in the middle
"""

####################################################
## O(n^2) | O(1) Space
####################################################

def longestPalindromicSubstring(string):
    currentLongest = [0,1]                                          # this only needs to have the index of the start and end index
    for i in range(1, len(string)):                                 # start from 1 because we don't need to check the first char
        odd = getLongestPalindromeFrom(string, i - 1 , i + 1)       # the palindrome that is of odd length at this location. Moving out to the side via i + 1 and i - 1.
        even = getLongestPalindromeFrom(string, i -1 , i)           # even length palindrome centreted between the current letter and the previous letter. Centre of palindrme is between i -1 and i
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])  # update the current longest
    return string[currentLongest[0]:currentLongest[1]]                              # slice the current longest out of the string



def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    # implements the expansion from the middle of the string
    while leftIdx >= 0 and rightIdx < len(string):                  # if we are still in the string
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]







def isPalindrome(string, i = 0):
    j = len(string) - 1 -i              #  J is the last letter 
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string, i + 1)      # this tail recursion is compiler dependent