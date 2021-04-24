"""
----- NAME: ZigZag Traverse -----
----- Category: Arrays -----
----- Level: Hard -----
------ BRIEF ------
- Write a function that takes in an "n x m" two-dimensional array (that can be square shaped when n == m) 
and returns one-dimensional array of all the arrays elements in zigzag order.

ZigZag oreder strart at the top left coroner of the two-dimensional array, goes down by one element, 
and proceeds in a zigzag pattern all the way to the bottom right order.

Sample input:
array = [
    [1, 3, 4,10],
    [2, 5, 9,11],
    [6, 8,12,15],
    [7,13,14,16]
]
Sample output:
[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]

------ Hints ------
- Don't overthink this question by trying to come up with a clever way of getting the zigzag order.
Think about the simplest checks that need to be made to decide when and how to change direction throughout this exact reversal.

- Starting at the top left corner, iterate through the two-dimensional array by keeping track of the direction that you're moving in (up or down).

If you're moving up, 
you know that you need to move in an up-right pattern and that you need to handle the case where you hit the top or the right borders of the array.

If you're moving down,
 you need to know that you need to move in a down-left pattern and that you need to handle the case where you hit the left or the bottom borders of the array.

- When going up, if you hit the right border, you'll have to go down one element;
If you hit the top border, you'll have to go right one element. 
Similarly, when going down, if you hit the left border, you'll have to go down one element; 
if you hit the bottom border, you'll have to go right on the element.

------ Complexity ------ 
Time: O(n) - where n is total number of elements in the array  
Space: O(n) - We have to store all elements in our final array 
------ Approach ------
"""
####################################################
## Time: O(n) - where n is the length of the 2D array
## Space: O(n) - We have to store all elements in our final array 
####################################################

def zigzagTraverse(array):
    

    height = len(array) - 1
    width = len(array[0]) - 1
    result = []                         # we will appending all the values to this
    row, col = 0, 0
    goingDown = True

    # Checking if we ever at the perimeter?
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])                  # save the current value to the result

        # now check out position?
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:                       # are we at the bottom?
                    col += 1                            # ... go to the right.
                else:
                    row += 1
            else:                                       # ... then go diagonally down
                row += 1
                col -= 1
        
        # We must be going up 
        else:
            if row == 0 or col == width:                # Are we at the top row of the last column? 
                goingDown = True
                if col == width:                        # we are at the boarder 
                    row += 1                            # ... go down a row.
                else:
                    col += 1
            else:
                row -= 1                                # opposite of the similar lines above
                col += 1
    return result
        

def isOutOfBounds(row, col, height, width):
    return (row < 0) or (row > height) or (col < 0) or (col > width)