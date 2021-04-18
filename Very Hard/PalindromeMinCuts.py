"""
----- NAME: Palindrome Min Cuts -----
----- Category: Dynamic programming -----
----- Level : Very Hard-----
------ BRIEF ------

Given a non-empty string, write a function that returns the minimum number of cuts need to perform 
on the string such that each remaining substring is a palindrome.

A palindrome is defined as a string that's written the same forward as abackward. 
Note that single-character strings are palindromes.

Sample input = "noonabbbad"

Sample Output = 2 // noon | abba | d

------ Hints ------
- Try building a two-dimensional array of the palindromicities of all substrings of the input string.
Let the value stored row i and at column j represent the palindromicity of the substring starting at index I am lending at index j.

- Checking for palindromicity is typically and O(n) time operation. 
Can you eliminiate this step and build the same two-dimensional array mentioned above a different way?
Realize that the substring whose starting and ending indices are (i,j) is also a palindrome.

Build a one-dimensional array of the same length as the input string. 
At each index in this array compute and store the minimum number of cuts needed for the subsring whose starting and ending indices are (0,i).
Use previously calculated values as well as the two-dimensional array mentioned above to fund each value in this array.

------ Complexity ------ 
Time: O(n^3) 
Space: O(n^2) - store 2 arrays: palindromes array and the results array

------ Approach ------
Of the 2D array, store the palindromicity in each index where the row starting index; column ending index
"""

####################################################
## Optimal approach 
## Time: O(n^2) - If we eliminate the isPlaindrome() func
## Space: O(n^2) - store 2 arrays: palindromes array and the results array
####################################################

def palindromePartitioningMinCuts(string):
    palindromes = [[False for i in string] for j in string]

    for i in range(len(string)):
        palindromes[i][i] = True                        # set the diagonal to True. This is a base case
    
    for length in range(2, len(string) + 1):            # look at substrings of 2 or more
        
        # below keeps the substring length below the length of the string 
        for i in range(0, len(string) - length + 1):    #
            j = i + length - 1                          # ending index. -1 to get to the ending index
            
            # instead of is palindromes. This section is the constant time optimisation
            if length == 2:
                palindromes[i][j] = string[i] == string[j]
            else:
                # 
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j - 1]
    
    # as in the the non optimal approach
    cuts = [float("inf") for i in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1
    return cuts[-1]


####################################################
## Naive (but still complex) approach 
## Time: O(n^3) 
## Space: O(n^2) - store 2 arrays: palindromes array and the results array
####################################################

def palindromePartitioningMinCuts(string):
    palindromes = [[False for i in string] for j in string]

    for i in range(len(string)):
        for j in range(i, len(string)):
            palindromes[i][j] = isPalindrome(string[i : j + 1])     # check if the string is a palindrome
    
    cuts = [float("inf") for i in string]                           # this will simplify the action on the final if statement                     
    for i in range(len(string)):        
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1                            
            for j in range(1, i):                                   # iter through all the other substrings
                # Check the string is a palindrome AND min number cuts before is less than what we currently stored at cuts[i] even if we add 1 to it
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1                       # update the current cuts
    
    return cuts[-1]


def isPalindrome(string):
    # two pointer strategy of palindrome check - most optimal  as per clip
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
    
