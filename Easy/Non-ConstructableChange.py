"""
----- Non-Constructable Change : Easy -----
------ BRIEF ------
Given an array of positive integers representing the values of coins in your posession. Write a function that returns the minimum amount of change (the minimum sum of money)
that you CANNOT create. The given coins can have any positive integer value and aren't necessarily unique (i.e; you can have multiple coins of the same value).

For example, if you're given `coins = [1,2,5]`, the minimum amount of change that you can't create is 4, because we CAN make 1,3,2,5,6,7,8 but we cannot make 4. We can make 5.
If you're given no coins, the minimum amount of change that you can't create is 1.

------ Hints ------
1. The brute force approach to solve this problem is to attempt to create every single amount of change, starting at 1 and going up until you eventually can't create an amount. 
While this approach works, there is a better one. 

2. Start by sorting the input array. Since you're trying to find the minimum amount of change that you can't create, it makes sense to consider the smallest coins first. 

3.  To understand the trick with this problem, consider the following example: `coins = [1,2,4]`. 
With this set of coins, we can create 1,2,3,4,5,6,7 cents worth of change. Now, if we were to add a coin of value 9 to this set, 
we would NOT be able to create 8 cents. 

However ,if we were to add a coin of value 7, we would be able to create 8 cents, and we would also be able to create all values of change from 1 to 15. 
Why is this the case? 

4. Create a variable to store the amount of change that you can currently create up to. Sort all of your coins, and loop though them in asscending order. 
At every iteration, compare the current coin to the amount of change that you can currently create up to. Here are the two scenarios that you'll encounter.
- The coin value is GREATER than the amount of change that you can currently create plus 1.
- The coin value is SMALLER than or equal to the amount of change that you cna currently create plus 1.

In the first scenario, you simply return the current amount of change that you can create plus 1, because you can't create that amount of change, 
In the second scenario, you add the value of the coin to the amount of change that you can currently create up to, and you continue iterating through the coins. 

The reason for this is that, if you're in the second scenario, you can create all of the values of change that you can currently create plus the value of the coin that you
just considered. If you're given coins [1,2], then you can make 1,2,3 cents. so if you add a coin of 4, then you can make 4 + 1 cents, 4 + 2 cents, and 4 + 3 cents. Thus , you cna make up to 7 cents.  

From a sorted list , if a coin is greater than (the current amount of change that we have + 1), 
U = SetOfCoins
C = Change we can create wit hour coins
V = Arbitrary Individual Coin we are inspecting


U  = {1}
C   = 1

We add V to U. `If V > C + 1 we cannot make C + 1 change`, so for this exercise we would return C + 1 as the lowest change we annnot make

If V <= C + 1, we can make C + V change.

When we get a coin that is greater than the change we can add plus 1, we return the change plus 1 because the smallest value we cannot create.

The C value is how much change we can make up to. 
------ Complexity ------ 
Time: O(n log (n)) 
Space: O(1)  - because we are sorting/working inplace

"""

def nonConstructibleChange(coins):
    coins.sort()                                # sort into assending in place

    currentChangeCreated = 0                    # keep track of change we can create. our C value
    for coin in coins:
        if coin > currentChangeCreated + 1:     # if the coin we are going to add is greater than the current change + 1 , then that is our limit.
            return currentChangeCreated + 1
        
        currentChangeCreated += coin            

    return currentChangeCreated + 1             # if we get to the end of our list then the next number is the lowest we cannot create