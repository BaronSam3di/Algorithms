"""
----- NAME: Search in sorted matrix -----
----- Category: Searching -----
----- Level : Medium -----
------ BRIEF ------


You're given a two-dimensional array (a matrix) of distinct integers and a target integer.
Each row in the matrix is sorted, and each column is also sorted; the matrix doesn't necessarily have the same height and width.

Note: Every number in the matrix will have larger numbers underneath it, and smaller numbers to the left of it.

Write a function that returns in a ray of the row and column indices of the target integer if it's contained in the matrix,
otherwise return [-1,-1].

------ Hints ------

- Pick any number in the matrix and compare it to the target number. 
If this number is bigger than the target number, 
what does that tell you about all of the other numbers in this number is row and this number is column? 
What about if this number is smaller than the target number?

- Try starting at the top right corner of the matrix, comparing the number there to the target number,
and using whatever you gathered from him #1 to figure out what number to compare next if
 the top right number isn't equal to the target number.
 Continue until you find the target number or until you get past the extremities of the matrix. 

------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""

####################################################
## Time: O(n + m) | Space: O(1) - Where N is the length of the columns, M is the length of the rows
####################################################

def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >= 0:               # while our coords are still valid positions in the matrix. if row is the length and the col is < 0, we are done.
        if matrix[row][col] > target:
            col -= 1                                    # eliminate all the numbers below and move left
        elif matrix[row][col] < target:
            row += 1                                    # moving our position down
        else:
            return [row,col]
    return [-1,-1]