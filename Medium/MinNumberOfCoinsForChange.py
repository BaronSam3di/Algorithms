"""
----- NAME: Min number of Coins for Change -----
----- Category: Dynamic programming -----
----- Level: Medium -----
------ BRIEF ------

Given an array of positive integers represeting coin denominations and a single non-negative integer n representing a target amount of money,
write a function that return the smallest number of coins needed to make change for (to sum up to) that target amount using the given coin denominations.

Note that you have access to an unlimited amount of coins. In other words, if the denomination are [1, 5, 10], 
you have access to an unlimited amount of 1's 5s and 10s. 

If it's impossible to male change for hte target amount return -1.

Sample Input n = 7
denoms = [1, 5, 10]

------ Hints ------
- Try building an array of the minimum number of coins needed to make change for all amounts between zero and n inclusive.
Note that no coins and needed to make change for 0: in order to make change 40, you do not need to use any coins.

- Build up the array mentioned above one coin the nomination at a time. In other words, find the minimum number of coins needed to make change for
 all amounts between zero and then with only one denomination, then with two, et cetera. Until you use all denominations.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
- First solve solutions to small problems 
if denom <= amount: 
    update the numsOfAmount[amount] = min (nums[amount])
"""

####################################################
## Time: O(nd) - where n is is the target and d is the amount of denominations 
## Space: O(n) - 
####################################################


def minNumberOfCoinsForChange(n, denoms):
    # declare numOfCoins with infs as base case to help instead of compareing with things like null/None
    numOfCoins = [float("inf") for amount in range(n + 1)]                              
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):                                           # amount based on the value of the range
            if denom <= amount:                                                         # eg £2 to make £1 we just move on

                # assigning the numberOfcoins as the min of the existing (poss inf ) and (denom - amount ) + 1
                numOfCoins[amount] = min(numOfCoins[amount] , numOfCoins[amount - denom] + 1)

    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1                   # Turnery to catch any "inf" and follow the breif