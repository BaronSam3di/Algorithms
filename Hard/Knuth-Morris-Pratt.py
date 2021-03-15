"""
----- NAME: Knuth-Morris-Pratt (KNP) Algorithm -----
----- Category: Famous Algorithms / Strings -----
----- Level : Hard -----
------ BRIEF ------
Write a function that takes in two sttrings and checks if the first string contains the second one using the KNP algorithm. 
The function shoudl return a boolean. 



------ Hints ------


------ Complexity ------ 
Time: O(n + m)
Space: O(m) where m is the length of your substring.

------ Approach ------
The solutions takes advantage of the patterns in the strings. 
Cacheing patterns in a list 
1. Traverse the sub string and build a list of patterns we identity in the substring.
2, initialise a scores array to a bunch of -1's.
3. compare the first two integers in the substring , i and j.
    once the values at i and j match we write the index of j at the location of i's index at the array.
    This array will reference the indices of where there was a matching substring so we don't need to go back to the start of our substring string.
    for example [-1,-1,-1,0,-1,0,1,2,3,2,3] where a -1 means there was no match. Arbitrarily, a 2 means at index 2.


"""

####################################################

def knuthMorrisPrattAlgorithm(string, substring):
    pattern = buildPattern(substring)
    return doesMatch(string, substring, pattern)

def buildPattern(substring):
    pattern = [-1 for i in substring]
    j = 0
    i = 1
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else: 
            i += 1
    return pattern

def doesMatch(string, substring , pattern):
    j = 0
    i = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:                 # j is the last char in the substring
                return True                             # ...then we have a match
            i += 1
            j += 1
        elif j > 0:                                      
            j = pattern[j - 1] + 1                       # got pack to the pattern and then move up one and start again
        else:
            i += 1
    return False

