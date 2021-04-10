"""
----- NAME: Number of ways to traverse a graph -----
----- Category: Dynamic programming -----
----- Level : Medium -----
# Has a recursive solution 

------ BRIEF ------

You're given to positive integers representing the width and height of the grid-shapeed, rectangular graph.
Write a function in return is the number of ways to reach the bottom right corner of the graph when starting at the top left corner.
Each move you take must either go down or right. In other words, you can never move up or left in the graph.

For example, given the graph illustrated below, with width = 2 and height = 3. there are three ways to reach the bottom right corner when starting at the top left corner:
 _ _
|_|_|
|_|_|
|_|_|

1. Down , Down, Right
2  Right, Down, Down
3. Down , Right, Down

Note: You may assume that with * height >= 2. In other words, the graph will never be 1x1 grid.
------ Hints ------

- Think recursively. How many positions in the graph can access the bottom right corner of the graph?
In other words, what positions do you need to reach before you can reach the bottom right corner?

- The number of ways to reach any position in the graph is equal to the number of ways to
 reach the position directly above it plus the number of ways to reach the position directly to its left.
 This is because you can only travel down and right.

- Can you come up with an efficient way to solve this problem that doesn't repeatedly perform the same work? 
What does dynamic-programming implementation look like?

- To efficiently solve this problem, simply loop through the entire graph, column by column, row by row, and calculate the number of ways to reach a position.
If you're on the top or left edge of the graph, there's only one way to reach your position. If you're anywhere else in the graph, 
the number of ways to reach a position is the number of ways to reach the position directly above it plus 
the number of ways to reach the position directly to its left (which you've already calculated and should be storing). 
Every time you calculate the number of ways to reach position, store the answer so that you can use it later in the calculation of other positions.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

"""



####################################################
# math solution ( Optimal)
## Time: O(n+m) - becasue of the calulation of the factorial
## Space: O(1) - 
####################################################

def numberOfWaysToTraverseGraph(width, height):
    xDistanceToCorner = width - 1
    yDistanceToCorner = height - 1

    # The number of permutations of right and down movements
    # is the number of ways to reach the bottom right corner.
    numerator = factorial(xDistanceToCorner + yDistanceToCorner)
    denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)
    return numerator // denominator     

def factorial(num):
    result = 1
    for n in range(2, num + 1):                             # multiple up to and including n
        result *= n

    return result

####################################################
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################


def numberOfWaysToTraverseGraph(width, height):
    numberOfWays= [[ 0 for _ in range(width + 1)] for _ in range(height + 1)]   # + 1 to take care of index errors

    for widthIdx in range(1, width + 1):                                        # loops though rows and columns
        for heightIdx in range(1, height + 1 ):
            if width == 1 or heightIdx == 1:                                    # this covers our boarder of the graph
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                waysLeft = numberOfWays[heightIdx][widthIdx - 1]                
                waysUp = numberOfWays[heightIdx - 1][widthIdx]
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp           # calculates the the values at each node in the graph

    return numberOfWays[height][width]                                          # return the value represented at the node


####################################################
# Worst method, even though it is recursive
## Time: O(2^(n+m)) - where n is 
## Space: O(n+m) 
####################################################

def numberOfWaysToTraverseGraph(width, height):
    	if width == 1 or height == 1:
		    return 1

	return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width , height - 1)