"""
----- SpiralTraverse : Medium -----
------ BRIEF ------

Write a function that take in an n x m 2D array ( that can be a square-shaped when n ==m)
and return a one-dimensional array of all the array's elements in spiral order. 

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, 
and proceeds in a spiral clockwise pattern round the edge all the way inward until
every element has been visited. 

array = [
    [1,  2, 3, 4],
    [12,13,14, 5],
    [11,16,15, 6],
    [10, 9, 8, 7],
]


This question test the code application f simple logic. 
It can be solved both iteratively and recursively.

One approach (not covered) keeps track of your direction, but it is not as clean.

Firstly try and simplify the problem. The problem involves
traversing the perimeter the 2d Array. We then traverse the inner perimitier.

We would take the Starting row, Starting Column, Ending Column and Ending Row and
as we traverse these we will reduce these dimensions to close in on the perimiter beneath.

These 4 values can be taken from the array. 
- Time: O(N) where N is the total number of elements in the array.
- Space: O(N) space because we are storing all N values in another array.

------ Hints ------


------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""

# ## Iterative
# def spiralTraverse(array):
# 	result = []
#     startRow, endRow = 0, len(array) - 1
#     startCol, endCol = 0, len(array[0]) - 1                    # endCol length of the first sub-array

#     while startRow <= endRow and startCol <= endCol:  
        # for col in range(startCol, endCol + 1):                # traverse top boarder, + 1 to be inclusive
        #     result.append(array[startRow][col])

        # for row in range(startRow + 1, endRow + 1):            # +1 to not double count
        #     result.append(array[row][endCol])

        # for col in reversed(range(startCol, endCol)):          # not +1 because python is inclusive
        #     result.append(array[endRow][col])

        # for col in reversed(range(startRow + 1, endRow)):      # not +1 because python is inclusive
        #     result.append(array[endRow][col])

#         startRow += 1
#         endRow -= 1
#         startRow += 1
#         endCol -= 1

        # if startCol == endCol:                                 # edge case
        #     break
    
#     return result


## Recursive
def spiralTraverse(array):
    	result = []
    spiralFill(array, 0, len(array) -1, 0, len(array[0]) -1, result)
    return result


def spiralFill(array, startRow, endRow, startCol, endCol, result):
    # base case 
    if startRow > endRow or startCol > endCol:
        return 
	
		
    for col in range(startCol, endCol + 1):                # traverse top boarder, + 1 to be inclusive
        result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):            # +1 to not double count
        result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):           # not +1 because python is inclusive
		if startRow == endRow:
			break
        result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):      # not +1 because python is inclusive
		if startCol == endCol:                                 # edge case
			break
        result.append(array[row][startCol])
    
    

    spiralFill(array, startRow +1 , endRow -1 , startCol + 1, endCol -1 , result)
