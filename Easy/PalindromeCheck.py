"""
----- Palindrome check : Easy -----
# Has a recursive solution 
------ BRIEF ------
Write function that takes in a non-empty string and that returns a boolean representing weather the string is a pallindrome.
A palindrome is defined as string that's written the same forward and backward. not tha single-character strings are palindromes.

------ Hints ------
- Start by building the input string in reverse order and comparting this newly built string to the input string. 
Can you do this without using string concatenations.

- Can you optimize the algorithm by using recursion? What are the implications of recursion on an algorithm's space-time complexity analysis?

- GO back to an iterative solution and try useing pointers to solve this problem: Start with a pointer at the first index of the string and a pointer at the final index of the string. 
What can you do from there?
------ Complexity ------ 


------ Recursive Formula ------

def isPalindrome(string):
    return firstLetter == lastLetter AND isPalindrome(remaining middle)

------ Iterative Approach ------

"""


# ################################################################
# ## Reverese string approach - O(n^2) time | O(n) Space 
# ################################################################
# ''' we build a reverese string and then return its comparison with the original. are they the same?  '''
# def isPalindrome(string):
#     revereseString = ""
#     for i in reversed(range(len(string))):
#         revereseString += string[i]
#     return string == revereseString 

# ################################################################
## Reverese list approach - O(n) time | O(n) Space
################################################################
'''  '''
def isPalindrome(string):
    revereseChars = []
    for i in reversed(range(len(string))):
        revereseChars.append(string[i])
    return string == "".join(revereseChars) 


# ################################################################
## Recursive - O(n) time | O(n) Space
################################################################

def isPalindrome(string, i = 0):
    j = len(string) - 1 -i              #  J is the last letter 
    return True if i >= j else string[i] == string [j] and isPalindrome(string, i + 1) # 


# ################################################################
## Recursive : with Tail recursion - O(n) time | O(n) Space
################################################################

def isPalindrome(string, i = 0):
    j = len(string) - 1 -i              #  J is the last letter 
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string, i + 1)      # this tail recursion is compiler dependent

# ################################################################
## Iterative with Pointers :  - O(n) time | O(1) Space
################################################################

def isPalindrome(string):
    leftIDx = 0 
    rightIdx = len(string) - 1
    while leftIDx < rightIdx:
        if string[leftIDx] != string[rightIdx]:     # As long as this doesn't happen it is still could be a palindrome
            return False
        leftIDx += 1
        rightIdx -= 1
    return True