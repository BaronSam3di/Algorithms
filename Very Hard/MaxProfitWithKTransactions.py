"""
----- NAME: Max Profit with K transactions -----
----- Category: Dynamic programming -----
----- Level: Very Hard  -----
------ BRIEF ------
You're given an array of positive integers representing the prices of a single stock on various days (each index in the array represents a different day.
You're also given an integer K, which represents the number of transactions you're allowed to make.
One transaction consists of buying the stock on a given day and selling it on another, late today.

Write a function that returns the maximum profit you can make by buying and selling the stock, given K transactions.

Note that you can only hold one share of the stock at a time; in other words, you can't buy more than one share of the stock on any given day,
and you can't buy a share of the stock if you're still holding another share.
Also, you don't need to use all K transactions that you're allowed.

Sample input:
prices = [5 ,11, 3, 50, 60, 90]
k = 2

Sample Output:

93 # Buy: 5, Sell: 11; Buy: 3, Sell: 90

------ Hints ------

- Try building a two dimensional array of the maximum profit she can make on each day with zero, one, two, etc., k transactions. 
Let columns represent days and rows represt the number of transactions. 

- Build up the array mentioned above one row at a time. In other words, find the maximum profits that you can make on each day with a zero transactions first, 
then with one transaction, etc until you reach k transactions. Find a formula that relates the maximum profit at any given point to previous profits. 
Once you find that formula, identify certain values that you repeatedly need and that you can temporarily store to optimise your algorithm.

- Do you really need to store the entire two-dimensional Ray mentioned above? 
Identify what stored values you actually use throughout the process of building the right and come up with a way of storing only what you need and nothing more.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

"""

####################################################
## Time: O(nk) 
## Space: O(nk)  
####################################################

def maxProfitWithKTransactions(prices, k):
    # edge case of no prices
    if not len(prices):
        return 0

    # initialise profits
    profits = [[0 for d in prices] for t in range(k + 1)]

    for t in range(1, k + 1):               # start from one because we don't care for the first price
        maxThusFar = float("-inf")          # initialise to the smallest possible value
        for d in range(1, len(prices)):
            # compare maxThusFar vs buying a stock on day d-1 + the profit on that day with 1 transaction less than our position 
            maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
            profits[t][d] = max(profits[t][d - 1],maxThusFar + prices[d])
    return profits[-1][-1]


####################################################
## similar but with smaller space complexity
## Time: O(nk) - 
## Space: O(n) - 
####################################################

def maxProfitWithKTransactions(prices, k):

    if not len(prices):
        return 0

    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]

    for t in range(1, k + 1):
        maxThusFar = float("-inf")
        if t % 2 == 1:                      # if its an odd number of transactions
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits
        
        # Apply formula
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
            currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
    return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]