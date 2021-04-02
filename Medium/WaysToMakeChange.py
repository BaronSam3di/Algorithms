"""
----- NAME: Number of ways to make change-----
----- Category: Dynamic programming -----
----- Level : Medium -----
------ BRIEF ------


Given an array of distinct positive integers representing coin denominations and a single non-negative integer and representing a target amount of money,
Write a function the returns number of ways to make change for that target amount using the given coin denominations.

Note that an unlimited amount of coins is at your disposal.

------ Hints ------


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
Create a ways array , for each way to  ame change
"""

####################################################
## Time: O(nd) - where n is The number and D is that the denomination  
## Space: O(n) - 
####################################################

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]         # initialise to n + 1 filled with 0's
    ways[0] = 1
    for demon in demons:
        for amount in range(1, n+1):            # skip 0 because we juts set it
            if denom <= amount:                 # the coin is less than the change to be given
                ways[amount] += ways[amount - denom] # coming up  with this is a bit tricky
    return ways[n]