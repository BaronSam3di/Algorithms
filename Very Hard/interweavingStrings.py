"""
----- NAME: Interweaving strings -----
----- Category: Recursion -----
----- Level : Very HArd -----
# Has a recursive solution 
------ BRIEF ------

Write a function that takes in three strings and returns a boolean representing whether the third string can be formed by interweaving the first two strings.

To enter wave strings means to match them by alternating their letters without any specific pattern.
For instance, the strings "abc" and "123 can be interwoven as "a1b2c3", and as "abc123" ( This list is nonexhaustive).

Letters within a string must maintain the relative ordering in the interwoven string.


String a 
String b 
String c

------ Hints ------


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

Declare three variables for hte three strings that we will traverse the three strings with.
for char a and b, are one of these in the result string?
if one of the letters is equal, the recursive call starts. 


Experiment with running it with local print statements
"""

####################################################
## With cacheing 
## Time: O(ab) -   
## Space: O(nm) - 
####################################################
# the cache will be mainly looking for false values.

def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    # initialise the cache to allow out indices going out of bounds by 1
    cache = [[None for j in range(len(two)+1)] for i in range(len(one) + 1)]        
    return areInterwoven(one, two, three, 0,0, cache)

def areInterwoven(one,two,three, i , j, cache):
    print("again")
    if cache[i][j] is not None:                 
        return cache[i][j]              # return the boolean stored at that value

    k = i + j
    if k == len(three):                 #
        return True

    if i < len(one) and one[i] ==three[k]:
        cache[i][j] =  areInterwoven(one, two, three , i + 1, j ,cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] ==three[k]:
        cache[i][j] = areInterwoven(one, two, three, i , j + 1,cache)
        return cache[i][j]

    cache[i][j] = False                 # cache does not contain the 
    return False



####################################################
## Naive solution Without cacheing 
## Time: O(2^(n+m) - where m is the first drink in n is the second string
## Space: O(n+m) - 
####################################################


def interweavingStrings(one, two, three):
    # edge case check for sum length == length of 3
    if len(three) != len(one) + len(two):
        return False

    return areInterwoven(one, two, three, 0, 0)


def areInterwoven(one,two,three, i , j):                    # pass in strings and indices

    k = i + j   
    if k == len(three):                                     # we have brought i and j to the ends of their strings so we are done
        return True

    if i < len(one) and one[i] == three[k]:                 # inside string 1 and we are matching with the char in string 3
        if areInterwoven(one, two, three , i + 1, j ):      # If we are interwoven ...
            return True                                     # ... return True

    if j < len(two) and two[j] == three[k]:                  # inside string 2 and we are matching with the char in string 3
        return areInterwoven(one, two, three, i , j + 1)    #

    return False                                            # We are not dealing with interwoven strings at this point 