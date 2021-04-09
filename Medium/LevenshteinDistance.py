"""
----- NAME: Levenshtein Distance -----
----- Category: Dynamic programming -----
----- Level : Medium -----
------ BRIEF ------
Write a function that takes in two strings and returns the minimum number of 
edit operations that need to be performed on the first string to obtain the second string.

There are three edit operations: 
- Insertion of a character
- Deletion of a character
- Substitution of a character for another


--Sample Input--
str1 = "abc"
str2 = "yabd"

--Sample Ouput--

2 # insert "y"; Substitute "c" for "d"

------ Hints ------


------ Complexity ------ 
Time: O(nm) - Where n is the length of string one and m is the length of string two
Space: O(mn) 

We could loose the array as we are only ever useing two entire rows/
Space = O(min(m,n))

------ Approach ------
 - BUild a 2D array. at each index we store the 
 10 mins in the walkthrough explains the crx of the algo
 Formula 
 if sttr1[r-1] == str2[c-1]:        # r = row, c = column
     E[r][c] = E[r -1 ][c -1 ]  # this is the diagonal
else:
    E[r][c] = 1 + min(E[r][c-1],E[r-1][c],E[r-1][c-1])
"""

####################################################
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################

def levenshteinDistance(str1, str2):
    	
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]       # create the 2D array, the +1 take care of the empty strings
    for i in range(1, len(str2) + 1):                                               # generate the first column
        edits[i][0] = edits[i - 1][0] + 1                                           
	for i in range(1, len(str2) + 1):                                               
        for j in range(1,len(str1) + 1):
			if str2[i - 1] == str1[j-1]:                                            # if the letters are the same
				edits[i][j] = edits[i - 1][j - 1]                                   # move diagonally
			else:
				edits[i][j] = 1 + min(edits[i - 1][j - 1],edits[i - 1][j],edits[i][j - 1])
	return edits[-1][-1]

# o(nm) Time | O(min(n,m)) Space
def levenshteinDistance(str1, str2):
	small = str1 if len(str1) < len(str2) else str2
	big = str1 if len(str1) >= len(str2) else str2
	evenEdits = [x for x in range(len(small) + 1)]
	oddEdits = [None for x in range(len(small) + 1 )]
	for i in range(1, len(big) + 1):
		if i % 2 == 1:
			currentEdits = oddEdits
			previousEdits = evenEdits
		else:
			currentEdits = evenEdits
			previousEdits = oddEdits
		currentEdits[0] = i
		for j in range(1, len(small) + 1):
			if big[i -1] == small[j - 1]:
				currentEdits[j] = previousEdits[j - 1]
			else:
				currentEdits[j] = 1 + min(previousEdits[j-1],previousEdits[j],currentEdits[j-1])
	return evenEdits[-1] if len(big) % 2 ==0 else oddEdits[-1]
