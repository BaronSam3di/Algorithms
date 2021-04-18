"""
----- NAME: Maximize Expression -----
----- Category: Dynamic programming -----
----- Level : Hard -----

------ BRIEF ------

Write a function that takes in an array of integers 
and returns the largest possible value for the expression: 
array[a] - array[b] + array[c] - array[d], 

where a, b, c, and d are indices of the array and of the indices;  a < b < c < d. 
So if a is the 2nd index, they cannot be the first index.

If the input array has fewer than 4 elements, your function should return zero.

Sample input:
array = [ 3, 6, 1, -3, 2, 7,]

Sample output:
4 
// Choose a = 1, b = 3, c = 4 and d = 5
// -> 6 - (-3) + 2 - 7 = 4

------ Hints ------

- Brute force approach to solving this problem is to simply iterate through every valid choice of a, b, c, and d and to evaluate the expression at each iteration. 
While doing this, you can keep track of the maximum value that you find and return it after considering all possibilities. 
This solution runs at O(n^4).

- You can solve this problem using dynamic programming with a time complexity of O(n); however, you'll need to use external space.

- If you know what the maximum possible value of 'a' is at each index of the array, 
you can find the maximum possible value of 'a - b' at each individual index of the array in O(1) time (or in O(n) time for all indicies).
The same thing holes for finding the maximum possible value of 'a - b + c' If you know the maximum possible value of 'a - b' at least index.
How does this fact help you solve the entire problem in O(n) time?

- Start by finding the maximum possible value of 'a' at each index in the array ,
 meaning the maximum value of 'a' that you can obtain at each index 'i' if 'a' is chosen from an index between 0 and i, inclusive.
 Store all of these values in an array, and use them to help you determine the maximum possible value of 'a - b' At each index.
 Do the same for ('a - b + c' using the results from 'a - b' ) and 'a - b + c - d' (using the results from 'a - b + c'). 
 Once you make it to 'a - b + c - d', you'll be able to determine the maximum value of the expression. 

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
"""
####################################################
## Time: O(n) - 
## Space: O(n) -
## It could be said that this runs in 4n ( space and time) Because we have four of each, but we don't reference constants in BigO
####################################################

def maximizeExpression(array):
    	if len(array) < 4:
            return 0

	maxOfA = [array[0]]                                 
	maxOfAMinusB = [float("-inf")]                          # empty place holder value
	maxOfAMinusBPlusC = [float("-inf")] * 2                 # * 2 because we want two placeholder values to represent a and b
	maxOfAMinusBPlusCMinusD = [float("-inf")] * 3           # * 3 As above because D cannot be index values 0, 1 or 2
	
	for idx in range(1, len(array)):
        # starting at 1 to handle the -1 check below 
        currentMax = max(maxOfA[idx - 1], array[idx])
		maxOfA.append(currentMax)
		
	for idx in range(1, len(array)):
        # Previous entry in maxOfAMinusB compared to (maxOfA - current index)
		currentMax = max(maxOfAMinusB[idx - 1], maxOfA[idx - 1] - array[idx])
		maxOfAMinusB.append(currentMax)
	
	for idx in range(2, len(array)):                        # Starting at 2 because this is the minimum index of c
		currentMax = max(maxOfAMinusBPlusC[idx - 1] , maxOfAMinusB[idx - 1] + array[idx])
		maxOfAMinusBPlusC.append(currentMax)
		
	for idx in range(3, len(array)):                        # Starting at 3 because this is the minimum index of d
		currentMax = max(maxOfAMinusBPlusCMinusD[idx - 1], maxOfAMinusBPlusC[idx - 1] - array[idx])
		maxOfAMinusBPlusCMinusD.append(currentMax)

    # Last index of this array is the solution to the problem
	return maxOfAMinusBPlusCMinusD[len(maxOfAMinusBPlusCMinusD) - 1] 


####################################################
## Brute force
## Time: O(n^4) - where n is 
## Space: O(1) - 
####################################################

def maximizeExpression(array):
    if len(array) < 4:
        return 0
    
    maximumValueFound = float("-inf")
    
    for a in range(len(array)):
        aValue = array[a]
        for b in range(a + 1, len(array)):
            bValue = array[b]
            for c in range(b + 1, len(array)):
                cValue = array[c]
                for d in range(c + 1, len(array)):
                    dValue = array[d]
                    expressionValue = evaluateExpression(aValue,bValue,cValue,dValue)
                    maximumValueFound = max(expressionValue, maximumValueFound)
				
	return maximumValueFound
	
def evaluateExpression(a,b,c,d):
    # Helper function demonstrates that you can change the arithmetic without changing the main function
	return a - b + c - d