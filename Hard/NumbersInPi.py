"""
----- NAME: Numbers in Pi -----
----- Category: Dynamic programming -----
----- Level: Hard -----
# Has a recursive solution 
------ BRIEF ------
Given a strong representation of the first n digits of pi and a list of positive integers (all in string format), 
write a function that returns the smallest number of spaces that could be added to the n digits of pi such that 
all resulting numbers (with the spaces added to them) are found in the list of integers.

Note that a single number canapé multiple times in the resulting numbers. For example, if pie is "3141" and the numbers are ["1",3"."4"], 
the number "1" is allowed to appear twice in the list of resulting numbers after three spaces are added: "3 | 1 | 4 | 1".

If no number of spaces to be added exist such that all resulting numbers are found in the list of integers, the function should return -1.

Sample Input:
pi = "3141592653589793238462643383279"
numbers = ["314159265358979323846", "26433", "8", "3279","314159265", "35897932384626433832", "79"]

Sample Output:
2           # "314159265" | "35897932384626433832" | "79"
------ Hints ------
- You'll need to look numbers up quickly; is the emperor the best data structure for this?

- Don't every favorite number in a hash table for fast look-up. 
Iterate through the digits of pi, checking if every prefix of the 10 digits is a favorite number.
What should you do if you find a prefix of the N digits of pi is a favourite number?

- If you find a prefix of the digits of pi that is a favorite number, try adding one space after it and then recursively calculating the smallest number of spaces in the suffix that comes after it.
 Do this for every prefix, and your find the answer. Can this message be optimised with the cache?


------ Complexity ------ 
Time: O(n^3 + m ) - Why exactly?
Space: O(n+m) - where n is the length of the pi number and m is the length of the digits

------ Approach ------

"""

####################################################
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################

def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers} # hash table  of out numbers
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces   

# helper function
def getMinSpaces(pi, numbersTable, cache, idx): # Starting index
	# base case
	if idx ==len(pi):
		return -1

	if idx in cache:                                    # this is where the time saving is as we just reference the cache
		return cache[idx]                               

	minSpaces = float("inf")
	for i in range(idx, len(pi)):
		prefix = pi[idx : i + 1]                

        # recursive step
		if prefix in numbersTable:
			minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)    
			minSpaces = min(minSpaces, minSpacesInSuffix + 1)               # this line needs more clarity fr me 

	cache[idx] = minSpaces
	return cache[idx]
